import json
from .forms import ContVoteForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
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
    return JsonResponse(json.loads(response.text), safe=False)


@login_required
def voting(request):
    if request.method == 'POST':
        form = ContVoteForm(request.POST)
        logging.config.dictConfig(LOGGING)
        logging.info(str(form.Cont))
        # do the magick
        return HttpResponseRedirect('/account/logout/')
    else:
        form = ContVoteForm()
        return render(request, 'vote/voting.html', {'form': form})


def sendvote(request):
    logging.config.dictConfig(LOGGING)
    logging.info("ktos tu jest")
    logging.info(request.body.decode('utf-8'))
    return JsonResponse({'boo','far'})