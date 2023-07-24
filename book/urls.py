from django.urls import path
from .views import (AllCreateBookView,DetailUpdateDeleteApiView)
urlpatterns = [
    path('',AllCreateBookView.as_view()),
    # path('<pk>',DetailBookView.as_view()),
    # # path('create/',CreateBookView.as_view()),
    # path('update/<pk>/',UpdateBookView.as_view()),
    # path('delete/<pk>/',DeleteBookView.as_view()),
    path('<pk>',DetailUpdateDeleteApiView.as_view())
]