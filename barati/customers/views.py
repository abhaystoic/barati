#Ignore pylint whitespace warning
# pylint: disable=W0311

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from django.db import connection, transaction
from django.db.models import Sum
from django.template.defaulttags import register
from customers import models as m
import sys, json

#@login_required(login_url='/auth/login/')
class Dashboard(View):
   try:
      def __init__(self):
         self.template_name = 'customers/index.html'
         
      def get_context_data(self, **kwargs):
         query = "select id, name from venue_types"
         venue_types = m.Venue_Types.objects.raw(query)
         
         query = "select id, name from card_types"
         card_types = m.Card_Types.objects.raw(query)
         
         query = "select id, name from beautician_types"
         beautician_types = m.Beautician_Types.objects.raw(query)
         
         query = "select id, name from music_types"
         music_types = m.Music_Types.objects.raw(query)
         
         query = "select id, name from gift_types"
         gift_types = m.Gift_Types.objects.raw(query)
         
         query = "select id, name from photo_types"
         photo_types = m.Photo_Types.objects.raw(query)
         
         query = "select id, name from video_types"
         video_types = m.Video_Types.objects.raw(query)
         
         query = "select id, name from bakery_types"
         bakery_types = m.Bakery_Types.objects.raw(query)
         
         query = "select id, name from ghodi_bagghi_types"
         ghodi_bagghi_types = m.Ghodi_Bagghi_Types.objects.raw(query)
         
         query = "select id, name from band_types"
         band_types = m.Band_Types.objects.raw(query)
         
         query = "select id, name from mehendi_types"
         mehendi_types = m.Mehendi_Types.objects.raw(query)
         
         query = "select id, name from fireworks_types"
         fireworks_types = m.Fireworks_Types.objects.raw(query)
         
         query = "select id, name from tent_types"
         tent_types = m.Tent_Types.objects.raw(query)
         
         context = {\
         'venue_types' : venue_types, 'card_types' : card_types, 'beautician_types' : beautician_types,\
         'gift_types' : gift_types, 'photo_types' : photo_types,\
         'video_types' : video_types, 'bakery_types' : bakery_types, 'ghodi_bagghi_types' : ghodi_bagghi_types,\
         'band_types' : band_types, 'mehendi_types' : mehendi_types, 'fireworks_types' : fireworks_types,\
         'tent_types' : tent_types, 'music_types' : music_types \
         }
         return context
         
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         context_dict = self.get_context_data()
         return render(request, self.template_name, context_dict)   
   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno


def get_categories():
   categories = ('venues', 'cards', 'beauticians', 'gifts', 'photo_videos', 'bakeries', 'ghodi_bagghis', 'bands', 'mehendis', 'fireworks', 'tents', 'music')
   return categries
      


