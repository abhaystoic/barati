'''
Haystack Searching
This program indexes the specific attributes we want to provide search functionalities on
'''
import datetime
from haystack import indexes #For Search
from customers.models import Address, Cards, Beauticians, Venues

class AddressIndex(indexes.SearchIndex, indexes.Indexable):
   '''
   When you choose a document=True field, it should be consistently named across all of your
   SearchIndex classes to avoid confusing 
   the backend. The convention is to name this field 'text'
   '''
   text = indexes.CharField(document=True, use_template=True) #primary field for searching within
   #locality = indexes.CharField(model_attr='locality')
   timestamp = indexes.DateTimeField(model_attr='timestamp')
   #For autocomplete
   locality = indexes.EdgeNgramField(model_attr='locality')
   
   def get_model(self):
      return Address

   def index_queryset(self, using=None):
      """Used when the entire index for Address is updated."""
      return self.get_model().objects.filter(timestamp__lte=datetime.datetime.now())

   def prepare_locality(self, obj):
      return "%s" %(obj.locality)

class CardIndex(indexes.SearchIndex, indexes.Indexable):
   '''
   When you choose a document=True field, it should be consistently named across all of your
   SearchIndex classes to avoid confusing 
   the backend. The convention is to name this field 'text'
   '''
   text = indexes.CharField(document=True, use_template=True) #primary field for searching within
   timestamp = indexes.DateTimeField(model_attr='timestamp')
   #For autocomplete
   name_card = indexes.EdgeNgramField(model_attr='name')
   type = indexes.EdgeNgramField(model_attr='type')
   
   def get_model(self):
      return Cards

   def index_queryset(self, using=None):
      """Used when the entire index for Card is updated."""
      return self.get_model().objects.filter(timestamp__lte=datetime.datetime.now())

class BeauticianIndex(indexes.SearchIndex, indexes.Indexable):
   '''
   When you choose a document=True field, it should be consistently named across all of your
   SearchIndex classes to avoid confusing 
   the backend. The convention is to name this field 'text'
   '''
   text = indexes.CharField(document=True, use_template=True) #primary field for searching within
   timestamp = indexes.DateTimeField(model_attr='timestamp')
   #For autocomplete
   name_beautician = indexes.EdgeNgramField(model_attr='name')
   type = indexes.EdgeNgramField(model_attr='type')
   
   def get_model(self):
      return Beauticians

   def index_queryset(self, using=None):
      """Used when the entire index for Beautician is updated."""
      return self.get_model().objects.filter(timestamp__lte=datetime.datetime.now())
      
class VenueIndex(indexes.SearchIndex, indexes.Indexable):
   '''
   When you choose a document=True field, it should be consistently named across all of your
   SearchIndex classes to avoid confusing 
   the backend. The convention is to name this field 'text'
   '''
   text = indexes.CharField(document=True, use_template=True) #primary field for searching within
   timestamp = indexes.DateTimeField(model_attr='timestamp')
   #For autocomplete
   name_venue = indexes.EdgeNgramField(model_attr='name')
   type = indexes.EdgeNgramField(model_attr='type')
   
   def get_model(self):
      return Venues

   def index_queryset(self, using=None):
      """Used when the entire index for Venue is updated."""
      return self.get_model().objects.filter(timestamp__lte=datetime.datetime.now())
