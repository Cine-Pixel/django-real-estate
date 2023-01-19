from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import PropertyForm
from .models import Property
from .serializers import PropertySerializer


def create_property(request: HttpRequest) -> HttpResponse:
    """
    Create a new propert of :model:`properties.Property`.

    **Context**

    ``property``
        An instance of :model:`properties.Property`.

    **Template:**

    :template:`properties/create_property.html`

    """
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            property: Property = form.save(commit=False)
            property.owner = request.user
            property.save()
            return redirect(list_property)

    form = PropertyForm()
    context = {
        "form": form,
    }
    return render(request, "properties/create_property.html", context=context)


def list_property(request: HttpRequest) -> HttpResponse:
    """List all existing peoperities of :model:`properties.Property`.

    **Context**

    ``properties``
        A list of instances of :model:`properties.Property`.

    **Template:**

    :template:`properties/list_properties.html`

    """
    properties = Property.objects.all()
    context = {"properties": properties}
    return render(request, "properties/list_properties.html", context=context)


def view_property(request: HttpRequest, pk: int) -> HttpResponse:
    """Get details of one property of :model:`properties.Property`.

    **Context**

    ``Property``
        An instance of :model:`properties.Property`.

    **Template:**

    :template:`properties/view_property.html`

    """
    property = Property.objects.filter(id=pk).first()
    if property is None:
        return HttpResponse("<h1>Property not found</h1>")
    context = {"property": property}
    return render(request, "properties/view_property.html", context=context)


@api_view(["GET"])
def property_list_api(request: HttpRequest) -> Response:
    properties = Property.objects.all()
    data = PropertySerializer(properties, many=True).data
    return Response(data)
