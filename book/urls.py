from django.urls import path
from . views import *
from . import views

urlpatterns = [
    path('',BookViews.as_view(),name='index'),
    path('book-detail/<int:id>',BookDetails.as_view(),name="bookdetails"),
]
