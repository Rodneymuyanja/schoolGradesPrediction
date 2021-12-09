from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from EndPoints.models import Student, Subject, Grade, Tests, Teacher, Prediction, Marks 
from EndPoints.serializers import StudentSerializer, SubjectSerializer, GradeSerializer
from EndPoints.serializers import TeacherSerializer, MarksSerializer, TestsSerializer, PredictionSerializer

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
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Prediction.objects.all().order_by('dateGenerated')
    serializer_class = PredictionSerializer
    permission_classes = []
