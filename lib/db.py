import sqlite3

try:
    import settings
except:
    print('settings not in pythonpath')

def _execute(query):
    dbPath = ''
    connection = sqlite3.connect(settings.dbPath)
    cursorobj = connection.cursor()
    try:
            cursorobj.execute(query)
            result = cursorobj.fetchall()
            connection.commit()
    except Exception:
            raise
    connection.close()
    return result