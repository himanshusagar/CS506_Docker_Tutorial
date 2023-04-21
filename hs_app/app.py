import time
from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql_password'
app.config['MYSQL_DATABASE_DB'] = 'mysql_db'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
mysql.init_app(app)

g_init = False

#Create empty DB.
def init_once():
    global g_init
    if g_init:
        return
    g_conn = mysql.connect()
    g_cursor = g_conn.cursor()
    g_cursor.execute("CREATE TABLE IF NOT EXISTS metadata(counter int NOT NULL)")
    g_conn.commit()
    g_cursor.close()
    g_init = True


def get_hit_count():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("INSERT INTO metadata VALUES(0)")
    conn.commit()
    cursor.execute("SELECT COUNT(*) from metadata")
    data = cursor.fetchone()
    return data

@app.route('/')
def hello():
    init_once();
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

   

