from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExpenseSerializer
from django.views.decorators.csrf import csrf_exempt
from user_management.models import Person
from user_management.serializers import PersonSerializer
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from .models import Expense


# Create expense
@api_view(('POST',))
@csrf_exempt
def post(request):
    '''
    Create the expense. The expense sharing is rounded off to the
    floor of the shared expense.
    '''
    try:
        amount = int(request.POST['amount'])
        type = request.POST['type']
        contacts = request.POST['contacts']
        if (len(contacts) == 0):
            raise TypeError
    except MultiValueDictKeyError:
        return Response("Key Error", status=status.HTTP_400_BAD_REQUEST)
    except TypeError:
        return Response("Specify at least one contact", status=status.HTTP_400_BAD_REQUEST)

    contacts = list(map(int, contacts.split(',')))
    no_contacts = len(contacts)
    data = {}
    #
    try:
        if (type == "equal"):
            expense = amount // no_contacts
            for contact in contacts:
                data[contact] = expense
            #
        elif (type == "exact"):
            try:
                expenses = list(map(int, request.POST['expenses'].split(',')))
                if (len(expenses) == no_contacts):
                    for i in range(0, no_contacts):
                        data[contacts[i]] = expenses[i]
                else:
                    raise MultiValueDictKeyError
            except MultiValueDictKeyError:
                return Response("Key error", status=status.HTTP_400_BAD_REQUEST)            
            #
        elif (type == "percentage"):
            try:
                percentages = list(map(int, request.POST['percentages'].split(',')))
                if (sum(percentages) == 100 and len(percentages) == no_contacts):
                    for i in range(0, no_contacts):
                        data[contacts[i]] = int(amount * (percentages[i] / 100))
                    #
                else:
                    raise TypeError
            except MultiValueDictKeyError:
                return Response("Key error", status=status.HTTP_400_BAD_REQUEST)
            except TypeError:
                return Response(
                    "Error: Sum of percentages not equal to 100 or number of values of percentages not equal to number of contacts", 
                    status=status.HTTP_400_BAD_REQUEST
                )
            #
        #
        else:
            raise TypeError
        #
    except TypeError:
        return Response(
            "Allowed values for type are equal, exact and percentage.", 
                status=status.HTTP_400_BAD_REQUEST
        )
    #
    uuid = len(Expense.objects.all()) + 1
    print(uuid)
    dict1 = {
        'uuid': uuid,
        'amount': amount, 
        'users_expense': data,
    }
    #
    for contact in contacts:
        try:
            p = Person.objects.filter(contact=contact)[0]
        except IndexError:
            return Response(
                "Contact " + str(contact) + " not saved.", 
                status=status.HTTP_400_BAD_REQUEST
            )
        #
        if p.total is None:
            p.total = dict1['users_expense'][contact]
        else:
            p.total += dict1['users_expense'][contact]
        #
        p.save()
    #
    serializer = ExpenseSerializer(data=dict1)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get Overall Expenses
@api_view(('GET',))
def get_overall_expenses(request):
    """
    This method returns a response for all the persons 
    if the request method is GET. The ```total``` field of the
    Person instance gives the overall expense of that person.
    """
    if (request.method == "GET"):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# Download Balance Sheet
@api_view(('GET',))
def download_balance_sheet(request):
    """
    
    """
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    f = open('static/file.txt', 'w')
    f.write(str(serializer.data))
    f.close()
    f = open('static/file.txt', 'r')
    response = HttpResponse(f)
    response['Content-Disposition'] = 'attachment; filename="balance-sheet.txt"'
    return response
