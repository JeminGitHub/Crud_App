from django.urls import path
from . import views

# from .views import signup_view, signin_view

urlpatterns = [

    path('', views.add, name='home'),
    path('edit/', views.Crudlistview.as_view(), name='edit'),
    path('detail/<int:pk>/detail/', views.CrudDetailview.as_view(), name='detail'),
    path('update/<int:pk>/update/', views.CrudUpdate.as_view(), name='update'),
    path('delete/<int:pk>/delete/', views.CrudDeleteView.as_view(), name='delete'),

    path('signup/', views.register_request, name='signup'),
    path('signin/', views.login_request, name='signin'),
]

# <a href="{% url 'book_update' book.pk %}">Edit Book</a>
#
# path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),