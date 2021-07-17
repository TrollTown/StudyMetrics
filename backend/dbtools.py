def getSubjectIDByName(subjectName):
	cur.execute('''
		select subjectID
		from Subjects
		where subjectName=%s
	''',[subjectName])

def getSubjectNameByID(subjectID):
	cur.execute('''
		select subjectName
		from Subjects
		where subjectID=%s
	''',[subjectID])

def getModuleIDByName(moduleName):
	cur.execute('''
		select moduleID
		from Modules
		where moduleName=%s
	''',[moduleName])

def getModuleNameByID(moduleID):
	cur.execute('''
		select moduleName
		from Modules
		where moduleID=%s
	''',[moduleID])

def getSubmoduleIDByName(submoduleName):
	cur.execute('''
		select submoduleID
		from Submodules
		where submoduleName=%s
	''',[submoduleName])

def getSubmoduleNameByID(submoduleID):
	cur.execute('''
		select submoduleName
		from Submodules
		where submoduleID=%s
	''',[submoduleID])

def getQuestionByID(questionID):
	cur.execute('''
		select *
		from Questions
		where questionID=%s
	''',[questionID])

def getHistoryByStudentID(studentID):
	cur.execute('''
		select *
		from History
		where studentID=%s
		order by finish_time
	''',[studentID])

def getQuestionsBySubject(subjectID):
	cur.execute('''
		select *
		from Questions
		where subjectID=%s
	''',[subjectID])
	
def getQuestionsByModule(moduleID):
	cur.execute('''
		select *
		from Questions
		where moduleID=%s
	''',[moduleID])

def getQuestionsBySubmodule(submoduleID):
	cur.execute('''
		select *
		from Questions
		where submoduleID=%s
	''',[submoduleID])

def addHistory(qID,sID,fTime,ans,res,approved):
	cur.execute('''
		insert into History
		values (%s,%s,%s,%s,%s,%s)
	''',[qID,sID,fTime,ans,res,approved])

def addUser(email,name,passwd,isTeacher):
	cur.execute('''
		insert into History (email, name, passwd, isTeacher)
		values (%s,%s,%s,%s,%s,%s)
	''',[email,name,passwd,isTeacher])
