from django.contrib import admin
from .models import Person, Study, Language, Contact, Experience, Award, OtherInformation

appModels = [Person, Study, Language, Contact, Experience, Award, OtherInformation]
admin.site.register(appModels)

# Register your models here.
