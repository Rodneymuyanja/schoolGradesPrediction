from EndPoints.models import Student, Subject, Grade, Tests, Teacher, Prediction, Marks 
from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['url','regNo', 'firstname','lastname', 'classS','age','phoneNumber','residence','dateAdded', 'email']

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['url', 'name', 'compulsory']

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ['url', 'firstname','lastname', 'email', 'subject', 'phoneNumber', 'age']

class TestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tests
        fields = ['url', 'name', 'dateAdded']

class MarksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marks
        fields = ['url', 'student', 'subject', 'test', 'grade', 'dateAdded','comment']

class PredictionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prediction
        fields = ['url','student','subject', 'prediction', 'confidenceLevel', 'dateGenerated']

class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = ['url','grade','comment']
