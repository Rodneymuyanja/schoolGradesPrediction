from EndPoints.apps import EndpointsConfig
#from EndPoints.models import Student, Subject, Marks
import os
import time
import csv
from datetime import datetime
import numpy as np
import pandas as pd
from EndPoints.serializers import PredictionSerializer

import pickle

def GetPrediction(file):
    date = datetime.today().strftime('%Y-%m-%d')
    subject = os.path.basename(str(file))
    counter = 0
    with open(file) as f:
        next(f)
        for line in f.readlines():
            #print(line)
            #creating a list
            parameters = line.split(",")
            #getting firstname and lastname
            firstname = parameters[0]
            lastname = parameters[1]
            #removing the name out of the list
            """
            both are zero because when you remove firstname at index 0,
            lastname becomes index zero, so we remove it too.
            """
            parameters.pop(0)
            parameters.pop(0)
            #print(parameters)

            v = np.asarray([parameters])
            v = v.astype(np.float64)
            #print(v)

            model = EndpointsConfig.model

            prediction = model.predict(v)
            print(prediction)
            
            data = {"student":firstname,"subject":subject, "prediction":int(prediction[0]),"dateGenerated":date}

            print("dataaa",data)
            serializer = PredictionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                counter = counter + 1

    print("A total of ",counter," predictions have been made")    

    #return prediction, datetime.today().strftime('%Y-%m-%d')