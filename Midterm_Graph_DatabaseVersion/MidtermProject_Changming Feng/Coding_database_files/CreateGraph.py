import sqlite3 as dbi
import sys

#global counters for unique ID for cityID, AirlineID, FlightID
CTID=0
ALID=0
FLID=0

def getCityID(db, name, State):
    cu=db.cursor()
    cmd="""SELECT ID FROM Cities 
           WHERE Name='{}' AND State='{}'"""
    cu.execute(cmd.format(name, State))
    cityID=cu.fetchone()
    return cityID

def createCityEntry(db,ID,name,State):
    c=getCityID(db, name, State)
    cu = db.cursor()
    sql_command = """INSERT INTO Cities (ID, Name, State)
                     VALUES ({}, '{}', '{}')"""
    if c==None :
        cu.execute(sql_command.format(ID,name,State))



def createAirportEntry(db,Name, CityID, lon, lati, x, y):
    cu = db.cursor()
    sql_command = """INSERT INTO Airports (Name, CityID, Long, Lati, X, Y)
                     VALUES ('{}', {}, {}, {}, {}, {})"""
    #print sql_command.format(ID,name,dob)
    cu.execute(sql_command.format(Name, CityID, lon, lati, x, y))

def getAirlineID(db, name):
    cu=db.cursor()
    cmd="""SELECT ID FROM Airlines 
           WHERE Name='{}'"""
    cu.execute(cmd.format(name))
    AirID=cu.fetchone()
    return AirID    

def createAirlineEntry(db,ID,name):
    a=getAirlineID(db, name)
    sql_command = """INSERT INTO Airlines (ID, Name)
                     VALUES ({}, '{}')"""
    cu = db.cursor()
    if a == None:
        cu.execute(sql_command.format(ID,name))
    
     

def createFlightEntry(db, ID, Number, OperatorID, FromAir, ToAir, DepartTime, ArrivalTime, TravelTime):
    cu=db.cursor()
    sql_command="""INSERT INTO Flights (ID, Number, OperatorID, FromAir, ToAir, DepartTime, ArrivalTime, TravelTime)
                     VALUES ({}, '{}', {}, '{}', '{}', {}, {}, {})"""
    cu.execute(sql_command.format(ID, Number, OperatorID, FromAir, ToAir, DepartTime, ArrivalTime, TravelTime))



filename="Airport Data.txt"
#connect to the database
try:
    db = dbi.connect('Graph.db')
    print 'success'
except:
    print 'failed'
    sys.exit()
# open the file    
try:
    f = open(filename,'r')
    print 'success'
except IOError:
    print 'failed when open Airport Data'
    sys.exit()
    

c=db.cursor()
head=f.readline().split('\t')

for line in f:
    line=line.split('\t')
    for i in range(3,len(line)):
            line[i] = float(line[i])
    CTID+=1
    createCityEntry(db, CTID, line[1], line[2])
    #find the cityID and store in cID
    sql_cmd="""SELECT ID From Cities
               WHERE Name= '{}' and State = '{}'"""
    c.execute(sql_cmd.format(line[1], line[2]))
    cID=c.fetchone()[0]
    createAirportEntry(db, line[0], cID, line[3], line[4], line[5], line[6])
f.close()

filename1="Flight Data.txt"
# open the file
try:
    g = open(filename1,'r')
    print 'success'
except IOError:
    print 'failed when open Flight Data'
    sys.exit()

head=g.readline().split('\t')
#print head



for line in g:
    line=line.split('\t')
    FLID+=1
    ALID+=1
    createAirlineEntry(db, ALID, line[1])
    #find the airlineID and store in oID
    sql_cmd="""SELECT ID From Airlines
               WHERE Name= '{}'"""
    c.execute(sql_cmd.format(line[1]))
    oID=c.fetchone()[0]
    #get the hour and minutes of departTime and arrivalTime and calculate the TravelTime
    deTime=line[4].split(':')
    arTime=line[5].split(':')
    deTime=int(deTime[0])*60+int(deTime[1])
    arTime=int(arTime[0])*60+int(arTime[1])
    TrvlTime=arTime-deTime
    createFlightEntry(db, FLID, line[0], oID, line[2], line[3], deTime, arTime,TrvlTime)

db.commit()
db.close()

            




