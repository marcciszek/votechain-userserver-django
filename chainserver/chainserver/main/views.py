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

logging.config.dictConfig(LOGGING)

def log(text):
    logging.info(text)



from . import blockchain

@csrf_exempt
def block(request):
    logging.config.dictConfig(LOGGING)
    if request.method == "GET":
        #when client connects within url bar
        logging.info("client")
        return HttpResponseNotFound("Nic tutaj nie ma")

    if request.method == "POST":
        #logging.info(request.POST)
        #user = request.POST['user']
        vote = request.POST['vote']
        hash = request.POST['hash']

        # add data to blockchain
        blc = blockchain.Blockchain()
        blc.loadFromFile()
        #log(blc.length)
        if not(blc.didUserVote(hash)):
            log("vote added.")
            try:
                blc.add_block(blockchain.Block(blc.length,int(vote),str(hash)))
                #log(blc.length)
                result = blc.saveToFile()
            except Exception as error:
                log(str(error))
        else:
            log("user had already voted.")
        #poniżej
        '''
        a = blockchain.Blockchain()
        x = blockchain.Block(1, 2, "afasef")
        y = blockchain.Block(2, 1, "wgegre")
        z = blockchain.Block(3, 1, "fefefe")
        #a.add_block(x)
        #a.add_block(y)
        #a.add_block(z)
        #a.saveToFile()
        '''
        '''
        a.loadFromFile()
        log("xxx")
        for x in a.chain:
            log(x.write())
        log("xxx")

        if a.length>1:
            a.saveToFile()
        '''
        '''
        a.add_block(x)
        a.add_block(y)
        a.add_block(z)
        logging.info("startchain")
        for x in a.chain:
            logging.info(x.write())
        logging.info("endchain")
        logging.info("")
        r = a.saveToFile()
        logging.info(str(r))
        dj = a.getFromFile()
        logging.info(str(dj['chain']))
        for el in dj['chain']:
           log(str(el))
           log(str(el['vote']))
           log("")
        log("xxx")
        log(a.loadFromFile())
        log("xxx")
        #jay = json.loads(text)
        #logging.info(jay['glossary']['title'])
        '''