from matplotlib import pyplot
import matplotlib.pyplot as plt
try:
    f=open('CEE_220_Scores.txt', 'r')
except IOError:
    print("could not open the file")

line=f.readline()#takes one line at one time
#line=line.rstrip()
headline=line.split('\t')
#print headline

(AS, LB, MT, FI)=[],[],[],[]
for i in range(1,len(headline)):
    if headline[i].find('Assignment')>=0:
        AS.append(i)
    elif headline[i].find('Lab')>=0:
        LB.append(i)
    elif headline[i].find('Midterm')>=0:
        MT.append(i)
    elif headline[i].find('Final')>=0:
        FI.append(i)
studentresult=[]
line=f.readline()
targetline=line.split('\t')

(AStarget, LBtarget, MTtarget, FItarget)=0,0,0,0
for i in AS:
    AStarget+=int(targetline[i])
for i in LB:
    LBtarget+=int(targetline[i])
for i in MT:
    MTtarget+=int(targetline[i])
for i in FI:
    FItarget+=int(targetline[i])

for line in f:
    l=line.split('\t')
    (ASsum, LBsum, MTsum, FIsum)=0,0,0,0
    
    for j in AS:
        try:
            ASsum+=float(l[j])
        except ValueError:
            print 'missing data or data error for column', j, 'of', l[0]
    for j in LB:
        try:
            LBsum+=float(l[j])
        except ValueError:
            print 'missing data or data error for column', j, 'of', l[0] 
    for j in MT:
        try:
            MTsum+=float(l[j])
        except ValueError:
            print 'missing data or data error for column', j, 'of', l[0]
    for j in FI:
        try:
            FIsum+=float(l[j])
        except ValueError:
            print 'missing data or data error for column', j, 'of', l[0]
    weightedscore=ASsum/AStarget*0.25+LBsum/LBtarget*0.05+MTsum/MTtarget*0.40+FIsum/FItarget*0.30
    grade=(weightedscore-0.2)/0.20
    if grade<0.7 :
        grade=0.0
    elif grade>4.0:
        grade=4.0
    grade=round(grade,1)
    result = dict(student=l[0], AssignmentSum=ASsum, labSum=LBsum, MidtermSum=MTsum, FinalSum=FIsum, Weightedscore=weightedscore, Grade=grade)
    studentresult.append(result)
f.close()
g=[]
for i in studentresult:
    g.append(i.get('Grade'))
    
n,bins, patches = plt.hist(g, 40, range=(0,4))
plt.xlabel('assigned numeric grade')
plt.ylabel('number of students')
plt.title('Grade distribution for CEE200')
plt.savefig('myreport.png')
plt.show()

     
