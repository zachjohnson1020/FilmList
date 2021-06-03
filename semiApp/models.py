from django.db import models

# Create your models here.
class ShowsManager(models.Manager):
	def Add_validator(self, postData):
		errors = {}
		#add keys and values to errors dictionary for each invalid field
		if len(postData['title']) == 0:
			errors['titleReq'] = 'The title is required'
		elif len(postData['title']) < 2:
			errors['titleLen'] = 'Title should be at least 2 characters'

		if len(postData['network']) < 3:
			errors['networkReq'] = 'Network should be at least 3 characters'

		if len(postData['desc']) < 10:
			errors['descReq'] = 'Description should be at least 10 characters'

		return errors
	



class Shows(models.Model):
	Title = models.CharField(max_length=255)
	Network = models.CharField(max_length=50)
	Release_Date = models.DateField()
	Description = models.CharField(max_length=300, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True) 
	objects = ShowsManager()

