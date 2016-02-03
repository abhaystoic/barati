from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json, datetime, os

class Submit_Product(View):
   try:
      def __init__(self):
         self.template_name = 'vendors/list_product.html'
         
      def convert_to_float(self, value):
         if value:
            return float(value)
         else:
            return None
      
      def convert_to_string(self, value):
         if value:
            return str(value)
         else:
            return None
      
      def convert_to_int(self, value):
         if value:
            return int(value)
         else:
            return None
      
      def convert_to_boolean(self, value):
         if value == 'yes':
            return True
         else:
            return False
      
      def post(self, request):
         context_dict = {}
         orders_list = []
         count = 0
         ref_id_prefix = ''
         user = m.Users.objects.get(username=request.user.username)
         vendor = m.Vendors.objects.get(user_id=user.id)
         ref_id = self.convert_to_string(request.POST.get('product_id'))
         
         #Validate ref_id
         product_type = self.convert_to_string(request.POST.get('product_type'))
         
         #Fields common to all types
         name = self.convert_to_string(request.POST.get('product_name'))
         short_description = self.convert_to_string(request.POST.get('product_short_description'))
         long_description = self.convert_to_string(request.POST.get('product_long_description'))
         actual_price = self.convert_to_float(request.POST.get('product_actual_price'))
         
         #Saving the concerned address
         address = m.Address()
         address.building_number = self.convert_to_string(request.POST.get('product_building_number'))
         address.street = self.convert_to_string(request.POST.get('product_street'))
         address.locality = self.convert_to_string(request.POST.get('product_locality'))
         address.landmark = self.convert_to_string(request.POST.get('product_landmark'))
         address.city = self.convert_to_string(request.POST.get('product_city'))
         address.state = self.convert_to_string(request.POST.get('product_state'))
         address.country = self.convert_to_string(request.POST.get('product_country'))
         address.zipcode = self.convert_to_string(request.POST.get('product_zipcode'))
         address.save()
         
         #Catching the venue details
         if product_type == 'venue':
            new_venue = m.Venues()
            ref_id_prefix = 'VEN_'
            new_venue.ref_id = ref_id_prefix + ref_id
            new_venue.vendor = vendor
            new_venue.name = name
            new_venue.actual_price = actual_price
            new_venue.short_description = short_description
            new_venue.long_description = long_description
            new_venue.type = m.Venue_Types.objects.get(name=self.convert_to_string(request.POST.get('product_venue_type')))
            new_venue.address = address
            new_venue.max_capacity = self.convert_to_int(request.POST.get('product_max_capacity'))
            new_venue.accomodation_available = self.convert_to_boolean(request.POST.get('product_accomodation_available'))
            new_venue.number_of_rooms = self.convert_to_int(request.POST.get('product_number_of_rooms'))
            new_venue.per_room_per_day_cost = self.convert_to_float(request.POST.get('per_room_per_day_cost'))
            new_venue.room_details = self.convert_to_string(request.POST.get('product_room_details'))
            new_venue.food_types = self.convert_to_string(request.POST.get('product_food_types'))
            new_venue.per_plate_cost_veg = self.convert_to_float(request.POST.get('product_per_plate_cost_veg'))
            new_venue.per_plate_cost_nonveg = self.convert_to_float(request.POST.get('product_per_plate_cost_nonveg'))
            new_venue.outside_catering_allowed = self.convert_to_boolean(request.POST.get('product_outside_catering_allowed'))
            new_venue.alcohol_serving = self.convert_to_boolean(request.POST.get('product_alcohol_serving'))
            new_venue.outside_decoration_allowed = self.convert_to_boolean(request.POST.get('product_outside_decoration_allowed'))
            new_venue.function_types = self.convert_to_string(request.POST.get('product_function_types'))
            new_venue.valet_parking = self.convert_to_boolean(request.POST.get('product_valet_parking'))
            new_venue.parking_capacity_4_wheelers = self.convert_to_int(request.POST.get('product_parking_capacity_4_wheelers'))
            new_venue.parking_capacity_2_wheelers = self.convert_to_int(request.POST.get('product_parking_capacity_2_wheelers'))
            new_venue.generator_available = self.convert_to_boolean(request.POST.get('product_generator_available'))
            new_venue.generator_cost_type = self.convert_to_string(request.POST.get('product_generator_cost_type'))
            new_venue.generator_cost = self.convert_to_float(request.POST.get('product_generator_cost'))
            new_venue.generator_details = self.convert_to_string(request.POST.get('product_generator_details'))
            new_venue.audio_video_equipment_details = self.convert_to_string(request.POST.get('product_audio_video_equipment_details'))
            new_venue.wheelchair_accessibility = self.convert_to_string(request.POST.get('product_wheel_chair_accessibility'))
            new_venue.stage_details = self.convert_to_string(request.POST.get('product_stage_details'))
            new_venue.cutlery_and_crockery_details = self.convert_to_string(request.POST.get('product_cutlery_and_crockery_details'))
            new_venue.service_staff_details = self.convert_to_string(request.POST.get('product_service_staff_details'))
            new_venue.save()
            
         #Catching the card details
         if product_type == 'card':
            new_card = m.Cards()
            ref_id_prefix = 'CRD_'
            new_card.ref_id = ref_id_prefix + ref_id
            new_card.vendor = vendor
            new_card.name = name
            new_card.actual_price = actual_price
            new_card.printing_price = self.convert_to_float(request.POST.get('product_printing_price'))
            new_card.short_description = short_description
            new_card.long_description = long_description
            new_card.address = address
            new_card.type = m.Card_Types.objects.get(name=str(request.POST.get('product_card_type')))
            new_card.min_numbers = self.convert_to_int(request.POST.get('product_card_min_numbers'))
            new_card.max_numbers = self.convert_to_int(request.POST.get('product_card_max_numbers'))
            new_card.length =self.convert_to_float( request.POST.get('product_card_length'))
            new_card.width = self.convert_to_float(request.POST.get('product_card_width'))
            new_card.weight = self.convert_to_float(request.POST.get('product_card_weight'))
            new_card.save()
         
         #Catching the beautician details
         if product_type == 'beautician':
            new_beautician = m.Beauticians()
            ref_id_prefix = 'BTN_'
            new_beautician.ref_id = ref_id_prefix + ref_id
            new_beautician.vendor = vendor
            new_beautician.name = name
            new_beautician.actual_price = actual_price
            new_beautician.short_description = short_description
            new_beautician.long_description = long_description
            new_beautician.address = address
            new_beautician.type = m.Beautician_Types.objects.get(name=str(request.POST.get('product_beautician_type')))
            new_beautician.gender = self.convert_to_string(request.POST.get('product_beautician_gender'))
            new_beautician.services = self.convert_to_string(request.POST.get('product_beautician_services'))
            new_beautician.female_person_available = self.convert_to_boolean(request.POST.get('product_female_person_available'))
            new_beautician.home_visit_charge = self.convert_to_float(request.POST.get('product_beautician_home_visit_charge'))
            new_beautician.home_visit_policy = self.convert_to_string(request.POST.get('product_beautician_home_visit_policy'))
            new_beautician.save()
         
         main_photos = request.FILES.getlist('product_photos')
         #Saving the main pictures
         for a_file in main_photos:
            count = count + 1
            product_picture = m.Product_Pictures(name=(ref_id_prefix + str(ref_id) + '_' + str(count)), ref_id=ref_id, picture=a_file, picture_path=os.path.join((str(product_type) + 's'), str(ref_id)))
            product_picture.save()
         
         #re-initializing counter
         count = 0
         more_photos = request.FILES.getlist('product_more_photos')         
         #Saving additional pictures
         for a_file in more_photos:
            count = count + 1
            product_picture = m.Product_Pictures(name=(str(ref_id) + '_additional_' + str(count)), ref_id=ref_id, picture=a_file, picture_path=os.path.join((str(product_type) + 's'), str(ref_id)))
            product_picture.save()
         
         message = "success_submit_product"
         return HttpResponse(json.dumps(message))
         #context_dict = {'message' : message}
         #return render(request, self.template_name, context_dict)
   except Exception as e:
      print e
      print sys.exc_traceback.tb_lineno
