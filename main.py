from bs4 import BeautifulSoup
import requests
import os
from winotify import Notification, audio

URL = "https://www.gov.pl/web/kas/komunikaty"
FILE_NAME = "messages.txt"


def extract_last_num_page(tag):
    begin = str(tag).index('[') + 1
    end = str(tag).index(']')
    try:
        res = int(str(tag)[begin:end])
        return res
    except Exception:
        print(f'extract_last_num_page() fail: {Exception}')
        return 1


def get_page_nums():
    page_nums = []
    response = requests.get(URL)
    parsed = BeautifulSoup(response.text, 'html.parser')
    tags = parsed.find_all('span')
    for tag in tags:
        tmp = str(tag)
        if 'Przejdź do ostatniej strony wyników' in tmp:
            last_page = extract_last_num_page(tag)
            for page in range(1, last_page+1):
                page_nums.append(page)
            return page_nums
    return [1]


def read_old_messages():
    with open(FILE_NAME, 'r') as file:
        return file.read().split('\n')


def get_current_messages():
    page_nums = get_page_nums()
    messages = []
    for page_num in page_nums:
        response = requests.get(f'{URL}?page={page_num}')
        parsed = BeautifulSoup(response.text, 'html.parser')
        tags = parsed.find_all('div')
        for tag in tags:
            tag.find('h2')
            if "Komunikat nr " in str(tag.string):
                messages.insert(0, tag.string)
    return messages


def show_new_message_notification(message):
    toast = Notification(app_id='gov.pl',
                         title="Nowy komunikat \U00002709",
                         msg=message,
                         duration="long",
                         icon=f'{os.getcwd()}/govpl.jpg')
    toast.set_audio(audio.Default, loop=False)
    toast.add_actions(label='Przejdź do strony', launch=f'{URL}?page=1')
    toast.show()


def rewrite_old_messages(msgs):
    with open(FILE_NAME, 'w', encoding="utf-16") as file:
        for line in msgs:
            file.write(f'{line}\n')


def main():
    try:
        old_messages = read_old_messages()
        current_messages = get_current_messages()
        if len(old_messages) == 1:  # is empty
            rewrite_old_messages(current_messages)
            return
        old_messages.pop(-1)  # delete last '\n' while reading the file
        if old_messages[-1] != current_messages[-1]:
            show_new_message_notification(current_messages[-1])
            rewrite_old_messages(current_messages)
    except Exception as E:
        print(E)


if __name__ == '__main__':
    main()


