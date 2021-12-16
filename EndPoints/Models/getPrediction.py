"""from EndPoints.apps import EndpointsConfig
from EndPoints.models import Student, Subject, Marks"""
import os
import time
import csv
from datetime import datetime

def getPred(student, subject):
    sound = "woof"
    
    queryset = Student.objects.filter(firstname=student)
    print([p.id for p in queryset])
    
    studentId = [p.id for p in queryset]

    marksQueryset = Marks.objects.filter(student=studentId[0])
    print("marksQueryset", marksQueryset)

    mark = [m.grade for m in marksQueryset]
    print("mark...grade ",mark)
   
    # vectorize sound
    vector = EndpointsConfig.vectorizer.transform([sound])
    # predict based on vector
    prediction = EndpointsConfig.regressor.predict(vector)[0]

    return prediction, datetime.today().strftime('%Y-%m-%d')


def GetLatestFile(subject):
    """
    find folder/Subject
    in there look for the most recent file 
    return that file
    """
    path = 'marks/'+subject
    fileslist = []
    latestFile = None
    
    s = '2021-12-9 01:45:54'
    t = time.strptime(s, '%Y-%m-%d %H:%M:%S')
    lastestTime = time.strftime("%Y-%m-%d %H:%M:%S", t)
    

    for root, dirs, files in os.walk(path):

        for file in files:
            #if(file.endswith(".csv")):
                #print(os.path.join(root,file))
            fileslist.append(os.path.join(root,file))

    for file in fileslist:
        try:
            ti_m = os.path.getctime(file)
            m_ti = time.ctime(ti_m)
            
            """ # Using the timestamp string to create a 
            # time object/structure"""
            t_obj = time.strptime(m_ti)

            """# Transforming the time object to a timestamp 
            # of ISO 8601 format"""
            T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
            if T_stamp > lastestTime:
                lastestTime = T_stamp
                latestFile = file
        except FileNotFoundError as f:
            print(f)
            return f

    return latestFile


def FinalMarkPrediction(subject):
    lastestFile = GetLatestFile(subject)
    print(lastestFile)
    """
    try to check history.txt or write there
    """
    if lastestFile != None:
        ranBefore = False
        logs = open('marks/Logs.txt','r')
        for line in logs:
            print(line)
            if line.split('->')[0] == lastestFile:
                ranBefore = True
                print("been run before ",line)
                

        if ranBefore == False:
            print("*********never been run before**********")
            #do its predictions then log 
            logsAgain = open('marks/Logs.txt','a')
            logsAgain.write('\n'+lastestFile+'->'+str(datetime.now()))
    else:
        print("file doesn't exist")        

        #fileToread = open(lastestFile, "r")
        #for line in fileToread.readlines():
            #print(line)
        """
            for each get a prediction create a prediction object 
            then save it onto the prediction model
        """
"""
********keep in mind*********
-> a user will upload a file
-> then they'll request for a prediction for a particular student x
-> we wont run cronjobs here(thou that would be ideal)
-> instead the FinalMarkPrediction() function will run 
-> this will give us a prediction for all students currently in the most recent file they've uploaded
-> if we had a cronjob we'd schedule it and it does FinalMarkPrediction() at an opportune time
-> after FinalMarkPrediction() is run the user still needs a prediction for a particular student x
-> so we'll query the prediction model for that student and return 

********the problem**********
-> this procedure may repeat for each prediction request 
********the solution*********
-> keep a history file(logs.txt) of which .csv file was last processed
-> if we check and it's the same file that GetLatestFile is returning then 
-> we just go ahead and query the prediction model for a prediction
"""        


#FinalMarkPrediction('pool')
