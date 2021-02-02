from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class MetaData(models.Model):
    metaDescription = models.CharField(max_length=60, blank=True)
    metaKeywords = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.metaDescription

class HomeData(models.Model):
    mainName = models.CharField(max_length=20)
    description = models.CharField(max_length=60)
    mainImg = models.ImageField(upload_to ='Images', blank=True)

    def __str__(self):
        return self.mainName

class AboutData(models.Model):
    firstParagraph = models.TextField(max_length=300)
    title = models.CharField(max_length=50)
    birthday = models.DateField()
    city = models.CharField(max_length=8)
    github = models.CharField(max_length=60)
    education = models.CharField(max_length=20) 
    email = models.EmailField(max_length=35)
    extraInfobottom = models.TextField(max_length=300)
    skillText = models.TextField(max_length=300)
    sideImg = models.ImageField(upload_to ='Images', blank=True,)

LEVEL = [
    ('Basic', 'Basic'),
    ('Medium', 'Medium'),
    ('Advance', 'Advance')
]
class SkillData(models.Model):
    skill = models.CharField(max_length=30)
    img = models.ImageField(upload_to ='Images', blank=True,)
    level = models.CharField(choices=LEVEL, max_length=7)
    percentaje = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=True)

    def __str__(self):
            return self.skill