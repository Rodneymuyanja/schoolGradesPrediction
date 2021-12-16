"""BackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from EndPoints import views
from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register(r'Students', views.StudentViewSet)
router.register(r'Subjects', views.SubjectViewSet)
router.register(r'Teachers', views.TeacherViewSet)
router.register(r'Marks', views.MarksViewSet)
router.register(r'Tests', views.TestsViewSet)
router.register(r'Grades', views.GradeViewSet)
router.register(r'Predictions', views.PredictionViewSet)
router.register(r'file', views.FileUploadViewSet, basename='file')
#router.register(r'GetPrediction', views.call_model)



# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('prediction/', views.predictions),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
urlpatterns = [
    path('admin/', admin.site.urls),
]
"""