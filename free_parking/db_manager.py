from logger import Log
from car_status import status
from time_utils import TimeUtils


class DbManager:
    def open(self, db_name: str):
        self.db_name = db_name
        Log.v('Database opened successfully')

    def close(self):
        Log.v('Database closed successfully')

    def get_car_status(self, number: str) -> status:
        if not self.is_exists(number):
            return status.NOT_EXISTS
        saved_time = self.get_time_by_number(number)
        if TimeUtils.is_time_elapsed(saved_time):
            return status.TIME_ELAPSED
        return TimeUtils.time_elapsed(saved_time)

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

    def get_time_by_number(self, number: str) -> str:
        with open(self.db_name, 'r') as f:
            lines = f.readlines()
            try:
                for line in lines:
                    only_number = line[line.index('|') + 2:].strip()
                    if number.strip() == only_number:
                        only_time = line[:line.index('|')-1].strip()
                        return only_time
            except ValueError:
                return ''


db = DbManager()
db.open('db.txt')

