from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_spot, name='book_spot'),
    path('exit/<int:ticket_id>/', views.exit_gate, name='exit_gate'),
]
