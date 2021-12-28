import random
import csv
import pandas as pd
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

creamRange = [80,100]
topRange = [70,85]
mediocres = [50,70]
lasts = [0,50]

creamRangeList = []
topRangeList = []
mediocresList = []
lastsList = []

students = open("D:/4th year final semester/project/code/students.csv", "r")
studentsList = []
for line in students.readlines():
    studentsList.append(line.replace('"', '').replace('\n',''))

studentsList.pop(0)


data = pd.read_csv("D:/4th year final semester/project/Student Result Tracking and Projection System/studentmat.csv")

d = data.drop(['G1','G2','G3'], axis='columns')

d['Mjob'] = le.fit_transform(d['Mjob'])
d['Fjob'] = le.fit_transform(d['Fjob'])
d['paid'] = le.fit_transform(d['paid'])
d['activities'] = le.fit_transform(d['activities'])
d['internet'] = le.fit_transform(d['internet'])
d['romantic'] = le.fit_transform(d['romantic'])
d['sex'] = le.fit_transform(d['sex'])


age = list(d['age'])
#school = list(d['school'])
sex = list(d['sex'])
#address = list(d['address'])
#famsize = list(d['famsize'])
#Pstatus = list(d['Pstatus'])
#Medu = list(d['Medu'])
#Fedu = list(d['Fedu'])
Mjob = list(d['Mjob'])
Fjob = list(d['Fjob'])
#reason = list(d['reason'])
#guardian = list(d['guardian'])
traveltime = list(d['traveltime'])
studytime = list(d['studytime'])
failures = list(d['failures'])
#schoolsup = list(d['schoolsup'])
#famsup = list(d['famsup'])
paid = list(d['paid'])
activities = list(d['activities'])
#nursery = list(d['nursery'])
#higher = list(d['higher'])
internet = list(d['internet'])
romantic = list(d['romantic'])
#famrel = list(d['famrel'])
#freetime = list(d['freetime'])
goout = list(d['goout'])
#Dalc = list(d['Dalc'])
#Walc = list(d['Walc'])
#health = list(d['health'])
absences = list(d['absences'])

files = ["Biology.csv", "Mathematics.csv", "Physics.csv", "Chemistry.csv", "History.csv", "Geography.csv", "English.csv", "Commerce.csv", "Agriculture.csv", "CRE.csv"]



def HardTest(kind):
    if kind == "cream":
        for i in range(0, 20):
            creamRangeList.append(random.randint(creamRange[0],creamRange[1]))
        #return creamRangeList
    elif kind == "top":
        for i in range(0, 100):
            topRangeList.append(random.randint(topRange[0], topRange[1]))
        #return topRangeList
    elif kind == "mediocres":
        for i in range(0, 300):
            mediocresList.append(random.randint(mediocres[0], mediocres[1]))
        #return mediocresList
    elif kind == "lasts":
        for i in range(0, 280):
            lastsList.append(random.randint(lasts[0], lasts[1]))
    return creamRangeList, topRangeList, mediocresList, lastsList
               

def EasyTest(kind):
    if kind == "cream":
        for i in range(0, 200):
            creamRangeList.append(random.randint(creamRange[0],creamRange[1]))
        #return creamRangeList
    elif kind == "top":
        for i in range(0, 300):
            topRangeList.append(random.randint(topRange[0], topRange[1]))
        #return topRangeList
    elif kind == "mediocres":
        for i in range(0, 299):
            mediocresList.append(random.randint(mediocres[0], mediocres[1]))
        #return mediocresList
    elif kind == "lasts":
        for i in range(0, 1):
            lastsList.append(random.randint(lasts[0], lasts[1]))
    return creamRangeList, topRangeList, mediocresList, lastsList
               
def WeirdTest(kind):
    if kind == "cream":
        for i in range(0, 5):
            creamRangeList.append(random.randint(creamRange[0],creamRange[1]))
        #return creamRangeList
    elif kind == "top":
        for i in range(0, 400):
            topRangeList.append(random.randint(topRange[0], topRange[1]))
        #return topRangeList
    elif kind == "mediocres":
        for i in range(0, 393):
            mediocresList.append(random.randint(mediocres[0], mediocres[1]))
        #return mediocresList
    elif kind == "lasts":
        for i in range(0, 2):
            lastsList.append(random.randint(lasts[0], lasts[1]))
    return creamRangeList, topRangeList, mediocresList, lastsList
               
