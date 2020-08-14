from django.forms.models import ModelForm
from .models import Student, Presence

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