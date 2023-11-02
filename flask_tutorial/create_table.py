def create_table() -> None:
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS Phones(
    PhoneId INTEGER PRIMARY KEY,
    ContactName varchar(255),
    PhoneValue INTEGER
    );
    """

    cur.execute(sql)

    con.commit()
    con.close()
    return 'phone_create'
