from django.shortcuts import render,HttpResponseRedirect,Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ItemModel, Package, TourPoint, User, Booking
from .serializers import ItemSerializer, PackageSerializer, TourPointSerializer, UserSerializer, BookingSerializer

# Create your views here.
@csrf_exempt
def ItemsView(request):

    if request.method == 'GET':
        items = ItemModel.objects.all()
        serializer = ItemSerializer(items, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =ItemSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)


@csrf_exempt
def PackagesView(request):

    if request.method == 'GET':
        items = Package.objects.all()
        serializer = PackageSerializer(items, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PackageSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)


@csrf_exempt
def TourPointsView(request):

    if request.method == 'GET':
        items = TourPoint.objects.all()
        serializer = TourPointSerializer(items, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TourPointSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)


@csrf_exempt
def TourPointView(request, nm):
    try:
        item = TourPoint.objects.get(id = nm)
    except TourPoint.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = TourPointSerializer(item)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TourPointSerializer(item,data =data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == "DELETE":
        item.delete()
        return HttpResponse(status =204)


@csrf_exempt
def UsersView(request):

    if request.method == 'GET':
        items = User.objects.all()
        serializer = UserSerializer(items, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)


@csrf_exempt
def BookingsView(request):

    if request.method == 'GET':
        items = Booking.objects.all()
        print(len(items))
        serializer = BookingSerializer(items, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['id'] = len(Booking.objects.all()) + 1
        serializer = BookingSerializero(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)


@csrf_exempt
def UserView(request, nm):
    try:
        item = User.objects.get(id = nm)
    except User.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = UserSerializer(item)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(item,data =data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == "DELETE":
        item.delete()
        return HttpResponse(status =204)


@csrf_exempt
def BookingView(request, nm):
    try:
        item = Booking.objects.get(id = nm)
    except Booking.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = BookingSerializer(item)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookingSerializer(item,data =data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == "DELETE":
        item.delete()
        return HttpResponse(status =204)


@csrf_exempt
def ItemView(request, nm):
    try:
        item = ItemModel.objects.get(id = nm)
    except ItemModel.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item,data =data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == "DELETE":
        item.delete()
        return HttpResponse(status =204)
