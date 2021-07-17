import psycopg2
#what do I parameters do i put into line 5 and line 22???

def save_canvas(canvas_id, data_url):
    conn = psycopg2.connect(database="testdb", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432") #connecting to database

    cur = conn.cursor()
    cur.execute('''CREATE TABLE BOARDSTABLE
        (ID INT PRIMARY KEY     NOT NULL,
        DATAURL           TEXT    NOT NULL,
        );''')

    cur.execute("INSERT INTO COMPANY (ID,DATAURL) \
      VALUES (f{canvas_id}, {dataURL})")

    conn.commit()
    conn.close()

    return {}

def load_canvas(canvas_id):
    conn = psycopg2.connect(database = "testdb", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()

    cur.execute("SELECT id, dataurl")
    rows = cur.fetchall()

    dataURL = NULL
    for row in rows:
        if (row[0] == canvas_id):   # looking for board with correct id
            dataURL = row[1]        # image of that board is in dataURL

    return {dataURL}


