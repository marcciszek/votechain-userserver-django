from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
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
def block(request):
    logging.config.dictConfig(LOGGING)
    if request.method == "POST":
        logging.info(request.POST)
        user = request.POST['user']
        vote = request.POST['vote']
        # add data to blockchain
    if request.method == "GET":
        #when client connects within url bar
        logging.info("client")
        return HttpResponseNotFound("Nic tutaj nie ma")