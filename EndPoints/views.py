from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.viewsets import ViewSet
from rest_framework import permissions
from EndPoints.models import Student, Subject, Grade, Tests, Teacher, Prediction, Marks
from EndPoints.serializers import StudentSerializer, SubjectSerializer, GradeSerializer, FileSerializer
from EndPoints.serializers import TeacherSerializer, MarksSerializer, TestsSerializer, PredictionSerializer
from .apps import EndpointsConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Prediction
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, FileUploadParser
from EndPoints.Models.getPrediction import GetPrediction
from rest_framework import status
import os

marksPath = 'marks/'
# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('dateAdded')
    serializer_class = StudentSerializer
    permission_classes = []

class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = []

class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = []

class MarksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Marks.objects.all().order_by('dateAdded')
    serializer_class =  MarksSerializer
    permission_classes = []

class TestsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tests.objects.all().order_by('dateAdded')
    serializer_class = TestsSerializer
    permission_classes = []

class GradeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = []

class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all().order_by('dateGenerated')
    serializer_class = PredictionSerializer
    permission_classes = []


@csrf_exempt
def predictions(request):
 
    if request.method == 'GET':
        predictions = Prediction.objects.all()
        serializer = PredictionSerializer(predictions, many=True)
        return JsonResponse(serializer.data, safe=False)

    #remove POST from here so that this thing only does a GET
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        prediction, date = getPred(data['student'], data['subject'])
        data.update({"prediction":prediction,"dateGenerated":date})
        print(data)
        serializer = PredictionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class FileUploadViewSet(viewsets.ViewSet):
    
    def create(self, request):
        serializer_class = FileSerializer(data=request.data)
        if  not serializer_class.is_valid():
            print("errrrrrrrrrrrorrrrrrr")
            return Response(serializer_class.errors ,status=status.HTTP_400_BAD_REQUEST)
        else:
            handle_uploaded_file(request.FILES['file'])
            #GetPrediction(file)
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)

def addSubjectFolder(subject):
        try:
            directory = os.path.join(marksPath,subject) 
            os.mkdir(directory)
            return directory
        except FileExistsError as fileExists:
            print (fileExists)
            return subject #as directory

def handle_uploaded_file(f):
    subject = f.name.split('-')[0]
    directory = addSubjectFolder(subject)
    path = marksPath+subject+'/'+f.name
    with open(marksPath+subject+'/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    GetPrediction(path)
#def GetPrediction(f):

