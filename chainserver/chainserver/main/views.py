from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.decorators.csrf import requires_csrf_token

import logging, logging.config
import sys

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}

@csrf_exempt
def test(request):
    if request.method == "POST":
        #when user server connects
        return JsonResponse({'roman': 'gulasz'})
    if request.method == "GET":
        #when client connects within url bar
        return JsonResponse({'kiedys': 'tobylo'})