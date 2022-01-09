import json
from random import choices
import string
from .forms import ContVoteForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import requires_csrf_token

from django.contrib.auth.hashers import PBKDF2PasswordHasher

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

@login_required
def voting(request):
    if request.method == 'POST':
        logging.config.dictConfig(LOGGING)
        form = ContVoteForm(request.POST)

        hasher = PBKDF2PasswordHasher()
        #salt = ''.join(choices(string.ascii_letters + string.digits, k=10))
        salt = "BlockChain"
        user_hash = hasher.encode(str(request.user), salt)

        post_data = {'user': str(request.user),
                     'vote': form['vote'].value(),
                     'hash': user_hash}

        logging.info(post_data)
        requests.post('http://127.0.0.1:8000/main/block/',
                      data=post_data)
        return HttpResponseRedirect('/account/logout/')
    else:
        form = ContVoteForm()
        return render(request,
                      'vote/voting.html',
                      {'form': form})
