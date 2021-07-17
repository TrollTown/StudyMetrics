def getSubjectIDByName(subjectName):
    cur.execute('''
      select subjectID
      from Subjects
      where subjectID=%s
    ''',[subjectName])

def getModuleIDByName(moduleName):
    cur.execute('''
      select moduleID
      from Modules
      where moduleID=%s
    ''',[moduleName])

def getSubmoduleIDByName(submoduleName):
    cur.execute('''
      select submoduleID
      from Submodules
      where submoduleID=%s
    ''',[submoduleName])

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
