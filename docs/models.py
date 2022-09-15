from django.db import models

class Item(models.Model):
	class Meta:
		db_table = 'SystemItem'

	TYPES = (('FILE','File'), ('FOLDER','Folder'))
	id = models.CharField(max_length=64, unique=True, primary_key=True)
	url = models.CharField(max_length=128, blank=True)
	date = models.CharField(max_length=128)
	parentId = models.CharField(max_length=64, blank=True)
	type = models.CharField(choices=TYPES, max_length=64)
	size = models.IntegerField(blank=True, null=True)
