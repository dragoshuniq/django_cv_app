from django.contrib import admin
from .models import Person, Study, Language, Contact, Experience, Award, OtherInformation, Projects

appModels = [Person, Study, Language, Contact, Experience, Award, OtherInformation,Projects]
admin.site.register(appModels)

# Register your models here.
