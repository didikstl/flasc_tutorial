from flask import Flask, request
from utils import commit_sql

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello TARAS!</h1>'


@app.route('/phone/create')
def phone_create():
    contactName = request.args('ContactName', 'Bob')
    phoneValue = request.args('PhoneValue', 22)
    sql = f"""
    INSERT INTO Phones(ContactName, PhoneValue)
    VALUES ({contactName, phoneValue});
    """
    commit_sql(sql)

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


@app.route('/phone/update')
def phone_update():
    phoneId = request.args['PhoneId']
    contactName = request.args['ContactName']
    phoneValue = request.args['PhoneValue']
    sql = f"""
    UPDATE Phones
    SET ContactName ='{contactName}', PhoneValue = {phoneValue}
    WHERE PhoneId= {phoneId};
    """
    commit_sql(sql)

    return 'phone_update'


@app.route('/phone/delete')
def phone_delete():
    phoneId = request.args['PhoneId']
    sql = f"""
    DELETE FROM Phones
    WHERE PhoneId= {phoneId}
    """
    commit_sql(sql)

    return 'phone_delete!!!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
