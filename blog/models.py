from django.db import models
from django.utils import timezone
from django import forms

class Verb(models.Model):
    id = models.AutoField(primary_key=True)
    phrasal_verb = models.CharField(max_length=100)
    meaning = models.CharField(max_length=100)
    example = models.CharField(max_length=100)
    proposition = models.CharField(max_length=100,default='')
    attempts = models.IntegerField(default=0)
    start_with = models.CharField(max_length=1,default='')

    class Meta:
        verbose_name = "verb"

class Error(models.Model):
    id = models.AutoField(primary_key=True)
    phrasal_verb = models.CharField(max_length=100)
    meaning = models.CharField(max_length=100)
    example = models.CharField(max_length=100)
    attempts = models.IntegerField(default=0)

class DateReport(models.Model):
    id = models.AutoField(primary_key=True)
    success_ratio = models.IntegerField(default=0)
    date = models.IntegerField(default=0)
    phrasal_verb = models.CharField(max_length=100,default='')
    meaning = models.CharField(max_length=100,default='')
    example = models.CharField(max_length=100,default='')

# class Proposition(models.Model):
#     id = models.AutoField(primary_key=True)
#     proposition = models.CharField(max_length=100,default='')
#
#     class Meta:
#         verbose_name = "propo"

    # def __str__(self):
    #     """
    #     Cette méthode que nous définirons dans tous les modèles
    #     nous permettra de reconnaître facilement les différents objets que
    #     nous traiterons plus tard dans l'administration
    #     """
    #     return(self.phrasal_verb,self.meaning)

# class Name(models.Model):
#     name = models.TextField(max_length=100)
#
#     class Meta:
#         verbose_name = "name"
#
#     def __str__(self):
#         """
#         Cette méthode que nous définirons dans tous les modèles
#         nous permettra de reconnaître facilement les différents objets que
#         nous traiterons plus tard dans l'administration
#         """
#         return self.name
#
# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)
