from django.db import models

# Create your models here.
class ganam_songs(models.Model):
	artist1=models.CharField(max_length=100)
	artist2=models.CharField(max_length=100)   
	release_year = models.IntegerField()
	release_label = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	album =models.CharField(max_length=50)
	track=models.CharField(max_length=100)
	hit=models.IntegerField()
	# docfile = models.FileField(upload_to='images/%Y/%m/%d')
	star=models.CharField(max_length=20)
	language=models.CharField(max_length=20)
	
	def _unicode_(self):
		return self.song_title
