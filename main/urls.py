from django.urls import path
from main.views import Index, Book_del

app_name="main"

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('book_del/<int:id>/', Book_del.as_view(), name="book_del")

]