#@login_required(login_url='/auth/login/')
class Venue(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/venue.html'

      def get_context_data(self, **kwargs):
         context = super(Venue, self).get_context_data(**kwargs)
         return context

      def get_queryset(self, **kwargs): 
         #type = self.kwargs['type']
         query = "select id, name from venue_types"
         self.venue_subcategories = m.Venue_Types.objects.raw(query)
         return self.venue_subcategories
         
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         print self.get_context_data()
         subcategories = self.get_context_data()['venue_types']
         context_dict = {'subcategories' : subcategories}
         context_dict.update(self.get_context_data())
         return render(request, self.template_name, context_dict)   
      
      '''
      Save something back to DB
       def get_object(self):
          # Call the superclass
          object = super(AuthorDetailView, self).get_object()
          # Record the last accessed date
          object.last_accessed = timezone.now()
          object.save()
          # Return the object
          return object
      '''
      
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno

 
#@login_required(login_url='/auth/login/')
class Card(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/card.html'

      def get_context_data(self, **kwargs):
         context = super(Card, self).get_context_data(**kwargs)
         
         return context

      def get_queryset(self, **kwargs):
         query = "select id, name from card_types"
         self.card_subcategories = m.Card_Types.objects.raw(query)
         return self.card_subcategories
         
      def get_cards(self, **kwargs):
         type = self.kwargs['type']
         query = "select id, name from cards where type_id = " + type
         self.cards = m.Cards.objects.raw(query)
         return self.cards

      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         subcategories = self.get_context_data()['card_types']
         cards = self.get_cards()
         context_dict = {'subcategories' : subcategories, 'cards' : cards}
         context_dict.update(self.get_context_data())
         return render(request, self.template_name, context_dict)   

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno


#@login_required(login_url='/auth/login/')
class Card_Details(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/card_details.html'

      def get_context_data(self, **kwargs):
         context = super(Card_Details, self).get_context_data(**kwargs)
         return context
      
      def get_queryset(self, **kwargs):
         query = "select id, name from card_types"
         self.card_subcategories = m.Card_Types.objects.raw(query)
         return self.card_subcategories
         
      def get_card_details(self, **kwargs):
         query = "select id, name from cards where id = " + str(self.kwargs['card_id'])
         self.card_details = m.Cards.objects.raw(query)
         return self.card_details

      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         subcategories = self.get_context_data()['card_types']
         card_details = self.get_card_details()
         context_dict = {'subcategories' : subcategories, 'card_details' : card_details}
         context_dict.update(self.get_context_data())
         
         return render(request, self.template_name, context_dict)   

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno


#@login_required(login_url='/auth/login/')
def product_details(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/product_details.html', context_dict, context_instance=context)

#@login_required(login_url='/auth/login/')
def blog(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/blog.html', context_dict, context_instance=context)

#@login_required(login_url='/auth/login/')
class Cart(Dashboard, View):
   try:
      def __init__(self):
         self.cursor = connection.cursor()
         self.template_name = 'customers/cart.html'

      def get_context_data(self, **kwargs):
         context = super(Cart, self).get_context_data(**kwargs)
         return context

      def get_queryset(self, **kwargs):
         query_cart = "select distinct on (ref_id) id, ref_id from cart where user_id = 1"

         self.cart = m.Cart.objects.raw(query_cart)
         self.card_list = []
         self.venue_list = []
         self.beautician_list = []
         self.music_list = []
         self.gift_list = []
         self.photo_video_list = []
         self.bakery_list = []
         self.ghodi_bagghi_list = []
         self.band_list = []
         self.mehendi_list = []
         self.fireworks_list = []
         self.tent_house_list = []

         for product in self.cart:
            #Get the details
            query_prod = "select * from " + str(product.product_type) + " where ref_id = '" + str(product.ref_id) + "'"
            
            if str(product.product_type) == "cards":
               self.card_list.append(m.Cards.objects.get(ref_id = str(product.ref_id)))

            if str(product.product_type) == "venues":
               self.venue_list.append(m.Venues.objects.get(ref_id = str(product.ref_id)))

            if str(product.product_type) == "beauticians":
               self.beautician_list.append(m.Beauticians.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "music":
               self.music_list.append(m.Music.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "gifts":
               self.gift_list.append(m.Gifs.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "photos_videos":
               self.photo_video_list.append(m.Photos_Videos.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "bakeries":
               self.bakery_list.append(m.Bakeries.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "ghodis_bagghis":
               self.ghodi_bagghi_list.append(m.Ghodis_Bagghi.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "bands":
               self.band_list.append(m.Bands.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "mehendi":
               self.mehendi_list.append(m.Mehendi.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "fireworks":
               self.fireworks_list.append(m.Fireworks.objects.get(ref_id = str(product.ref_id)))
         
         self.cart_sub_total = m.Cart.objects.filter(user_id = 1).aggregate(cart_sub_total = Sum('total_price'))
         self.tax = self.cart_sub_total['cart_sub_total'] * 0.10
         self.grand_total = float(self.tax) + float(self.cart_sub_total['cart_sub_total'])
         
         self.prod_dict = {'card_list' : self.card_list, 'venue_list' : self.venue_list, 'beautician_list' : self.beautician_list, \
            'music_list' : self.music_list, 'gift_list' : self.gift_list, 'photo_video_list' : self.photo_video_list, \
            'bakery_list' : self.bakery_list, 'ghodi_bagghi_list' : self.ghodi_bagghi_list, 'band_list' : self.band_list, \
            'mehendi_list' : self.mehendi_list, 'fireworks_list' : self.fireworks_list, \
            'cart_sub_total' : self.cart_sub_total['cart_sub_total'], 'tax' : self.tax, 'grand_total' : self.grand_total}
         return self.prod_dict
         
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         context_dict = self.get_queryset()
         context_dict.update(self.get_context_data())
         return render(request, self.template_name, context_dict)   
   
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno


#A function based view for adding a product in the cart. Returns json data and doesn't refresh the page
#@login_required(login_url='/auth/login/')
def add_to_cart(request, ref_id):
   cursor = connection.cursor()
   context_dict = {}
   message = ""
   try:
      context = RequestContext(request)
      product_type = request.POST.get('product_type')
      user_id = request.POST.get('user_id')
      price = int(request.POST.get('price'))
      quantity = int(request.POST.get('quantity'))
      total_price = quantity * price
      checked_out = "false"
      query = "INSERT INTO cart(ref_id, product_type, checked_out, user_id, quantity, total_price) VALUES( '%s', '%s', %s, %d, %d, %d)"\
      %(str(ref_id), str(product_type), str(checked_out), int(user_id), int(quantity), int(total_price))
      cursor.execute(query)
      transaction.commit()
      message = "successfully added in cart"
   except Exception as general_exception:
      message = str(general_exception)
      print general_exception
      print sys.exc_traceback.tb_lineno
   return HttpResponse(json.dumps(message))

#@login_required(login_url='/auth/login/')
def checkout(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/checkout.html', context_dict, context_instance=context)         
   
#@login_required(login_url='/auth/login/')
def shop(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/shop.html', context_dict, context_instance=context)   
   
#@login_required(login_url='/auth/login/')
def contact_us(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/contact_us.html', context_dict, context_instance=context)

#A Filter for enabling the usage of a dictionary in the templates
@register.filter(name = 'get_item') 
def get_item(dictionary, key):
   try:
      value = dictionary.get(key) #Using '.get' To suppress key error (just in case)
      return value
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return "not_found"

#Filter for cart
@register.filter(name = 'get_pic_path') 
def get_pic_path(key):
   try:
      value = m.Product_Pictures.objects.get(ref_id = key).picture_path #Using '.get' To suppress key error (just in case)
      return value
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return "not_found"

#Filter for cart
@register.filter(name = 'get_quantity') 
def get_quantity(key):
   try:
      total_quantity = 0
      quantities = m.Cart.objects.filter(ref_id = key)
      for quantity in quantities:
         total_quantity = total_quantity + quantity.quantity
      return total_quantity
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return 0

#Filter for cart
@register.filter(name = 'get_total_price')
def get_total_price(key):
   try:
      cart = m.Cart.objects.filter(ref_id = key).aggregate(sum_total = Sum('total_price'))
      return cart['sum_total']
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return 0

#A Filter for mulitplication
@register.filter(name = 'multiply')
def multiply(first, second):
   try:
      value = first * second
      return value
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return "not_found"
