from django.db import models

# Create your models here.


class Usregister(models.Model):
	uname = models.CharField(max_length=40)
	pwd =models.CharField(max_length=20)
	age = models.IntegerField(blank=True, null=True)

	# to rename table
	#class Meta:
	#	db_table="Renamedtable"

	def __str__(self):
		return self.uname +" | "+ str(self.age)

