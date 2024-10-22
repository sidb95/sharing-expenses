from django.urls import path
from .views import post as expense_post
from .views import get_overall_expenses
from user_management.urls import person_get
from .views import download_balance_sheet

urlpatterns = [
    path('api/add-expense', expense_post),
    path('api/get-overall-expenses', get_overall_expenses),
    path('api/get-details', person_get),
    path('api/balance-sheet', download_balance_sheet)
]
