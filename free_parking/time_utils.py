import time


class TimeUtils:
    @staticmethod
    def add_timestamp(data: str) -> str:
        date_time = TimeUtils.current_time()
        return f'{date_time} | {data}'

    @staticmethod
    def is_time_elapsed(saved_time: str) -> bool:
        current = TimeUtils.current_time()
        return False  #TODO

    @staticmethod
    def time_elapsed(saved_time: str) -> str:
        pass  #TODO

    @staticmethod
    def current_time():
        return time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
