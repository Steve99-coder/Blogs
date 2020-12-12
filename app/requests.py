import urllib.request,json
from . import create_app
import requests
from .models import Quote

def get_quotes():
   '''
   function that gets the json response to url request
   '''
   with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
       get_quote_data = url.read()
       get_quote_response = json.loads(get_quote_data)
       print(get_quote_response)
       quote_objects = None
       if get_quote_response:
           id = get_quote_response.get('id')
           author = get_quote_response.get('author')
           quote = get_quote_response.get('quote')
           quote_objects = Quote(id, author, quote)
   return quote_objects