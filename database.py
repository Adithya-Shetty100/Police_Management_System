import mysql.connector
from datetime import time, datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="police"
)
c = mydb.cursor()

def trigger():
    #c.execute('CREATE TRIGGER my_trigger BEFORE INSERT ON Officer FOR EACH ROW BEGIN -- generate a new caseid SELECT COALESCE(MAX(OfficerId), 0) + 1 INTO NEW.OfficerId FROM Officer END;')
    c.execute('CREATE TRIGGER CaseId'
              'BEFORE INSERT ON Cases'
              'FOR EACH ROW'
              'SET NEW.CaseId = (SELECT MAX(CaseId) + 1 FROM Cases);')

    c.execute('CREATE TRIGGER CriminalId'
              'BEFORE INSERT ON Criminal'
              'FOR EACH ROW'
              'SET NEW.CriminalId = (SELECT MAX(CriminalId) + 1 FROM Criminal);')

    c.execute('CREATE TRIGGER ComplaintId'
              'BEFORE INSERT ON Complaint'
              'FOR EACH ROW'
              'SET NEW.ComplaintId = (SELECT MAX(ComplaintId) + 1 FROM Complaint);')

    c.execute('CREATE TRIGGER ComplainantId'
              'BEFORE INSERT ON Complainant'
              'FOR EACH ROW'
              'SET NEW.ComplainantId = (SELECT MAX(ComplainantId) + 1 FROM Complainant);')


def stored_func():
    c.execute('DELIMITER $$')
    c.execute('CREATE FUNCTION date_difference (input_date DATE) '
              'RETURNS INT '
              'BEGIN'
              'DECLARE result INT;'
              'SET result = DATEDIFF(CURDATE(), input_date);'
              'RETURN result;'
              'END; $$')
    c.execute('DELIMITER ;')

def create_tables():
    c.execute('CREATE TABLE IF NOT EXISTS OFFICER(OfficerId VARCHAR(20) NOT NULL, FirstName TEXT, LastName TEXT, Ranking TEXT, Department TEXT, Phone TEXT, Address TEXT, BloodGrp TEXT, PRIMARY KEY(OfficerId))'
              'CREATE TABLE IF NOT EXISTS CASES(CaseId VARCHAR(20) NOT NULL, Name TEXT, DOC DATE, Location TEXT, CRIME TEXT, OfficerId VARCHAR(20), PRIMARY KEY(CaseId), FOREIGN KEY(OfficerId) REFERENCES OFFICER(OfficerId))'
              'CREATE TABLE IF NOT EXISTS COMPLAINT(ComplaintId VARCHAR(20) NOT NULL, Type TEXT, Complainant TEXT, DOC DATE, Solved TEXT, CaseId VARCHAR(20), OfficerId VARCHAR(20),PRIMARY KEY(ComplaintId), FOREIGN KEY(CaseId) REFERENCES CASES(CaseId), FOREIGN KEY(OfficerId) REFERENCES OFFICER(OfficerId))'
              'CREATE TABLE IF NOT EXISTS COMPLAINANT(ComplainantId VARCHAR(20) NOT NULL, Name TEXT, Phone TEXT, Address TEXT, ComplaintId VARCHAR(20), RelationToVictim TEXT,PRIMARY KEY(ComplainantId), FOREIGN KEY(ComplaintId) REFERENCES COMPLAINT(ComplaintId))'
              'CREATE TABLE IF NOT EXISTS CRIMINAL(CriminalId VARCHAR(20) NOT NULL, Name TEXT, JailTerm TEXT, CaseId VARCHAR(20),PRIMARY KEY(CriminalId), FOREIGN KEY(CaseId) REFERENCES CASES(CaseId))'
              'CREATE TABLE IF NOT EXISTS ARREST(ArrestId VARCHAR(20) NOT NULL, DOC DATE, Location TEXT, CellNo TEXT, OfficerId VARCHAR(20), CriminalId VARCHAR(20), PRIMARY KEY(ArrestId), FOREIGN KEY(OfficerId) REFERENCES OFFICER(OfficerId), FOREIGN KEY(CriminalId) REFERENCES CRIMINAL(CriminalId))')


# add
def add_data_officer(Id, FirstName, LastName, Ranking, Department, Phone, Address, BloodGrp):
    c.execute('INSERT INTO OFFICER(OfficerId, FirstName, LastName, Ranking, Department, Phone, Address, BloodGrp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (Id, FirstName, LastName, Ranking, Department, Phone, Address, BloodGrp))
    mydb.commit()

def add_data_cases(Name, DOC, Location, CRIME, OfficerId):
    c.execute('INSERT INTO CASES(Name, DOC, Location, CRIME, OfficerId) VALUES (%s,%s,%s,%s,%s)', (Name, DOC, Location, CRIME, OfficerId))
    mydb.commit()

def add_data_complaint( Type, Complainant , DOC, Solved, CaseId, OfficerId):
    c.execute('INSERT INTO COMPLAINT(Type, Complainant , DOC, Solved, CaseId, OfficerId) VALUES (%s,%s,%s,%s,%s,%s)', (Type, Complainant, DOC, Solved, CaseId, OfficerId))
    mydb.commit()

def add_data_complainant( Name, Phone, Address, ComplaintId, RelationToVictim):
    c.execute('INSERT INTO COMPLAINANT(Name, Phone, Address, ComplaintId, RelationToVictim) VALUES (%s,%s,%s,%s,%s)', (Name, Phone, Address, ComplaintId, RelationToVictim))
    mydb.commit()

def add_data_arrest(ArrestId, DOC, Location, CellNo, OfficerId, CriminalId):
    c.execute('INSERT INTO ARREST(ArrestId, DOC, Location, CellNo, OfficerId, CriminalId) VALUES (%s,%s,%s,%s,%s,%s)', (ArrestId, DOC, Location, CellNo, OfficerId, CriminalId))
    mydb.commit()

def add_data_criminal(Name, JailTerm, CaseId):
    c.execute('INSERT INTO CRIMINAL(Name, JailTerm, CaseId) VALUES (%s,%s,%s)', (Name, JailTerm, CaseId))
    mydb.commit()


#view
def view_data_officer():
    c.execute('SELECT * FROM OFFICER')
    data = c.fetchall()
    return data

def view_data_cases():
    c.execute('SELECT * FROM CASES')
    data = c.fetchall()
    return data

def view_data_complaint():
    c.execute('SELECT * FROM COMPLAINT')
    data = c.fetchall()
    return data

def view_data_complainant():
    c.execute('SELECT * FROM COMPLAINANT')
    data = c.fetchall()
    return data

def view_data_arrest():
    c.execute('SELECT * FROM ARREST')
    data = c.fetchall()
    return data

def view_data_criminal():
    c.execute('SELECT * FROM CRIMINAL')
    data = c.fetchall()
    return data

#update
#officer details
def get_officer(OfficerId):
    c.execute('SELECT * FROM OFFICER WHERE OfficerID="{}"'.format(OfficerId))
    data = c.fetchall()
    return data

def edit_officer_data(new_ranking, new_department, new_phone, new_address,OfficerId):
    c.execute("UPDATE Officer SET Ranking=%s, Department=%s, Phone=%s, Address=%s WHERE OfficerId=%s  ", (new_ranking, new_department, new_phone, new_address,OfficerId))
    mydb.commit()

#delete
#case
def view_only_CaseID():
    c.execute('SELECT CaseID FROM CASES')
    data = c.fetchall()
    return data

def delete_data(selected_case):
    c.execute('DELETE FROM CASES WHERE CaseId={}'.format(selected_case))
    mydb.commit()
