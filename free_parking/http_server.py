from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
from logger import Log
from defines import status
from defines import text
from free_parking.db_manager import db


class HttpServer:
    class BaseServer(BaseHTTPRequestHandler):
        def do_GET(self):
            match self.path:
                case '/read':
                    try:
                        content_len = int(self.headers.get('Content-Length'))
                        number = self.rfile.read(content_len).decode()
                        self.__on_get_number(number)
                    except TypeError:
                        Log.e('/read failed')
                    return
                case _:
                    self.__on_unknown_path()

        def do_PUT(self):
            match self.path:
                case '/write':
                    #try:
                    content_len = int(self.headers.get('Content-Length'))
                    number = self.rfile.read(content_len).decode()
                    self.__on_save_number(number)
                    #except TypeError:
                    #Log.e('/write failed')
                    return
                case _:
                    self.__on_unknown_path()

        def __on_get_number(self, number: str):
            car_status, time_left = db.get_car_status(number)
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = ''
            match car_status:
                case status.NOT_EXISTS:
                    response = text.NOT_EXISTS
                case status.TIME_ELAPSED:
                    response = text.TIME_ELAPSED
                case status.OK:
                    response = str(time_left)
            self.wfile.write(bytes(response, 'utf-8'))

        def __on_unknown_path(self):
            self.send_response(HTTPStatus.NOT_IMPLEMENTED)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes(text.NOT_IMPLEMENTED, 'utf-8'))

        def __on_save_number(self, number: str):
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            if db.save_if_not_exists(f'{number}\n'):
                self.wfile.write(bytes(text.SAVE_TO_DB, 'utf-8'))
                return
            self.wfile.write(bytes(text.NUMBER_ALREADY_EXISTS, 'utf-8'))

    def __init__(self, host: str, port: int):
        self.server: HTTPServer
        self.__host = host
        self.__port = port

    def start(self):
        self.server = HTTPServer((self.__host, self.__port), self.BaseServer)
        Log.i(text.HTTP_SERVER_RUNNING)
        self.server.serve_forever()

    def stop(self):
        self.server.server_close()


