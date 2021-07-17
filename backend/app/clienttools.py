from app.dbtools import getSubmoduleIDsByModuleID
from app.dbtools import *
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

def getUnapprovedQuestions():
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
	return retVal
	
def getSubmodulesByModuleID(moduleID):
	submoduleIDs = getSubmoduleIDsByModuleID(moduleID)
	retVal = []
	for sID in submoduleIDs:
		submodule = getSubmoduleByID(sID)
		retVal.append({
			'submoduleID': submodule[1],
			'submoduleName': submodule[2]
		})
	return retVal

def getNextQuestionID(studentID,submoduleID):
	history = getHistoryByStudentID(studentID)[::-1]
	lastTime = {}
	for qID,sID,fTime,masteredQ,nextAttempt,sAns,res,approved in history:
		if sID == submoduleID:
			lastTime[qID] = int(datetime.strptime(fTime, '%Y-%m-%d %I:%M:%S %p').strftime('%s'))
	items = list(lastTime.items())
	items.sort(key=lambda x:x[1])
	return items[0][0]

def getLevelProgress(studentID,level,levelID):
	# get total number of questions
	if level=='subject':
		n = len(getQuestionsBySubjectID(levelID))
	elif level=='module':
		n = len(getQuestionsBySubjectID(levelID))

	# get number of those questions that were attempted, and how many were answered right
	history = getHistoryByStudentID(studentID)[::-1]