# from django.views.generic import ListView
# from django.shortcuts import render
#
# from .models import Student
#
#
# def students_list(request):
#     template = 'school/students_list.html'
#     context = {}
#
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     ordering = 'group'
#
#     return render(request, template, context)
from django.views.generic import ListView
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'school/students_list.html'
    context_object_name = 'students'
    ordering = ['group']