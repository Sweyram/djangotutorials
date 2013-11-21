from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 255)
	slug = models.SlugField(max_length = 255)
	body = models.TextField()
	author = models.CharField(max_length = 255)
	pub_date =  models.DateTimeField()

	def __unicode__(self):
		return self.title	