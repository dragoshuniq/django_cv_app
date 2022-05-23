from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Study, Language, Contact, Experience, Award, OtherInformation

def personal_cv(request):
    person = Person.objects.get(personId=1)
    studies = list(Study.objects.all())
    languages = Language.objects.all()
    contacts = Contact.objects.all()
    experience = Experience.objects.all()
    awards = Award.objects.all()
    information = OtherInformation.objects.all()
    print(studies)
    
    return render(request, 'curriculum_vitae.html',
    {'person': person,'studies':studies,'languages':languages,
    'contacts':contacts,'experience':experience,'awards':awards,'information':information})

