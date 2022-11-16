from shop import Shop
from logger import Log
from db import Users


class Api:
    shop = Shop()

    def on_message(self, message: str) -> bool:
        match message:
            case '/exit':
                # self.logout_procedure()
                return True

            case '/login':
                self.login_procedure()

            case '/logout':
                self.logout_procedure()

            case '/show-all-items':
                self.show_all_goods()

            case '/show-item':
                self.show_item()

            case '/add-to-basket':
                self.add_to_basket()

            case '/show-all-in-basket':
                self.show_all_in_basket()

            case '/clear-basket':
                self.clear_basket()

            case '/remove-item-from-basket':
                self.remove_item_from_basket()

            case '/finalize-order':
                self.finalize_order()

            case '/change-password':
                self.change_password()

            # ============ ADMIN PANEL ============ #
            case '/add-item-to-store':
                self.add_item_to_store()

            case '/remove-item-from-store':
                self.remove_item_from_store()

            case '/change-item-count':
                self.change_item_count()

            case '/change-item-price':
                self.change_item_price()

            case '/add-user':
                self.add_user()

            case '/remove-user':
                self.remove_user()

            case '/change-user-password':
                self.change_user_password()

            case '/show-user-info':
                self.show_user_info()

            case '/change-user-type':
                self.set_user_type_to_admin()
                pass

            case _:
                Api.print_help()
        return False

    def login_procedure(self):
        login = input('Enter login:\n')
        password = input('Enter password:\n')
        res = self.shop.login_procedure(login, password)
        if res == '':
            Log.i('Login successful')
            return
        Log.e(res)

    def logout_procedure(self):
        self.shop.logout_procedure()

    def show_all_goods(self):
        self.shop.show_all_goods()

    def show_item(self):
        look_for = input('Enter what are You looking for:\n')
        self.shop.show_goods(look_for)

    def add_to_basket(self):
        item_id = self.get_user_input_int('product id')
        self.shop.add_good_to_basket(item_id)

    def show_all_in_basket(self):
        self.shop.print_basket()

    def clear_basket(self):
        self.shop.clear_basket()

    def remove_item_from_basket(self):
        item_id = self.get_user_input_int('product id')
        self.shop.remove_one_item_from_basket(item_id)

    def finalize_order(self):
        self.shop.finalize_order()

    def change_password(self):
        password = input('Enter new password')
        self.shop.change_password(password)

    def add_item_to_store(self):
        self.shop.add_item()

    def remove_item_from_store(self):
        if not self.shop.is_admin():
            Shop.show_not_admin_error()
            return False
        item_id = Api.get_user_input_int('product id')
        self.shop.remove_item(item_id)

    def change_item_count(self):
        if not self.shop.is_admin():
            Shop.show_not_admin_error()
            return False
        item_id = Api.get_user_input_int('product id')
        item_count = Api.get_user_input_int('product count')
        self.shop.change_item_count(item_id, item_count)

    def change_item_price(self):
        if not self.shop.is_admin():
            Shop.show_not_admin_error()
            return False
        item_id = Api.get_user_input_int('product id')
        item_price = Api.get_user_input_int('product price')
        self.shop.change_item_price(item_id, item_price)

    def add_user(self):
        self.shop.add_user()

    def remove_user(self):
        self.shop.remove_user()

    def change_user_password(self):
        if not self.shop.is_admin():
            Shop.show_not_admin_error()
            return
        Log.d('Enter password:')
        password = input()
        if len(password) < 8:
            Log.e('Password is too short')
            return False
        Log.d('Enter user\'s login:')
        login = input()
        if not Users.login_correct(login):
            Log.e('Incorrect login')
            return False
        self.shop.change_user_password(password, login)

    def show_user_info(self):
        if not self.shop.is_admin():
            Shop.show_not_admin_error()
            return
        Log.d('Enter user login:')
        login = input()
        self.shop.show_user_info(login)

    def set_user_type_to_admin(self):
        if not self.shop.is_admin():
            Shop.show_not_admin_error()
            return
        Log.d('Enter user login:')
        login = input()
        self.shop.set_user_type_to_admin(login)
        
    @staticmethod
    def print_help():
        Log.i('usage:\n'
              '/exit\n'
              '/login\n'
              '/logout\n'
              '/show-all-items\n'
              '/show-item\n'
              '/add-to-basket\n'
              '/show-all-in-basket\n'
              '/clear-basket\n'
              '/remove-item-from-basket\n'
              '/finalize-order\n'
              '/change-password\n'
              '/add-item-to-store\n'
              '/remove-item-from-store\n'
              '/change-item-count\n'
              '/change-item-price\n'
              '/add-user\n'
              '/remove-user\n'
              '/change-user-password\n'
              '/show-user-info\n'
              '/change-user-type')

    @staticmethod
    def get_user_input_int(dialog: str) -> int:
        while True:
            try:
                value = int(input(f'Enter {dialog}:\n'))
                if value > 0:
                    return value
            except:
                Log.e('Incorrect integer value')
