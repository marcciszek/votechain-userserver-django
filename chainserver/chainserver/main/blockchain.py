from hashlib import sha256
import json
from time import time


class Block:
    def __init__(self, index, vote = None, user_hash = None, previous_hash = None,timestamp = None, nonce=0):
        self.index = index
        self.vote = vote
        self.user_hash = user_hash
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

    def write(self):
        return "id: "+str(self.index)+", vote: "+str(self.vote)+\
               ", user: "+str(self.user_hash)+", prev: "+str(self.previous_hash)+\
               ", nonce: "+str(self.nonce)+", time: "+str(self.timestamp)

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

import pkgutil
from . import static

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class Blockchain:
    def __init__(self):
        genesisblock = Block(0,"novote","nohash","genesis_block")
        self.chain = []
        self.chain.append(genesisblock)
        self.difficulty = 2

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def getFromFile(self):
        try:
            json_data = pkgutil.get_data(__name__, "static/chain.json")
            return json.loads(json_data)
        except Exception as error:
            return str(error)

    def loadFromFile(self):
        try:
            data = self.getFromFile()
            text = ""
            chain = []
            self.difficulty = data['difficulty']
            for el in data['chain']:
                block = Block(el['index'],el['vote'],el['user_hash'],el['previous_hash'],el['timestamp'],el['nonce'])
                text+=block.write()
                text+="\n"
                chain.append(block)
            self.chain = chain
            return text
        except Exception as error:
            return str(error)

    def saveToFile(self):
        try:
            f = open(str(dir_path)+"/static/chain.json","w")
            f.write(self.toJSON())
            f.close()
            return True
        except Exception as error:
            return str(error)

    @property
    def last_block(self):
        """
        return last block from the chain
        """
        return self.chain[-1]

    @property
    def length(self):
        return len(self.chain)

    def getblock(self,id):
        try:
            return self.chain[id]
        except:
            return None
        
    def proof_of_work(self,block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        block.timestamp = time()
        while not computed_hash.startswith('0' * self.difficulty):  # Blockchain.difficulty
            block.nonce += 1
            computed_hash = block.compute_hash()
        return block

    def add_block(self,block):
        previous_hash = self.last_block.compute_hash()
        block.index = len(self.chain)
        block.previous_hash = previous_hash
        newblock = self.proof_of_work(block)
        self.chain.append(newblock)
        return True

    def write(self):
        return self.block.compute_hash()