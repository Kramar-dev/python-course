from http_server import HttpServer
from free_parking.db_manager import db

if __name__ == '__main__':
    http_server = HttpServer("localhost", 12345)
    try:
        http_server.start()
    except KeyboardInterrupt:
        db.close()
        http_server.stop()
        exit(0)


