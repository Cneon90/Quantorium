from .functional import *

class Ferst:
    def __init__(self,get_response):
        #init_news()
        self._get_response = get_response
    def __call__(self,request):
        response = self._get_response(request)
        return response