from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import get_all_properties

@cache_page(60 * 15)  # cache for 15 minutes
def property_list(request):
    properties = get_all_properties()
    return JsonResponse({"data": properties})
