from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ItemModel(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 80, blank = False)
	price = models.IntegerField()

	class Meta:
		ordering = ['id']

	def __str__(self):
		return f"{self.name}: {self.price}"

class TourPoint(models.Model):
	POINT_TYPES = [
		("Mo", "Monastery"),
		("Ma", "Market"),
		("Mn", "Monument"),
		("Wf", "Water Fall"),
		("Mt", "Mountain"),
		("Bg", "Botanical Garden"),
		("Zg", "Zoological Garden"),
		("Te", "Tea Estate"),
	]
	id = models.IntegerField(primary_key = True)
	Name = models.CharField(max_length = 180)
	Type = models.CharField(max_length = 2, choices=POINT_TYPES)
	Image = models.CharField(max_length = 500)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.Name


class Package(models.Model):
	TYPES = [
		("PD", "Pickup Drop"),
		("TP", "Tour Package"),
	]
	id = models.IntegerField(primary_key = True)
	Title = models.CharField(max_length = 180)
	Price = models.IntegerField()
	Type = models.CharField(max_length = 2, choices=TYPES)
	Description = models.CharField(max_length = 200)
	Image = models.URLField(max_length = 500)
	Itinerary = models.ManyToManyField(TourPoint, verbose_name="list of TourPoints")

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.Title


class User(models.Model):
	id = models.IntegerField(primary_key = True)
	Name = models.CharField(max_length = 200)
	PhoneNumber = models.IntegerField()
	Email = models.EmailField()

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.Name


class Booking(models.Model):
	VEHICLES = [
		('De', 'Desire - 4 seater'),
		('Al', 'Alto - 4 seater'),
		('Wg', 'WagonR - 5 seater'),
		('In', 'Innova - 6 seater'),
	]
	id = models.IntegerField(primary_key = True)
	Package = models.ForeignKey(Package, on_delete = models.CASCADE)
	User = models.ForeignKey(User, on_delete = models.CASCADE)
	Vehicle = models.CharField(max_length = 2, choices = VEHICLES)
	DateBooked = models.DateField()
	PrefDate = models.DateField()
	SpecReq = models.TextField(max_length = 500)


	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.Package.__str__()