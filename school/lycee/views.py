from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from .models import Cursus,Student,Presence
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

class Call(CreateView):
  model = Presence

  form_class = forms.PresenceForm

  template_name = "lycee/cursus/call.html"

class StudentEditView(UpdateView):
  #le model au se refere cette view
  model = Student
  #le formulaire associé (dans form.py)
  form_class = forms.StudentForm
  #le nom du template
  template_name = "lycee/student/edit.html"
  
  def get_success_url(self):
    return reverse('student_detail', args=(self.object.id,))

class StudentCreateView(CreateView):

  #le model au se refere cette view
  model = Student
  #le formulaire associé (dans form.py)
  form_class = forms.StudentForm
  #le nom du template
  template_name = "lycee/student/create.html" 
  
  def get_success_url(self):
    return reverse('student_detail', args=(self.object.id,))

class ParticularCallCreateView(CreateView):
  #le model au se refere cette view
  model = Presence
  #le formulaire associé (dans form.py)
  form_class = forms.PresenceForm
  #le nom du template
  template_name = "lycee/presence/create.html" 
  
  def get_success_url(self):
    return reverse('index')




  