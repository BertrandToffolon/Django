from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from .models import Cursus,Student
from . import forms
from . import populate_Students3


# Create your views here.
def index(request):
  result_liste = Cursus.objects.order_by('name')
  #chargement du template
  template = loader.get_template('lycee/index.html')
  #contexte
  context = {
    'liste' : result_liste
  }

  return HttpResponse(template.render(context,request))

def detail(request, cursus_id):
  result_liste = Student.objects.filter(cursus=cursus_id)

  template = loader.get_template('lycee/cursus/detail.html')

  context = {
    'liste' : result_liste
  }
  return HttpResponse(template.render(context,request))

def call(request, cursus_id):
  result_liste = Student.objects.filter(cursus=cursus_id)

  template = loader.get_template('lycee/cursus/call.html')

  context = {
    'liste' : result_liste
  }
  return HttpResponse(template.render(context,request))

def particular_call(request):
  result_liste = Cursus.objects.order_by('name')
  #chargement du template
  template = loader.get_template('lycee/student/formcall.html')
  #contexte
  context = {
    'liste' : result_liste
  }

  return HttpResponse(template.render(context,request))

def student_detail(request, student_id):
  result_liste = Student.objects.filter(id=student_id)

  template = loader.get_template('lycee/student/detail.html')

  context = {
    'liste' : result_liste
  }
  return HttpResponse(template.render(context,request))
  
class StudentEditView(UpdateView):
  #le model au se refere cette view
  model = Student
  #le formulaire associé (dans form.py)
  #form_class = forms.StudentForm
  fields = {
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comment",
      "cursus",
    }
  #le nom du template
  template_name = "lycee/student/edit.html"
  def get_success_url(self):
    return reverse('index')
    #kwargs={'student_id': self.get_object().id}




class StudentCreateView(CreateView):

  #le model au se refere cette view
  model = Student
  #le formulaire associé (dans form.py)
  form_class = forms.StudentForm
  #le nom du template
  template_name = "lycee/student/create.html" 

  #if request.POST:
  #     form = UserForm(request.POST)
  #     if form.is_valid():
  #        first_name = form.cleaned_data['first_name']
  #        last_name = form.cleaned_data['last_name']
  #        birth_date = form.cleaned_data['birth_date']
  #        phone = form.cleaned_data['phone']
  #        email = form.cleaned_data['email']
  #        comment = form.cleaned_data['comment']
  #        cursus = form.cleaned_data['cursus']
  #cp1= Cursus.objects.get(name__contains = cursus)
  #cp1.student_set.create(
	#last_name = last_name,
	#first_name = first_name,
	#phone = phone,
	#email = email,
	#birth_date = birth_date,
	#comment = comment,
	#)