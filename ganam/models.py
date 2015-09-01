from django.db import models

# Create your models here.
class songs(models.Model):
	artist1=models.CharField(max_length=100)
	artist2=models.CharField(max_length=100)   
	release_year = models.IntegerField(max_length=10)
	release_label = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	album =models.CharField(max_length=50)
	track=models.CharField(max_length=100)
	hit=models.IntegerField(max_length=10)
	docfile = models.FileField(upload_to='images/%Y/%m/%d')
	star=models.CharField(max_length=20)
	language=models.CharField(max_length=20)
	
	def _unicode_(self):
		return self.song_title

class user_playlist(models.Model):
	user_name = models.CharField(max_length=100)
	user_song = models.ForeignKey(songs)
	
	def _unicode_(self):
		return self.user_name

