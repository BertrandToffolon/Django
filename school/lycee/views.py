from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from .models import Cursus,Student,Presence,Call,Creneaux
from . import forms
from . import populate_Students3
import logging
from datetime import datetime



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
    'liste' : result_liste,
    'cursus' : Cursus.objects.get(id=cursus_id)
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
    'liste' : result_liste,
    'absence' : len(Presence.objects.filter(student=student_id))
  }
  return HttpResponse(template.render(context,request))

def callCreateView(request, cursus_id):
  student_liste = Student.objects.filter(cursus=cursus_id)
  cursus_liste = Cursus.objects.filter(id=cursus_id)
  creneaux_liste = Creneaux.objects.all().order_by('name')
  template = loader.get_template('lycee/cursus/call.html')

  if request.method == 'POST':
    absent_students = [key.split("-")[1] for key, id in request.POST.items() if key.startswith('student-')]

    form = forms.CallForm(request.POST)
    #print(form.is_valid())
    if form.is_valid():
      for studentID in absent_students:
        print(studentID)
        call_Instance = Call(date=form.cleaned_data['date'], creneaux=form.cleaned_data['creneaux'])
        call_Instance.student = Student.objects.filter(id=studentID)[0]
        call_Instance.isMissing = True
        call_Instance.save()
      return HttpResponseRedirect('/')
  else:
    pass
  
  context = {
    'student_liste' : student_liste,
    'cursus_liste' : cursus_liste,
    'creneaux_liste' : creneaux_liste
  }
  return HttpResponse(template.render(context,request))

def manage_roll(request):

  result_liste = Call.objects.all()

  template = loader.get_template('lycee/rolls/detail.html')

  context = {
    'liste' : result_liste
  }

  return HttpResponse(template.render(context,request))

def make_roll(request, call_id):
  call_liste = Call.objects.get(id=call_id)
  student_liste = Student.objects.get(id=call_liste.student.id)
  creneaux_liste = name=call_liste.creneaux
  template = loader.get_template('lycee/rolls/form.html')
  
  if request.method == 'POST':
    form = forms.PresenceForm(request.POST)
    
    if form.is_valid():
      call_Instance = Presence(
        date=call_liste.date, 
        isMissing=call_liste.isMissing,
        reason=form.cleaned_data['reason'],
        start_time=creneaux_liste.start_time, 
        stop_time=creneaux_liste.stop_time,
        student = Student.objects.filter(id=call_liste.student.id)[0])
      call_Instance.save()
      call_liste.delete()
    return HttpResponseRedirect('/rolls')
  else:
    pass
  
  context = {
    'call_liste' : call_liste,
    'student_liste' : student_liste,
    'creneaux_liste' : creneaux_liste,
  }
  return HttpResponse(template.render(context,request))

def absense(request, cursus_id):
  student_liste = Student.objects.filter(cursus=cursus_id).order_by('cursus')
  template = loader.get_template('lycee/presence/detail.html')
  context = {
    'student_liste' : student_liste,
    'cursus' : Cursus.objects.get(id=cursus_id)
  }
  return HttpResponse(template.render(context,request))

def visualize_absense(request, cursus_id, student_id):
  liste_presence = Presence.objects.filter(student=student_id).order_by('date')
  lenght = len(liste_presence)

  template = loader.get_template('lycee/presence/vizualize.html')
  context = {
    'student' : Student.objects.get(id=student_id),
    'cursus' : Cursus.objects.get(id=cursus_id),
    'liste_presence' : liste_presence,
    'lenght' : lenght
  }
  return HttpResponse(template.render(context,request))


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




  