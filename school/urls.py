# from django.urls import path
#
# from school.views import students_list
#
# urlpatterns = [
#     path('', students_list, name='students'),
# ]
from django.urls import path
from .views import StudentListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='students'),
]