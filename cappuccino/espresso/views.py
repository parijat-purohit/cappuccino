from django.http import HttpResponse
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import AnonRateThrottle


@api_view(['GET'])
@throttle_classes([AnonRateThrottle])
def espresso_view(request):
    return HttpResponse("Hello World")
