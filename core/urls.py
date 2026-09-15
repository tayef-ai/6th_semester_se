from django.contrib import admin
from django.urls import path
from app.views import studentview, singlestudentview, allstudentview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:pk>/', singlestudentview),
    path('students/', allstudentview),
    path('createstudent/', studentview, name='createstudent')
]
