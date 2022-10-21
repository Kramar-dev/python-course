from ansicolors import *


class Log:
    @staticmethod
    def v(text):
        print(text)
    
    @staticmethod
    def d(text):
        print(f'{Colors.LIGHT_CYAN}{text}{Colors.END}')
    
    @staticmethod
    def i(text):
        print(f'{Colors.LIGHT_GREEN}{text}{Colors.END}')
    
    @staticmethod
    def w(text):
        print(f'{Colors.YELLOW}{text}{Colors.END}')
    
    @staticmethod
    def e(text):
        print(f'{Colors.LIGHT_RED}{text}{Colors.END}')
