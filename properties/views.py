from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Property  # assuming your model is named Property

@cache_page(60 * 15)  # cache for 15 minutes
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})
