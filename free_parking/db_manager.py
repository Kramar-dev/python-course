from logger import Log
from time_utils import TimeUtils
from defines import status
from defines import text

class DbManager:

    def __init__(self, db_name: str):
        self.db_name = db_name

    def open_db(self):
        Log.i(text.DB_OPEN)

    def close(self):
        Log.i(text.DB_CLOSED)

    def get_car_status(self, number: str) -> (status, str):
        if not self.is_exists(number):
            return status.NOT_EXISTS, ''
        saved_time = self.get_time_by_number_str(number)
        if TimeUtils.is_time_elapsed(saved_time):
            return status.TIME_ELAPSED, ''
        return status.OK, TimeUtils.time_left(saved_time)

    def save_if_not_exists(self, number: str) -> bool:
        if self.is_exists(number):
            return False
        with open(self.db_name, 'a') as f:
            f.write(TimeUtils.add_timestamp(number.strip()))
            return True

    def is_exists(self, number: str) -> bool:
        with open(self.db_name, 'r') as f:
            lines = f.readlines()
            try:
                for line in lines:
                    only_number = line[line.index('|') + 2:].strip()
                    if number.strip() == only_number:
                        return True
            except ValueError:
                return False

    def get_time_by_number_str(self, number: str) -> str:
        with open(self.db_name, 'r') as f:
            lines = f.readlines()
            try:
                for line in lines:
                    only_number = line[line.index('|') + 2:].strip()
                    if number.strip() == only_number:
                        return line[:line.index('|')-1].strip()
            except ValueError:
                return ''

    def drop_db(self):
        open(self.db_name, 'w').close()


db = DbManager('db.txt')
db.open_db()

