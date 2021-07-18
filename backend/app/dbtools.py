import psycopg2
import os
from app import flask_app

def getUserByEmail(email):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		SELECT *
		FROM users
		WHERE email=%s
	''',[email])
	return cur.fetchall()

def insertUserIntoDatabase(name, email, pwdHash, isTeacher):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute("""
		INSERT INTO Users
		VALUES (DEFAULT,%s, %s, %s, %s)
	""",[email, name, pwdHash, isTeacher])
	conn.commit()

def getSubjectIDByName(subjectName):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select subjectID
		from Subjects
		where subjectName=%s
	''',[subjectName])
	return cur.fetchall()[0]

def getSubjectNameByID(subjectID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select subjectName
		from Subjects
		where subjectID=%s
	''',[subjectID])
	return cur.fetchall()[0]

def getModuleIDByName(moduleName):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select moduleID
		from Modules
		where moduleName=%s
	''',[moduleName])
	return cur.fetchall()[0]

def getModuleNameByID(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select moduleName
		from Modules
		where moduleID=%s
	''',[moduleID])
	return cur.fetchall()[0]

def getSubmoduleIDByName(submoduleName):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select submoduleID
		from Submodules
		where submoduleName=%s
	''',[submoduleName])
	return cur.fetchall()[0]

def getSubmoduleNameByID(submoduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select submoduleName
		from Submodules
		where submoduleID=%s
	''',[submoduleID])
	return cur.fetchall()[0]

def getQuestionByID(questionID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where questionID=%s
	''',[questionID])
	return cur.fetchall()[0]

def getSubjectByID(subjectID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Subjects
		where subjectID=%s
	''',[subjectID])
	return cur.fetchall()[0]

def getModuleByID(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Modules
		where moduleID=%s
	''',[moduleID])
	return cur.fetchall()[0]

def getSubmoduleByID(submoduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Submodules
		where submoduleID=%s
	''',[submoduleID])
	return cur.fetchall()[0]

def getModuleByID(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Modules
		where moduleID=%s
	''',[moduleID])
	return cur.fetchall()[0]

def getSubmoduleByID(submoduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Submodules
		where submoduleID=%s
	''',[submoduleID])
	return cur.fetchall()[0]


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

def getQuestionsBySubjectID(subjectID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where subjectID=%s
	''',[subjectID])
	return cur.fetchall()
	
def getQuestionsByModuleID(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where moduleID=%s
	''',[moduleID])
	return cur.fetchall()

def getQuestionsBySubmoduleID(submoduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where submoduleID=%s
	''',[submoduleID])
	return cur.fetchall()

def getAllHistory():
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select * from History
	''')
	return cur.fetchall()

def uploadQuestion(subjectID,moduleID,submoduleID,questionText,questionType,answer,photo,difficulty,authorID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		insert into Questions
		values (%s,%s,%s,%s,%s,%s,%s,%s,%s)
	''',[subjectID,moduleID,submoduleID,questionText,questionType,answer,photo,difficulty,authorID])
	# return cur.fetchall()

def getModuleIDsBySubjectID(subjectID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select moduleID from Modules
		where subjectID=%s
	''',[subjectID])
	return cur.fetchall()

def getSubmoduleIDsByModuleID(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select submoduleID from Submodules
		where moduleID=%s
	''',[moduleID])
	return cur.fetchall()

def getAllSubjectIDs():
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select subjectIDs from Subjects
	''')
	return cur.fetchall()

def getHistoryEntry(questionID,studentID,finish_time):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select * from History
		where questionID=%s, studentID=%s, finish_time=%s
	''',[questionID,studentID,finish_time])
	return cur.fetchall()[0]

def getStudentIDsByClassID(classID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select studentID from Classes
		where classID=%s
	''',[classID])
	return cur.fetchall()

def getUserByID(userID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select * from Users
		where id=%s
	''',[userID])
	return cur.fetchall()[0]

def getClassIDsByTeacherID(teacherID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select classID from Teaches
		where teacherID=%s
	''',[teacherID])
	return cur.fetchall()

def getClassbyClassID(classID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select * from Teaches
		where classID=%s
	''',[classID])
	return cur.fetchall()[0]

def getClassIDsbyStudentID(studentID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select classID from Classes
		where studentID=%s
	''',[studentID])
	return cur.fetchall()