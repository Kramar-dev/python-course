from enum import Enum


class Status(Enum):
    OK = 0
    TIME_ELAPSED = 1
    NOT_EXISTS = 2


class Text:
    OK = 'OK'
    DB_OPEN = 'Database open successfully'
    DB_CLOSED = 'Database closed successfully'
    NOT_EXISTS = 'Number is not exists in database'
    TIME_ELAPSED = 'Parking time is elapsed!'
    NOT_IMPLEMENTED = 'Unsupported path'
    SAVE_TO_DB = 'Saved successfully'
    NUMBER_ALREADY_EXISTS = 'Already exists in database'
    HTTP_SERVER_RUNNING = 'Http server is running...'
