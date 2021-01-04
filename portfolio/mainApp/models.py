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