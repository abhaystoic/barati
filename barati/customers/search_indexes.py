'''
Searching
'''
import datetime
from haystack import indexes #For Search
from customers.models import Address

class AddressIndex(indexes.SearchIndex, indexes.Indexable):
   '''
   When you choose a document=True field, it should be consistently named across all of your
   SearchIndex classes to avoid confusing 
   the backend. The convention is to name this field 'text'
   '''
   text = indexes.CharField(document=True, use_template=True) #primary field for searching within
   city = indexes.CharField(model_attr='city')
   timestamp = indexes.DateTimeField(model_attr='timestamp')   
   
   def get_model(self):
      return Address

   def index_queryset(self, using=None):
      """Used when the entire index for Address is updated."""
      return self.get_model().objects.filter(timestamp__lte=datetime.datetime.now())
