from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect

from blog.forms import EnterVerbForm
from blog.forms import AskVerbForm
from blog.forms import Button
from blog.models import Verb
from blog.models import Error
from blog.models import DateReport
from django.db import connection

import pandas as pd
import random

# dataframe=pd.read_csv('blog/phrasal_verbs.csv', sep=', ')
# dataframe=pd.DataFrame(dataframe)

def date_actuelle(request):
    numbers=[i for i in range(len(dataframe))]
    number = random.choice(numbers)
    word=dataframe['Meaning'].iloc[number]
    return render(request, 'blog/phrasal_verbs.html', {'date': word})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def home(request,truth=False):
    xy=(0,0)
    l=[]
    cursor=connection.cursor()
    button_delete = Button(request.POST or None)
    if button_delete.is_valid():
        cursor.execute('DELETE FROM blog_error')
        for p in Verb.objects.raw('SELECT id FROM blog_verb ORDER BY attempts DESC'):
            p.proposition=''
            p.attempts=0
            p.save()
    for p in DateReport.objects.raw('SELECT id FROM blog_datereport'):
        xy=(p.date,p.success_ratio)
        l.append(xy)
    #print(L)

    if Error.objects.order_by('-attempts'):
        truth=True
        verb_to_learn=Error.objects.order_by('-attempts')[0]
        phrasal_verb_to_learn=verb_to_learn.phrasal_verb
        meaning_to_learn=verb_to_learn.meaning
        example_to_learn=verb_to_learn.example
    else :
        truth=False
        phrasal_verb_to_learn=''
        meaning_to_learn=''
        example_to_learn=''
    return render(request, 'blog/home.html', locals())

def enter_verbs(request):
    form = EnterVerbForm(request.POST)
    if form.is_valid():
        form.save()
        verb=Verb.objects.order_by('-id')[0]
        verb.start_with=verb.phrasal_verb[3]
        verb.save()
        form=EnterVerbForm()
    return render(request, 'blog/enter_verbs.html', locals())

def ask_verbs(request,number=85,meaning='to accept a decision',example='',truth=False):
    xy=(0,0)
    l=[]
    L=[]
    to_go=0
    verb=Verb.objects.get(id=number)
    finish=False
    if Error.objects.filter(phrasal_verb=verb.phrasal_verb).count() > 0:
        error=Error.objects.get(phrasal_verb=verb.phrasal_verb)
    else :
        error=Error(verb.id,verb.phrasal_verb,verb.meaning,verb.example,0)
    # print(verb.phrasal_verb,verb.meaning,verb.example,verb.attempts)
    # print(error.id)
    form = AskVerbForm(request.POST or None)
    if form.is_valid():
        proposition = form.cleaned_data['proposition']
        if proposition==verb.phrasal_verb:
            truth=True
            example=verb.example
            verb.attempts+=1
        else :
            truth=False
            phrasal_verb=verb.phrasal_verb
            error.attempts+=1
            error.save()
        verb.proposition=proposition
        verb.save()
        if Verb.objects.filter(attempts=0).count() > 0:
            for p in Verb.objects.raw('SELECT id FROM blog_verb WHERE proposition!=phrasal_verb'):
                L.append(p.id)
                to_go+=1
        else :
            finish=True
            to_go = 0
            return render(request, 'blog/ask_verbs.html', locals())
        number=random.choice(L)
        meaning=Verb.objects.get(id=number).meaning
        form=AskVerbForm()
    else :
        pass
    return render(request, 'blog/ask_verbs.html', locals())

def statistics(request):
    L=[]
    l=[]
    cursor=connection.cursor()
    button_save = Button(request.POST or None,prefix='button_save')
    button_delete = Button(request.POST or None,prefix='button_delete')
    errors={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    total_verbs = Verb.objects.filter(attempts=1).count()
    failed_attempts=0
    success_ratio=0
    start_with=''
    for p in Error.objects.raw('SELECT id FROM blog_error ORDER BY attempts DESC'):
        L.append((p.phrasal_verb,p.meaning,p.attempts))
        start_with=p.phrasal_verb[3]
        errors[start_with]+=p.attempts
        failed_attempts = failed_attempts + p.attempts
    total_attempts=total_verbs+failed_attempts
    if total_attempts!=0:
        success_ratio=int((total_attempts-failed_attempts)/total_attempts*100)
    else :
        success_ratio=100
    for letter in errors:
        l.append((letter,errors[letter]))
    if request.method == 'POST':
        if 'Save score' in request.POST:
            print(1)
            if button_save.is_valid() and Error.objects.order_by('-attempts'):
                print(2)
                date=DateReport.objects.order_by('-date')[0].date+1
                report=DateReport(success_ratio=success_ratio,date=date)
                report.save()
        elif 'Delete score' in request.POST:
            print(3)
            if button_delete.is_valid() :
                print(4)
                for p in Verb.objects.raw('SELECT id FROM blog_verb ORDER BY attempts DESC'):
                    p.proposition=''
                    p.attempts=0
                    p.save()
                cursor.execute('DELETE FROM blog_error')
    return render(request, 'blog/statistics.html', locals())
