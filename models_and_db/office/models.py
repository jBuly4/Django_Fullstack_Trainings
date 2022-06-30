from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):

        return f"{self.last_name}, {self.first_name} is {self.age} years old "

# to run migrations for new models of new app:
# register your app then run 'python manage.py makemigrations office'

# work with models in a shell
'''
(venv) jb@MBPjb models_and_db % python manage.py shell
Python 3.10.0 (default, Dec 20 2021, 00:18:44) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from office.models import Patient
>>> carl = Patient(first_name='carl', last_name='smith', age=30)
>>> carl.age
30
>>> carl.age < 20
False
>>> carl.save()  # saving created instance in db
>>> Patient.objects.create(first_name='susan', last_name='smith', age=40)  # shorter way to create and save record to db
<Patient: Patient object (2)>  # is an index position
>>> mylist = [Patient(first_name='adam', last_name='smith', age=40), Patient(first_name='karl', last_name='marx', 
age=40)]
>>> Patient.objects.bulk_create(mylist)  # multiple objects to create and save
[<Patient: Patient object (4)>, <Patient: Patient object (5)>]

# getting objects from db
>>> from office.models import Patient
>>> Patient.objects.all()
<QuerySet [<Patient: Patient object (1)>, <Patient: Patient object (2)>, <Patient: Patient object (3)>, 
<Patient: Patient object (4)>, <Patient: Patient object (5)>]>  # it's a list, so 
>>> Patient.objects.all()[0]
<Patient: Patient object (1)>  # to make it more readable we need to define representation method in our model and 
reload shell
>>> from office.models import Patient
>>> Patient.objects.all()[0]  # you also can use slicing
<Patient: smith, carl is 30 years old >

# https://docs.djangoproject.com/en/4.0/ref/models/querysets/
# Filter() and Get()
# .get() is to grab a single item from Model table
# .filter() is to gram multiple records which are correspond to our condition
# .filter() methods can be chained together
# from django.db.models import Q - from that function we can use logic operators OR (|) and AND (&)

>>> from office.models import Patient
>>> Patient.objects.get(pk=1)
<Patient: smith, carl is 30 years old >
>>> Patient.objects.get(pk=4)
<Patient: smith, adam is 40 years old >
>>> Patient.objects.get(pk=10)
Traceback (most recent call last):
...
office.models.Patient.DoesNotExist: Patient matching query does not exist.
>>> Patient.objects.get(last_name='smith')
Traceback (most recent call last):
...
office.models.Patient.MultipleObjectsReturned: get() returned more than one Patient -- it returned 3!  # get returns 
only 1 record!

>>> Patient.objects.filter(last_name='smith').all()
<QuerySet [<Patient: smith, carl is 30 years old >, <Patient: smith, susan is 40 years old >, <Patient: smith, adam is 40 years old >]>
>>> Patient.objects.filter(last_name='smith').filter(age=40).all()  # chained filters
<QuerySet [<Patient: smith, susan is 40 years old >, <Patient: smith, adam is 40 years old >]>

# you cand assign Patient.objects.filter(last_name='smith') to a variable and then apply to it another filter

>>> from django.db.models import Q
>>> Patient.objects.filter(Q(last_name='smith') & Q(age=40)).all()
<QuerySet [<Patient: smith, susan is 40 years old >, <Patient: smith, adam is 40 years old >]>
>>> Patient.objects.filter(Q(last_name='smith') | Q(age=30)).all()
<QuerySet [<Patient: smith, carl is 30 years old >, <Patient: smith, susan is 40 years old >, <Patient: smith, adam is 40 years old >]>

# field lookups. to use filter with <, >, <=, >=
# syntax
Model.objects.filter(name__startswith='s')

>>> Patient.objects.filter(last_name__startswith='s').all()
<QuerySet [<Patient: smith, carl is 30 years old >, <Patient: smith, susan is 40 years old >, <Patient: smith, adam is 40 years old >]>

>>> Patient.objects.filter(age__in=[20, 30, 40]).all()
<QuerySet [<Patient: smith, carl is 30 years old >, <Patient: smith, susan is 40 years old >, <Patient: smith, adam is 40 years old >, <Patient: marx, karl is 40 years old >]>

>>> Patient.objects.filter(age__gte=39).all()  # greater or equal than
<QuerySet [<Patient: smith, susan is 40 years old >, <Patient: smith, adam is 40 years old >, <Patient: marx, karl is 40 years old >]>

>>> Patient.objects.order_by('age').all()
<QuerySet [<Patient: smith, carl is 30 years old >, <Patient: bolus, mimi is 36 years old >, <Patient: smith, susan is 40 years old >, <Patient: smith, adam is 40 years old >, <Patient: marx, karl is 40 years old >]>
>>> Patient.objects.order_by('last_name').all()
<QuerySet [<Patient: bolus, mimi is 36 years old >, <Patient: marx, karl is 40 years old >, <Patient: smith, carl is 30 years old >, <Patient: smith, susan is 40 years old >, <Patient: smith, adam is 40 years old >]>



'''