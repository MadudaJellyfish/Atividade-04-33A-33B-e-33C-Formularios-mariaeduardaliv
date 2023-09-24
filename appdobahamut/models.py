from django.db import models


class Jogos(models.Model):
  tittle = models.CharField(max_length = 50)
  director = models.CharField(max_length = 70)
  mainProgrammer = models.CharField(max_length = 70)
  producer = models.CharField(max_length = 70)

class Mecanicas(models.Model):
  
  LIKE_LEVELS = [
    ("S", "Super Gosto"),
    ("M", "Maneirinho"),
    ("N", "Nhe"),
  ]
  
  tittle = models.CharField(max_length = 50)
  discription = models.CharField(max_length = 100)
  howMuchILike = models.CharField(max_length = 1, 
choices = LIKE_LEVELS)
  
class Tables(models.Model):
  tittle = models.CharField(max_length = 50)
  releaseDate = models.DateField()
  platforms = models.CharField(max_length = 50)

