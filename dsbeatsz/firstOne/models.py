from django.db import models



class CHYNGYZ_AITMATOV(models.Model):
    Chyngyz_Aitmatov = models.CharField(max_length=255)
    year_of_brith = models.DateTimeField()
    Year_of_death = models.DateTimeField(blank=True)
    Biogarfia = models.TextField()
    Detstvo_unost = models.TextField()
    photo = models.ImageField()

class BIOGRAFY(models.Model):
    Chyngyz_Aitmatov = models.CharField(max_length=255)
    year_of_brith = models.DateTimeField()
    Year_of_death = models.DateTimeField(blank=True)
    Biogarfia = models.TextField()
    Detstvo_unost = models.TextField()
    photo = models.ImageField()

class DETSTVO_UNOST(models.Model):
    Chyngyz_Aitmatov = models.CharField(max_length=255)
    year_of_brith = models.DateTimeField()
    Year_of_death = models.DateTimeField(blank=True)
    Biogarfia = models.TextField()
    Detstvo_unost = models.TextField()
    photo = models.ImageField()

class LITERATURA(models.Model):
    TEXT = models.TextField()
    photo = models.ImageField()

class LICHNAYA_LIFE(models.Model):
    Text = models.CharField(max_length=255)
    year_of_brith = models.DateTimeField()
    Year_of_death = models.DateTimeField(blank=True)
    photo = models.ImageField()

class PHOTO_KARUSEL(models.Model):
    photo = models.ImageField()


