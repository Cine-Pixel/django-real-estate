from django.urls import path
from properties.views import create_property, list_property, view_property

urlpatterns = [
    path("properties/add", create_property, name="add-property"),
    path("properties/<int:pk>", view_property, name="view-property"),
    path("", list_property, name="list-property"),
]
