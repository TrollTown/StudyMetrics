# Spaced repetition ends after three times
    #Day: 1, 3, 6 after start date

#if MasteredQ == False and Attempt < 3 --> give question
import time
from app.dbtools import getHistoryByStudentID

def selectRevisionQ(studentID):
    studentQHistory = getHistoryByStudentID(studentID)  #array of Tuples

    #Tuples I'm interested in
        # index 3: attempts
        # index 4: masteredQ
    revision = [0] * 5

    counter = 0

    attempts = 0 
    for question in studentQHistory:
        attempts += 1
        questionID = question[0]
        masteredQ = question[3] # boolean
        nextAttempt = question[4] #datetime
        
        currentTime = time.time()

        if (counter >= 5):
            break
        if (masteredQ == False and attempts < 3 and currentTime > nextAttempt):
            revision[counter] = questionID
            counter += 1

    return revision
    #currently returning revision array with questionID

    

