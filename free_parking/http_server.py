from free_parking.db_manager import db
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import sys
name = str(__file__)
index = name.index('\\free_parking\http_server.py') + 1
sys.path.append(name[:index])

from logger import Log
from car_status import status
#from ansicolors import Colors


class HttpServer:
    class BaseServer(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/read':
                content_len = int(self.headers.get('Content-Length'))
                # check by regex
                number = self.rfile.read(content_len).decode()
                self.__on_get_number(number)
                return
            self.__on_unknown_path()

        def do_PUT(self):
            if self.path == '/write':
                content_len = int(self.headers.get('Content-Length'))
                # check by regex
                number = self.rfile.read(content_len).decode()
                self.__on_save_number(number)
                return
            self.__on_unknown_path()

        def __on_get_number(self, number: str):
            Log.i(f'on get number {number}')
            car_status = db.get_car_status(number)
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            response: str
            match car_status:
                case status.NOT_EXISTS:
                    response = 'Number is not exists in database'
                case status.TIME_ELAPSED:
                    response = 'Parking time is elapsed!'
                case _:
                    response = db.get_time_by_number(number)
            self.wfile.write(bytes(response, 'utf-8'))

        def __on_unknown_path(self):
            self.send_response(HTTPStatus.NOT_IMPLEMENTED)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Unsupported path", "utf-8"))

        def __on_save_number(self, number: str):
            Log.i(f'on save number {number}')
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            if db.save_if_not_exists(f'{number}\n'):
                self.wfile.write(bytes("Saved successfully", "utf-8"))
                return
            self.wfile.write(bytes("Already exists in database", "utf-8"))

    def __init__(self, host: str, port: int):
        self.server: HTTPServer
        self.__host = host
        self.__port = port

    def start(self):
        self.server = HTTPServer((self.__host, self.__port), self.BaseServer)
        self.server.serve_forever()

    def stop(self):
        self.server.server_close()


