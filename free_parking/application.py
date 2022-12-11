from datetime import timedelta


class Application:
    free_parking_time: timedelta = timedelta(hours=2)
    time_format: str = '%Y.%m.%d %H:%M:%S'
