from django.db import models

# Create your models here.
class Cursus(models.Model):
  name = models.CharField(
    max_length = 50,
    blank = False,
    null  = True,
    default = 'aucun'
  )
  year_from_bac = models.SmallIntegerField(
    help_text = "year since bac",
    verbose_name = "year",
    blank = False,
    null = True,
    default = 0
  )
  scholar_year = models.CharField(
    max_length = 9,
    blank = False,
    null = True,
    default = '0000-00001'
  )

class Student(models.Model):
  first_name = models.CharField(
    max_length = 50,
    blank = False,
    null = False
  )
  birth_date = models.DateField(
    verbose_name = 'date of birth',
    blank = False,
    null=  False
  )
  last_name = models.CharField(
    verbose_name = "lastname",
    help_text = "last name of student",
    blank = False,
    null = False,
    default = "???",
    max_length=255
  )
  phone = models.CharField(
    verbose_name = "phonenumber",
    help_text = "phone number of the student",
    blank = False,
    null = False,
    default = "0999999999",
    max_length = 10
  )
  email = models.EmailField(
    verbose_name="email",
    help_text = "mail of thee student",
    blank = False,
    null = False,
    default = "x@y.z",
    max_length = 255,
  )
  comment = models.CharField(
    verbose_name = "comments",
    help_text = "some comment abount the student",
    blank = True,
    null = False,
    default = "",
    max_length = 255
  )
  cursus = models.ForeignKey(
    Cursus,
    on_delete = models.CASCADE,
    null = True
  )

