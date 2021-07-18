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
	data = cur.fetchall()
	conn.close()
	return data

def insertUserIntoDatabase(name, email, pwdHash, isTeacher):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute("""
		INSERT INTO Users
		VALUES (DEFAULT,%s, %s, %s, %s)
	""",[email, name, pwdHash, isTeacher])
	conn.commit()
	conn.close()

def getSubjectIDByName(subjectName):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select subjectID
		from Subjects
		where subjectName=%s
	''',[subjectName])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getSubjectNameByID(subjectID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select subjectName
		from Subjects
		where subjectID=%s
	''',[subjectID])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getModuleIDByName(moduleName):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select moduleID
		from Modules
		where moduleName=%s
	''',[moduleName])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getModuleNameByID(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select moduleName
		from Modules
		where moduleID=%s
	''',[moduleID])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getSubmoduleIDByName(submoduleName):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select submoduleID
		from Submodules
		where submoduleName=%s
	''',[submoduleName])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getSubmoduleNameByID(submoduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select submoduleName
		from Submodules
		where submoduleID=%s
	''',[submoduleID])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getQuestionByID(questionID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where questionID=%s
	''',[questionID])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getSubjectByID(subjectID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Subjects
		where subjectID=%s
	''',[subjectID])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getModuleByID(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Modules
		where moduleID=%s
	''',[moduleID])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getSubmoduleByID(submoduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Submodules
		where submoduleID=%s
	''',[submoduleID])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getModuleByID(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Modules
		where moduleID=%s
	''',[moduleID])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getSubmoduleByID(submoduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Submodules
		where submoduleID=%s
	''',[submoduleID])
	data = cur.fetchall()[0]
	conn.close()
	return data


def getHistoryByStudentID(studentID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from History
		where studentID=%s
		order by finish_time
	''',[studentID])
	data = cur.fetchall()
	conn.close()
	return data

def getQuestionsBySubjectID(subjectID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where subjectID=%s
	''',[subjectID])
	data = cur.fetchall()
	conn.close()
	return data
	
def getQuestionsByModuleID(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where moduleID=%s
	''',[moduleID])
	data = cur.fetchall()
	conn.close()
	return data

def getQuestionsBySubmoduleID(submoduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select *
		from Questions
		where submoduleID=%s
	''',[submoduleID])
	data = cur.fetchall()
	conn.close()
	return data

def getAllHistory():
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select * from History
	''')
	data = cur.fetchall()
	conn.close()
	return data

def uploadQuestion(subjectID,moduleID,submoduleID,questionText,questionType,answer,photo,difficulty,authorID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		insert into Questions
		values (%s,%s,%s,%s,%s,%s,%s,%s,%s)
	''',[subjectID,moduleID,submoduleID,questionText,questionType,answer,photo,difficulty,authorID])
	conn.close()

def getModuleIDsBySubjectID(subjectID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select moduleID from Modules
		where subjectID=%s
	''',[subjectID])
	data = cur.fetchall()
	conn.close()
	return data

def getSubmoduleIDsByModuleID(moduleID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select submoduleID from Submodules
		where moduleID=%s
	''',[moduleID])
	data = cur.fetchall()
	conn.close()
	return data

def getAllSubjectIDs():
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select subjectIDs from Subjects
	''')
	data = cur.fetchall()
	conn.close()
	return data

def getHistoryEntry(questionID,studentID,finish_time):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select * from History
		where questionID=%s, studentID=%s, finish_time=%s
	''',[questionID,studentID,finish_time])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getStudentIDsByClassID(classID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select studentID from Classes
		where classID=%s
	''',[classID])
	data = cur.fetchall()
	conn.close()
	return data

def getUserByID(userID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select * from Users
		where id=%s
	''',[userID])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getClassIDsByTeacherID(teacherID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select classID from Teaches
		where teacherID=%s
	''',[teacherID])
	data = cur.fetchall()
	conn.close()
	return data

def getClassbyClassID(classID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select * from Teaches
		where classID=%s
	''',[classID])
	data = cur.fetchall()[0]
	conn.close()
	return data

def getClassIDsbyStudentID(studentID):
	conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
	cur = conn.cursor()
	cur.execute('''
		select classID from Classes
		where studentID=%s
	''',[studentID])
	data = cur.fetchall()
	conn.close()
	return data

def addHistory2Database(questionID, studentID, finish_time, masteredQ, nextAttempt, student_answer , result, approved):
    # TODO: Duno what to do in line 83
    conn = psycopg2.connect(database="hackathon_db", user = "hackathon_db_user", password = os.environ.get("PGPASSWORD"))
    cur = conn.cursor()

    cur.execute("INSERT INTO HISTORY (questionID, studentID, finish_time, masteredQ, nextAttempt, student_answer , result, approved) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [questionID, studentID, finish_time, masteredQ, nextAttempt, student_answer, result, approved])
    conn.commit()
    conn.close()