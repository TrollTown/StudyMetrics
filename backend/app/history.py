"""
[P] QuestionID
[P] StudentID
[X] finish_time 
[X] Attempt
[X] MasteredQ
[X] NextAttempt
[P] WorkingOutPhoto
[O] Result
[X] Approved
"""


import time
def updateHistory(questionID, studentID, answer, workingOutPhoto):
    finish_time = int(datetime.strptime(fTime, '%Y-%m-%d %I:%M:%S %p').strftime('%s'))

    studentHistory = getHistoryByStudentID(studentID)

    #Need to find most recent history 
    newest_question = NULL
    successful_attempts = 0
    counter = 0
    for question in studentHistory:
        if (question[0] == questionID):
            newest_question = question
            if (question[7]):   #if result is true
                successful_attempts += 1
            counter += 1
    ########    Finding values for fields   ########

    attempt = 0
    if counter == 0:
        #This is first attempt
        attempt = 1
    elif counter > 0:
        attempt = newest_question[3] + 1    # incerementing attempt

    # default to false
    #Figure out result
    result = False 
    result = checkAnswer(answer)    #TODO: need to make checkAnswer Function

    #Figure out MasteredQ
    masteredQ = False
    if (successful_attempts >= 3):
        masteredQ = True

    #Figure out next attempt for revision
    nextAttempt = NULL
    if (attempt == 1):
        # next attempt should be 1 day from last attempt date
        nextAttempt = datetime.now() + datetime.timedelta(days=1)
    if (attempt == 2):
        # next attempt should be 3 days from last atttempt date
        nextAttempt = datetime.now() + datetime.timedelta(days=3)
    if (attempt == 3):
        #next attempt should be 10 days from last attempt date
        nextAttempt = datetime.now() + datetime.timedelta(days=10)

        
    #Figure out approved
    #default true for mc or numeric
    approved = False
    result = False

    questionInfo = getQuestionByID(questionID)
    questionType = questionInfo(5)
    questionSoln = questionInfo(6)
    #Note: if approved and result are false, then that means it was whiteboard input and hasn't been checked yet
    if (questionType != 'whiteboard'):
        # Check answer against database
        approved = True
        if (answer == questionSoln):
            result == True
