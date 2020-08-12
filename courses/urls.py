from django.urls import path
from .views import *

urlpatterns = [
    path("", index_page, name="index_page_url"),
    path("about/", about_page, name="about_page_url"),
    path("contacts/", contacts_page, name="contact_page_url"),
]
