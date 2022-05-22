from django.shortcuts import render
from django.http import HttpResponse


def personal_cv(request):
    return render(request, 'curriculum_vitae.html')