def ExtremelyHardTest(kind):
    if kind == "cream":
        for i in range(0, 1):
            creamRangeList.append(random.randint(creamRange[0],creamRange[1]))
        #return creamRangeList
    elif kind == "top":
        for i in range(0, 20):
            topRangeList.append(random.randint(topRange[0], topRange[1]))
        #return topRangeList
    elif kind == "mediocres":
        for i in range(0, 400):
            mediocresList.append(random.randint(mediocres[0], mediocres[1]))
        #return mediocresList
    elif kind == "lasts":
        for i in range(0, 279):
            lastsList.append(random.randint(lasts[0], lasts[1]))
    return creamRangeList, topRangeList, mediocresList, lastsList

def NormalTest(kind):
    if kind == "cream":
        for i in range(0, 50):
            creamRangeList.append(random.randint(creamRange[0],creamRange[1]))
        #return creamRangeList
    elif kind == "top":
        for i in range(0, 250):
            topRangeList.append(random.randint(topRange[0], topRange[1]))
        #return topRangeList
    elif kind == "mediocres":
        for i in range(0, 350):
            mediocresList.append(random.randint(mediocres[0], mediocres[1]))
        #return mediocresList
    elif kind == "lasts":
        for i in range(0, 50):
            lastsList.append(random.randint(lasts[0], lasts[1]))
    return creamRangeList, topRangeList, mediocresList, lastsList
               
ranges = ["cream", "top", "mediocres", "lasts"]




def testness():
    easyTests = []
    WeirdTests = []
    hardTests = []
    normalTests = []
    ExtremelyHardTests = []

    random.shuffle(tests)
    random.shuffle(tests)
    random.shuffle(tests)
    random.shuffle(tests)
    
    easyTests.append(tests[0])
    easyTests.append(tests[1])
    
    hardTests.append(tests[2])
    hardTests.append(tests[3])
   
    WeirdTests.append(tests[4])
    WeirdTests.append(tests[5])
    
    normalTests.append(tests[6])
    normalTests.append(tests[7])
    
    ExtremelyHardTests.append(tests[8])
    ExtremelyHardTests.append(tests[9])
    
    return easyTests, hardTests, normalTests, WeirdTests, ExtremelyHardTests



for fr in files:
    testOne = []
    testTwo = []
    testThree = []
    testFour = []
    testFive= []
    testSix = []
    testSeven = []
    testEight = []
    testNine = []
    testTen = []

    tests = [testOne, testTwo, testThree, testFour, testFive, testSix, testSeven, testEight, testNine, testTen]
    
    easyTests, hardTests, normalTests, WeirdTests, ExtremelyHardTests = testness()
    for t in tests:
        for i in ranges:
            if t in easyTests:
                a,b,c,d = EasyTest(i)
            elif t in hardTests:
                a,b,c,d = HardTest(i)
            elif t in normalTests:
                a,b,c,d = NormalTest(i)
            elif t in WeirdTests:
                a,b,c,d = WeirdTest(i)    
            elif t in ExtremelyHardTests:
                a,b,c,d = ExtremelyHardTest(i)       

        r = [a,b,c,d]
        
        for p in r:
            for u in p:
                t.append(u)

        creamRangeList = []
        topRangeList = []
        mediocresList = []
        lastsList = []



    #studytime,failures,absences,traveltime,age,paid,internet,romantic,sex,Mjob,Fjob,activities,goout



    print(fr)
    file =  open("D:/4th year final semester/project/Student Result Tracking and Projection System/subjects/"+fr, "w")

    zipped = zip(tuple(studentsList), tuple(testOne), tuple(testTwo), tuple(testThree), tuple(testFour), tuple(testFive), tuple(testSix), 
    tuple(testSeven), tuple(testEight), tuple(testNine),tuple(studytime),tuple(failures), tuple(absences),  tuple(traveltime), tuple(age), tuple(paid),
    tuple(internet), tuple(romantic), tuple(sex),tuple(Mjob), tuple(Fjob), tuple(activities), tuple(goout),
    )

    #print("students.....",studentsList)
    head = "firstname,lastname,one,two,three,four,five,six,seven,eight,nine,studytime,failures,absences,traveltime,age,paid,internet,romantic,sex,Mjob,Fjob,activities,goout"
    file.write(head+'\n')
    print("wrote head")
    for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w in zipped:
        string = str(a)+","+str(b)+","+str(c)+","+str(d)+","+str(e)+","+str(f)+","+str(g)+","+str(h)+","+str(i)+","+str(j)+","+str(k)+","+str(l)+","+str(m)+","+str(n)+","+str(o)+","+str(p)+","+str(q)+","+str(r)+","+str(s)+","+str(t)+","+str(u)+","+str(v)+","+str(w)
        #print(string)
        file.write(string+'\n')
    
    testOne = []
    testTwo = []
    testThree = []
    testFour = []
    testFive= []
    testSix = []
    testSeven = []
    testEight = []
    testNine = []
    testTen = []
       
            