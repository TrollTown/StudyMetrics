from app.dbtools import *
from app.history import *
from datetime import datetime
import time

def getQuestionDataByID(questionID):
	qData = getQuestionByID(questionID)
	return {
		'questionID': qData[0],
		'subjectID': qData[1],
		'moduleID' : qData[2]   ,
		'submoduleID' : qData[3],
		'questionText' : qData[4]  ,
		'questionType' : qData[5] ,
		'answer'  : qData[6] ,
		'photo'   : qData[7]  ,
		'difficulty' : qData[8],
		'authorID'  : qData[9],
		'starred'  : qData[10]
	}

def getSubjectDataByID(subjectID):
	data = getSubjectByID(subjectID)
	return {
		'subjectID': data[0],
		'subjectName':	data[1]
	}


def getModuleDataByID(moduleID):
	data = getModuleByID(moduleID)
	return {
		'moduleID': data[0],
		'subjectID': data[1],
		'moduleName': data[2]
	}


def getSubmoduleDataByID(submoduleID):
	data = getSubmoduleByID(submoduleID)
	return {
		'submoduleID': data[0],
		'moduleID': data[1],
		'submoduleName': data[2]
	}



def radarGraphForStudent(studentID,searchVal,searchMode):# or subject or module
	history = getHistoryByStudentID(studentID)
	groups = {}
	for qID,sID,fTime,masteredQ,nextAttempt,sAns,res,approved in history:
		if not approved:
			continue
		qData = getQuestionByID(qID)
		qDiff = qData[8]
		key = ''
		if searchMode == 'subject' and qData[1]==searchVal:
			key = getModuleNameByID(qData[2]) #if searhcing by subject, split on module
		elif searchMode == 'module'  and qData[2]==searchVal:
			key = getSubmoduleNameByID(qData[3]) #if searhcing by module, split on submodule
		else: 
			continue

		if key not in groups:
			groups[key] = []

		fTime = int(fTime.strftime('%s'))
		
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

def getUnapprovedQuestions(teacherID):
	history = []
	cIDs = getClassIDsByTeacherID(teacherID)
	sIDs = []
	for id in cIDs:
		sIDs += getStudentIDsByClassID(id)
	sIDs = list(set(sIDs))
	for id in sIDs:
		history += getHistoryByStudentID(id)
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
			lastTime[qID] = int(fTime.strftime('%s'))
	items = list(lastTime.items())
	items.sort(key=lambda x:x[1])
	return {
		'questionID': items[0][0]
	}

def getLevelProgress(studentID,level,levelID):
	# get total number of questions
	n = 0
	if level=='subject':
		n = len(getQuestionsBySubjectID(levelID))
	elif level=='module':
		n = len(getQuestionsByModuleID(levelID))
	elif level=='submodule':
		n = len(getQuestionsBySubmoduleID(levelID))

	if n == 0:
		return {
			'progress': 0
		}

	# get number of those questions that were attempted, and how many were answered right
	history = getHistoryByStudentID(studentID)[::-1]
	lastTime={}
	for qID,sID,fTime,masteredQ,nextAttempt,sAns,res,approved in history:
		qData = getQuestionByID(qID)
		if level=='subject' and levelID==qData[1]:
			if res:
				lastTime[qID] = 1
			elif qID in lastTime:
				del lastTime[qID]
	m = len(lastTime.keys())
	return {
		'progress': round(100*m/n)
	}

def getEntireLevelProgress(studentID,levelType,parentLevelID):
	ids = []
	if levelType=='subject':
		ids = getAllSubjectIDs()
	elif levelType=='module':
		ids = getModuleIDsBySubjectID(parentLevelID)
	elif levelType=='submodule':
		ids = getSubmoduleIDsByModuleID(parentLevelID)

	retVal = {}
	for id in ids:
		name = ''
		if levelType=='subject':
			name = getSubjectNameByID(id)
		elif levelType=='module':
			name = getModuleNameByID(id)
		elif levelType=='submodule':
			name = getSubmoduleNameByID(id)
		
		retVal.append({
			'id': id,
			'name': name,
			'progress': getLevelProgress(studentID,levelType,id)
		})

	return retVal

def approveAnswer(questionID,studentID,finish_time,result):
	entry = getHistoryEntry(questionID,studentID,finish_time)
	# new entry
	addHistory2Database(questionID, studentID, finish_time, entry[3], entry[4], entry[5], entry[6], result, True)
	return {
		'result':'success'
	}

# overall performance of class
# 
def getClassMembers(classID):
	ids = getStudentIDsByClassID(classID)
	retVal = []
	for id in ids:
		s = getUserByID(id)
		retVal.append({
			'id': id,
			'name': s[2],
		})
	return retVal


def getClassList(teacherID):
	ids = getClassIDsByTeacherID(teacherID)
	retVal = []
	for id in ids:
		c = getClassNamebyClassID(id)
		retVal.append({
			'id': id,
			'name': c[2],
		})
	return retVal

# def getSubjectListFromC

def getClassRadar(classID):
	c = getClassbyClassID(classID)
	sName = c[3]
	ids = getStudentIDsByClassID(classID)
	totals = {}
	n = len(ids)
	for id in ids:
		data = radarGraphForStudent(id, sName, 'subject')
		for k,v in data.items():
			totals[k] = totals.get(k,0) + v
	retVal = {}
	for k,v in totals.items():
		retVal[k] = round(v/n)
	return retVal

def getClassListByStudentID(studentID):
	cs = getClassIDsbyStudentID(studentID)
	retVal = []
	for c in cs:
		k = getClassbyClassID(c)
		retVal.append({
			'classID': c,
			'className': c[2]
		})
	return retVal


