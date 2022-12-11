from http_server import HttpServer
from free_parking.db_manager import db
from tests import TestNumberChecker
from threading import Thread
from time import sleep


def tests():
    sleep(1.0)
    tester = TestNumberChecker()
    tester.test_read_before()
    tester.test_write()
    tester.test_read_after()


if __name__ == '__main__':
    http_server = HttpServer("localhost", 12345)
    try:
        Thread(target=http_server.start).start()
        Thread(target=tests).start()
    except KeyboardInterrupt:
        db.close()
        http_server.stop()
        exit(0)
