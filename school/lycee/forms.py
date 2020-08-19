from django.forms.models import ModelForm
from .models import Student, Presence, Call, Creneaux

class StudentForm(ModelForm):
  class Meta:
    model = Student
    fields = [
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comment",
      "cursus",
    ]

class PresenceForm(ModelForm):
  class Meta:
    model = Presence
    fields = [
      "reason",
      "isMissing",
      "date",
      "start_time",
      "stop_time",
      "student",
    ]
class CallForm(ModelForm):
  class Meta:
    model = Call
    fields = [
      "isMissing",
      "date",
      "student",
      "creneaux",
    ]
class CreneauxForm(ModelForm):
  class Meta:
    model = Creneaux
    fields = [
      "name",
      "start_time",
      "stop_time",
    ]