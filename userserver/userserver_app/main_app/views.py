import json

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import requires_csrf_token

import logging, logging.config
import sys
import requests


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

def test(request):
    post_data = {'foo':'bar'}
    response = requests.post('http://127.0.0.1:8000/main/test/', data=post_data)
    logging.config.dictConfig(LOGGING)
    return JsonResponse(json.loads(response.text),safe=False)
