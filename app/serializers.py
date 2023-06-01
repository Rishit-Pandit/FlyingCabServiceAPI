from rest_framework import serializers
from .models import ItemModel, Package, TourPoint, User, Booking

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = ItemModel
		fields = ['id','name','price']


class PackageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Package
		fields = ['id', 'Title', 'Price', 'Type', 'Description', 'Image', 'Itinerary']


class TourPointSerializer(serializers.ModelSerializer):
	class Meta:
		model = TourPoint
		fields = ['id', 'Name', 'Type', 'Image']


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'Name', 'PhoneNumber', 'Email']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['id', 'Package', 'User', 'Vehicle', 'DateBooked', 'PrefDate', 'SpecReq']