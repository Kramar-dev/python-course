from api_dispatcher import Api
from ansicolors import Colors


def main():
    exit_app = False
    api = Api()
    while not exit_app:
        try:
            command = input(f'{Colors.BLUE}\nEnter command:\n{Colors.END}')
            exit_app = api.on_message(command)
        except KeyboardInterrupt:
            exit(0)


if __name__ == '__main__':
    main()
