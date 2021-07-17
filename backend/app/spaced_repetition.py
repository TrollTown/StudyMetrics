# Spaced repetition ends after three times
    #Day: 1, 3, 6 after start date

#if MasteredQ == False and Attempt < 3 --> give question
from datetime import datetime
import psycopg2

def selectRevisionQ(studentID):
    studentQHistory = getHistoryByStudentID(studentID)  #array of Tuples

    #Tuples I'm interested in
        # index 3: attempts
        # index 4: masteredQ
    revision = [0] * 5

    counter = 0
    for question in studentQHistory:
        questionID = question[0]
        attempts = question[3]  # integer
        masteredQ = question[4] # boolean
        nextAttempt = question[5] #datetime
        
        currentTime = int(datetime.strptime(fTime, '%Y-%m-%d %I:%M:%S %p').strftime('%s'))

        if (counter >= 5):
            break
        if (masteredQ == False and attempts < 3 and currentTime > nextAttempt):
            revision[counter] = questionID
            counter += 1

    return revision

def add2History(questionID, studentID):
    
    conn = psycopg2.connect(database = "testdb", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()

    cur.execute("INSERT INTO HISTORYTABLE (QuestionID,StudentID,Timestamp,Attempt,MasteredQ, NextAttempt, WorkingOutPhoto, Result, Approved) \
        VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

    conn.commit()
    print "Records created successfully";
    conn.close()
