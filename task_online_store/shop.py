from logger import Log
from db import *


class Shop:
    def __init__(self):
        self.current_user: str = ''
        self.users = Users().db
        self.goods = Goods()
        self.items = self.goods.db

    def login_procedure(self, user_login: str, user_password: str) -> str:
        user = self.users.get(user_login)
        if user is None:
            return 'User is not exists'
        if user.password != user_password:
            return 'Password is incorrect'
        if user.authorized:
            return 'Already authorized'
        self.users[user_login].authorized = True
        self.current_user = user.login
        return ''

    def logout_procedure(self):
        if self.authorized():
            self.users[self.current_user].authorized = False
            self.current_user = ''
            Log.i('Logout successful')

    def show_all_goods(self):
        for item_id, item in self.items.items():
            Log.v(f'{item_id}  {item.name}  {item.price}')

    def show_goods(self, name: str):
        count = 0
        for item_id, item in self.items.items():
            if name.lower() in item.name.lower():
                count += 1
                Log.v(f'{item_id}  {item.name}  {item.price}')
        if count == 0:
            Log.w('Sorry, no items in the store :(')

    def add_good_to_basket(self, item_id: int):
        if not self.authorized():
            Shop.show_not_auth_error()
            return
        exists = self.users[self.current_user].basket.get(item_id)
        if exists is None:
            self.users[self.current_user].basket[item_id] = ShoppingBasketItem(1, self.items[item_id].price)
            return
        self.users[self.current_user].basket[item_id].count += 1
        self.users[self.current_user].total_price += self.items[item_id].price

    def remove_one_item_from_basket(self, item_id: int):
        if not self.authorized():
            Shop.show_not_auth_error()
            return
        exists = self.users[self.current_user].basket.get(item_id)
        if exists is not None:
            self.users[self.current_user].basket[item_id].count -= 1
            self.users[self.current_user].total_price -= self.items[item_id].price

    def clear_basket(self):
        if not self.authorized():
            Shop.show_not_auth_error()
            return
        self.users[self.current_user].basket.clear()
        self.users[self.current_user].total_price = 0

    def print_basket(self):
        if not self.authorized():
            Shop.show_not_auth_error()
            return
        basket = self.users[self.current_user].basket
        for item_id, item in basket.items():
            Log.v(f'{self.items[item_id].name}  [{item.count}]  {item.price}')

    def finalize_order(self):
        if not self.authorized():
            Shop.show_not_auth_error()
            return
        for item_id, item in self.users[self.current_user].basket.items():
            if self.items[item_id].count < item.count:
                Log.e(f'Sorry, there is not enough {self.items[item_id].name} in the store, we have only'
                      f' {self.items[item_id].count}')
                return
            self.items[item_id].count -= item.count
            self.users[self.current_user].history.append(HistoryItem(item_id, item.count, item.price))
        self.clear_basket()
        Log.i(f'Order finalized - total price - {self.users[self.current_user].total_price}')

    def change_password(self, password: str, user_id: str = ''):
        user_id = ''
        if user_id == '':
            us_id = self.current_user
        else:
            us_id = user_id
        if self.current_user == '':
            Shop.show_not_auth_error()
            return
        if len(password) < 8:
            Log.e('Password length is less than 8')
            return
        if password == self.users[us_id].password:
            Log.w('You entered old password')
            return
        self.users[us_id].password = password
        Log.i('Password changed successfully')

    @staticmethod
    def show_not_auth_error():
        Log.e('Not authorized')

    @staticmethod
    def show_not_admin_error():
        Log.e('You are not admin')

    def add_item(self):
        if not self.is_admin():
            Shop.show_not_admin_error()
            return
        price_int = -1
        count_int = -1
        while True:
            Log.d('Enter new product name:')
            name = input()
            if len(name) < 1:
                Log.w('Too short name')
                continue
            break

        while True:
            Log.d('Enter price:')
            price = input()
            try:
                price_int = int(price)
                break
            except:
                Log.w('Incorrect value')
                continue

        while True:
            Log.d('Enter product count:')
            count = input()
            try:
                count_int = int(count)
                break
            except:
                Log.w('Incorrect value')
                continue

        self.items[self.goods.next_id()] = Good(name, price_int, count_int)
        Log.i('Product added successfully')

    def remove_item(self, item_id: id):
        if not self.authorized():
            Shop.show_not_auth_error()
            return
        item = self.items.get(item_id)
        if item is None:
            Log.e('Sorry, this id does not exists in database')
            return
        del self.items[item_id]

    def change_item_count(self, item_id: int, new_count: int):
        if not self.authorized():
            Shop.show_not_auth_error()
            return
        self.items[item_id].count = new_count

    def change_item_price(self, item_id: int, new_price: int):
        if not self.authorized():
            Shop.show_not_auth_error()
            return
        self.items[item_id].price = new_price

    def add_user(self):
        if not self.is_admin():
            Shop.show_not_admin_error()
            return
        while True:
            Log.d('Enter new user\'s login:')
            login = input()
            if not Users.login_correct(login):
                Log.e('Entered login is incorrect')
                continue
        while True:
            Log.d('Enter new user\'s login:')
            password = input()
            if not Users.password_correct(password):
                Log.e('Entered login is incorrect')
                continue
        # TODO set user type while adding new user
        self.users[login] = User(login, password, False, False, {}, 0, [])
        Log.i(f'User {login} added successfully')

    def remove_user(self):
        if not self.is_admin():
            Shop.show_not_admin_error()
            return
        while True:
            Log.d('Enter user\'s login to delete from database')
            login = input()
            exists = self.users.get(login)
            if exists is None:
                Log.w('Sorry, this user does not exists in database')
                continue
        del self.users[login]


    def change_user_password(self, new_password: str, user_id: str):
        if not self.authorized():
            Shop.show_not_auth_error()
            return
        self.change_password(new_password, user_id)
        Log.i('Password changed successfully')

    def show_user_info(self, user_id: str):
        if not self.authorized():
            Shop.show_not_auth_error()
            return
        user = self.users.get(user_id)
        if user is None:
            Log.d('Sorry, this user does not exists in database')
            return
        Log.i(user)

    def authorized(self) -> bool:
        if self.current_user == '':
            self.show_not_auth_error()
            return False
        return True

    def is_admin(self) -> bool:
        if not self.authorized():
            self.show_not_auth_error()
            return False
        if self.users[self.current_user].is_admin:
            return True
        return False

