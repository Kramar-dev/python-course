import requests
from defines import text
from free_parking.db_manager import db
from logger import Log


class TestNumberChecker():

    def test_read_before(self):
        db.drop_db()
        reader = requests.get(url='http://127.0.0.1:12345/read', data='GD 123 GKA')
        if reader.text == text.NOT_EXISTS:
            Log.i('Test 1 passed')
            db.drop_db()
            return
        Log.e('Test 1 not passed')

    def test_write(self):
        writer = requests.put(url='http://127.0.0.1:12345/write', data='GD 123 GKA')
        if writer.text == text.SAVE_TO_DB:
            Log.i('Test 2 passed')
            db.drop_db()
            return
        Log.e('Test 2 not passed')

    def test_read_after(self):
        reader = requests.get(url='http://127.0.0.1:12345/read', data='GD 123 GKA')
        if reader.text != '':
            Log.i('Test 3 passed')
            db.drop_db()
            return
        Log.e('Test 3 not passed')
        db.drop_db()
