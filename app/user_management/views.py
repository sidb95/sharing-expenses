from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError


# 1. List person
@api_view(('GET',))
def get(request):
    '''
    Lists the person with the provided contact number (```contact``` field
    of the GET request)
    '''
    if (request.method == "GET"):
        try:
            person = Person.objects.filter(contact = request.GET.get('contact'))[0]
        except IndexError:
            return Response(
                "Invalid key (should be ```contact```) or phone number does not exist.", 
                status=status.HTTP_400_BAD_REQUEST
            )
        #
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #

# 2. Create person
@api_view(('POST',))
@csrf_exempt
def post(request):
    '''
    Create person with the given data. The ```total``` field
    is 0 by default.
    '''
    if request.method == "POST":
        uuid = len(Person.objects.all()) + 1
        try:
            data = {
                'uuid': uuid,
                'name': request.POST['name'], 
                'email': request.POST['email'], 
                'contact': request.POST['contact']
            }
        except MultiValueDictKeyError:
            return Response("Key error", status=status.HTTP_400_BAD_REQUEST)
        #
        serializer = PersonSerializer(data=data)
        #
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
