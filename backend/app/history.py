def updateHistory(questionID, studentID, answer, workingOutPhoto):
    timestamp = int(datetime.strptime(fTime, '%Y-%m-%d %I:%M:%S %p').strftime('%s'))
    
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

    attempt = 0
    if counter == 0:
        #This is first attempt
        attempt = 1
    elif counter > 0:
        attempt = newest_question[3] + 1    # incerementing attempt

    #Figure out result
    result = checkAnswer(answer)    #TODO: need to make checkAnswer Function

    #Figure out MasteredQ
    masteredQ = False
    if (successful_attempts >= 3):
        masteredQ = True
         
    #Figure out next attempt

    

    #Figure out approved