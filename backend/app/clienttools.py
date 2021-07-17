from dbtools import *
from datetime import datetime
import time

def radarGraphForStudent(studentID,searchVal,searchMode):# or module or submodule
	history = getHistoryByStudentID(studentID)
	groups = {}
	for qID,sID,fTime,masteredQ,nextAttempt,sAns,res,approved in history:
		if not approved:
			continue
		qData = getQuestionByID(qID)
		qDiff = qData[8]
		key = ''
		if searchMode == 'subject' and qData[1]==searchVal:
			key = getSubjectNameByID(qData[2]) #if searhcing by subject, split on module
		elif searchMode == 'module'  and qData[2]==searchVal:
			key = getSubjectNameByID(qData[3]) #if searhcing by module, split on submodule
		if key not in groups:
			groups[key] = []

		fTime = int(datetime.strptime(fTime, '%Y-%m-%d %I:%M:%S %p').strftime('%s'))
		
		groups[key].append((res,qDiff,fTime))

	currTime = int(time.time())

	retVal = {}
	for key,data in groups.items():
		elo = 5
		for res,diff,fTime in data:
			days = (currTime-fTime)//(24*60*60) + 1
			# if they get it right
			if res:
				elo = min(10,elo + max(0.05,(diff-elo)/5) * max(1,7.0/days))
			else:
				elo = max(0,elo - max(0.05,(elo-diff)/8) * max(1,7.0/days))
				# if they get it wrong
			# print(elo,res,diff,days)
		retVal[key] = elo
	return retVal

def getUnapproved():
	history = getAllHistory()
	allQuestions = {}
	for qID,sID,fTime,masteredQ,nextAttempt,sAns,res,approved in history:
		if (qID,sID,fTime) in allQuestions and approved:
			del allQuestions[(qID,sID,fTime)]
		elif not approved:
			allQuestions[(qID,sID,fTime)] = [qID,sID,fTime,sAns]
		
	retVal = [] 
	for qID,sID,fTime,sAns in allQuestions.values():
		retVal.append({
			'questionID': qID,
			'studentID': sID,
			'finish_time': fTime,
			'student_answer':	sAns
		})
	return retval
	
	


