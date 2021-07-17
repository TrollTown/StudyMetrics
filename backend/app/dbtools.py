import psycopg2
import os

def getUserByEmail(email):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		SELECT *
		FROM users
		WHERE email=%s
	''',[email])
	return cur.fetchall()

def insertUserIntoDatabase(name, email, pwdHash, userType):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute("""
		INSERT INTO Users VALUES (DEFAULT, %s, %s, %s, %s)
	""",[email, name, pwdHash, userType])

def getSubjectIDByName(subjectName):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select subjectID
		from Subjects
		where subjectName=%s
	''',[subjectName])
	return cur.fetchall()

def getSubjectNameByID(subjectID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select subjectName
		from Subjects
		where subjectID=%s
	''',[subjectID])
	return cur.fetchall()

def getModuleIDByName(moduleName):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select moduleID
		from Modules
		where moduleName=%s
	''',[moduleName])
	return cur.fetchall()

def getModuleNameByID(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select moduleName
		from Modules
		where moduleID=%s
	''',[moduleID])
	return cur.fetchall()

def getSubmoduleIDByName(submoduleName):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select submoduleID
		from Submodules
		where submoduleName=%s
	''',[submoduleName])
	return cur.fetchall()

def getSubmoduleNameByID(submoduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select submoduleName
		from Submodules
		where submoduleID=%s
	''',[submoduleID])
	return cur.fetchall()

def getQuestionByID(questionID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where questionID=%s
	''',[questionID])
	return cur.fetchall()

def getHistoryByStudentID(studentID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from History
		where studentID=%s
		order by finish_time
	''',[studentID])
	return cur.fetchall()

def getQuestionsBySubject(subjectID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where subjectID=%s
	''',[subjectID])
	return cur.fetchall()
	
def getQuestionsByModule(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where moduleID=%s
	''',[moduleID])
	return cur.fetchall()

def getQuestionsBySubmodule(submoduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where submoduleID=%s
	''',[submoduleID])
	return cur.fetchall()

def addHistory(qID,sID,fTime,attempt, masteredQ, nextAttempt, answer, res,approved):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		insert into History
		values (%s,%s,%s,%s,%s,%s,%s,%s)
	''',[qID,sID,fTime,attempt, masteredQ, nextAttempt, answer, res,approved])
	return cur.fetchall()

def addUser(email,name,passwd,isTeacher):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		insert into Users (email, name, passwd, isTeacher)
		values (%s,%s,%s,%s,%s,%s)
	''',[email,name,passwd,isTeacher])
	return cur.fetchall()

def getAllHistory():
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select * from History
	''')
	return cur.fetchall()