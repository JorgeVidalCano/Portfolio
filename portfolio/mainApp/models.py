from django.db import models

class MetaData(models.Model):
    metaDescription = models.CharField(max_length=60, blank=True)
    metaKeywords = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.metaDescription

class HomeData(models.Model):
    mainName = models.CharField(max_length=20)
    description = models.CharField(max_length=60)

    def __str__(self):
        return self.mainName

class AboutData(models.Model):
    firstParagraph = models.CharField(max_length=300)
    title = models.CharField(max_length=50)
    birthday = models.DateField()
    country = models.CharField(max_length=8)
    education = models.CharField(max_length=20) 
    email = models.CharField(max_length=35)
    extraInfobotoom = models.CharField(max_length=300)

    skillText = models.CharField(max_length=300)
    