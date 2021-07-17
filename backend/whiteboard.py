import mysql.connector

def save_canvas(canvas_id, coord_array):
    #Do something with SQL
    INSERT INTO BoardsTable (BoardID, BoardCoord)
    VALUES (canvas_id, coord_array);
    return {}

def load_canvas(canvas_id):
    #Do something with SQL
    SELECT * FROM BoardsTable
    WHERE BoardID = canvas_id;

    return {}