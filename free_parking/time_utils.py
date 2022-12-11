from datetime import datetime, timedelta
from application import Application


class TimeUtils:
    @staticmethod
    def add_timestamp(data: str) -> str:
        date_time = TimeUtils.current_time_to_str()
        return f'{date_time} | {data}'

    @staticmethod
    def is_time_elapsed(saved_time: str) -> bool:
        current_time_obj = TimeUtils.current_time()
        saved_time_obj = TimeUtils.str_time_to_object(saved_time)
        return (current_time_obj - saved_time_obj) > Application.free_parking_time

    @staticmethod
    def time_elapsed(saved_time: datetime | str) -> timedelta:
        if saved_time is datetime:
            return TimeUtils.current_time() - saved_time
        return TimeUtils.current_time() - TimeUtils.str_time_to_object(saved_time)

    @staticmethod
    def time_left(saved_time: datetime | str) -> timedelta:
        return Application.free_parking_time - TimeUtils.time_elapsed(saved_time)

    @staticmethod
    def current_time_to_str():
        return datetime.now().strftime(Application.time_format)

    @staticmethod
    def current_time():
        return datetime.now()

    @staticmethod
    def str_time_to_object(saved_time: str) -> datetime:
        return datetime.strptime(saved_time, Application.time_format)
