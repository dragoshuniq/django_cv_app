from django.db import models 
class Person(models.Model):
    personId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    birthDate = models.DateField()
    photoFile = models.ImageField(upload_to ='images/')
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Study(models.Model):
    studyId = models.AutoField(primary_key=True)
    institutionName = models.CharField(max_length=200)
    startDate = models.DateField()
    endDate = models.DateField()
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)


class Language(models.Model):
    languageId = models.AutoField(primary_key=True)
    languageName = models.CharField(max_length=50)
    languageLevel = models.CharField(max_length=50, default=None)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)


class Contact(models.Model):
    contactId = models.AutoField(primary_key=True)
    contactType = models.CharField(max_length=150)
    contactDescription = models.CharField(max_length=200, default=None)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)


class Experience(models.Model):
    experienceId = models.AutoField(primary_key=True)
    experienceName = models.CharField(max_length=200)
    experienceDescription = models.CharField(max_length=500)
    startDate = models.DateField()
    endDate = models.DateField()
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)


class Award(models.Model):
    awardId = models.AutoField(primary_key=True)
    awardName = models.CharField(max_length=100)
    awardDescription = models.CharField(max_length=500)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)


class OtherInformation(models.Model):
    infoId = models.AutoField(primary_key=True)
    infoName = models.CharField(max_length=100)
    infoDescription = models.CharField(max_length=500)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)