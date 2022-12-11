import types


status = types.SimpleNamespace()
status.OK = 0
status.TIME_ELAPSED = 1
status.NOT_EXISTS = 2

text = types.SimpleNamespace()
text.OK = 'OK'
text.DB_OPEN = 'Database open successfully'
text.DB_CLOSED = 'Database closed successfully'
text.NOT_EXISTS = 'Number is not exists in database'
text.TIME_ELAPSED = 'Parking time is elapsed!'
text.NOT_IMPLEMENTED = 'Unsupported path'
text.SAVE_TO_DB = 'Saved successfully'
text.NUMBER_ALREADY_EXISTS = 'Already exists in database'
text.HTTP_SERVER_RUNNING = 'Http server is running...'
