from flask import Flask, request

# from utils import


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello TARAS!</h1>'


@app.route('/phone/create')
def phone_create():
    Contact = request.args('ContactName')
    Phone= request.args('PhoneValue')
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql ="""CREATE TABLE IF NOT EXISTS Phones(
    PhoneId INTEGER PRIMARY KEY,
    ContactName varchar(255),
    PhoneValue INTEGER
    );"""


    cur.execute(sql)

    con.commit()
    con.close()

    return 'phone_create'


@app.route('/phone/read')
def phone_read():
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = """
    SELECT * FROM Phones;
    """

    cur.execute(sql)

    resalt = cur.fetchall()
    con.close()
    return resalt


@app.route('/phone/updata')
def phone_update():
    return 'phone_update'


@app.route('phone/delete')
def phone_delete():
    return 'phone_delete!!!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
