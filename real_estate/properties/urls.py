from django.urls import path

from .views import create_property, list_property, property_list_api, view_property

urlpatterns = [
    path("api/properties", property_list_api, name="list-property-api"),
    path("properties/add", create_property, name="add-property"),
    path("properties/<int:pk>", view_property, name="view-property"),
    path("", list_property, name="list-property"),
]
