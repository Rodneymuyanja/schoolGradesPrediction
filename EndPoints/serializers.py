from EndPoints.models import Student, Subject, Grade, Tests, Teacher, Prediction, Marks
from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField
from .apps import EndpointsConfig

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

#class PredictionSerializer(serializers.HyperlinkedModelSerializer):
class PredictionSerializer(serializers.Serializer):

    class Meta:
        model = Prediction
        fields = ['url','student','subject','prediction','dateGenerated']
    
    def predict(sub, stu) -> serializers.IntegerField:
        s = "woof"
        #subject.objects.get()
        vector = EndpointsConfig.vectorizer.transform([s])
        
        prediction = EndpointsConfig.regressor.predict(vector)[0]
        return prediction
    
    student = serializers.CharField(required=False, allow_blank=True, max_length=100)
    subject = serializers.CharField(required=False, allow_blank=True, max_length=100)
    prediction = serializers.IntegerField()
    dateGenerated = serializers.DateField()

    
    def create(self, validated_data):
        return Prediction.objects.create(**validated_data)




class FileSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)


class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = ['url','grade','comment']


