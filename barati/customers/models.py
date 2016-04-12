from django.db import models
from django.core.validators import RegexValidator #For phone number validation
import os



class Users(models.Model):
   id = models.AutoField(primary_key=True)
   username = models.CharField(max_length=50, unique=True)
   ROLE_CHOICES = (
      ('customer', 'customer'),
      ('vendor', 'vendor'),
      ('admin', 'admin'),
   )
   role = models.CharField(choices=ROLE_CHOICES, max_length=10)
   WHAT_ARE_YOU_CHOICES = (
      ('bride', 'bride'),
      ('groom', 'groom'),
      ('family', 'family'),
      ('friend', 'friend'),
   )
   what_are_you = models.CharField(choices=WHAT_ARE_YOU_CHOICES, max_length=10, blank=True, null=True)
   first_name = models.CharField(max_length=50, blank=True, null=True)
   middle_name = models.CharField(max_length=100, blank=True, null=True)
   last_name = models.CharField(max_length=50, blank=True, null=True)
   #religion = models.ForeignKey(Religion, blank=True, null=True)
   email = models.EmailField(max_length=100, blank=True, null=True)
   phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
   contact1 = models.CharField(validators=[phone_regex], max_length=50, blank=True, null=True) # validators should be a list
   contact2 = models.CharField(validators=[phone_regex], max_length=50, blank=True, null=True) # validators should be a list
   contact3 = models.CharField(validators=[phone_regex], max_length=50, blank=True, null=True) # validators should be a list
   #user = models.ForeignKey(auth_user, blank=True, null=True)
   
   class Meta:
      managed = True
      db_table = 'users'
   def __unicode__(self):
      return unicode(self.username)

class Religion(models.Model):
   Religion_CHOICES=(
      ("Hinduism","Hinduism"),("Sikhism","Sikhism"),
      ("Buddhism","Buddhism"),("Jainism","Jainism"),
      ("Islam","Islam"),("Christianity","Christianity"), ("Other","Other")
      )
   id = models.AutoField(primary_key=True)
   religion= models.CharField(choices=Religion_CHOICES,max_length=50)
   users=models.ForeignKey(Users, blank=True, null=True)
   class Meta:
      managed = True
      db_table = 'religion'
   def __unicode__(self):
      return unicode(self.name)

class Address(models.Model):
   id = models.AutoField(primary_key=True)
   TYPE_CHOICES = (
      ('delivery', 'delivery'),
      ('vendor', 'vendor'),
      ('customer', 'customer'),
   )

   state_choices=( ("Andhra Pradesh", "Andhra Pradesh"),
   ("Arunachal Pradesh", "Arunachal Pradesh"),
   ("Assam","Assam"),( "Bihar", "Bihar"),( "Chhattisgarh", "Chhattisgarh"),
   ("Goa", "Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),( "Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir","Jammu and Kashmir"),("Jharkhand","Jharkhand"),
    ("Karnataka", "Karnataka"),("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),("Odisha","Odisha") ,("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),
    ("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"))
   type = models.CharField(choices=TYPE_CHOICES, max_length=10)
   building_number = models.CharField(max_length=50, blank=True, null=True)
   street = models.CharField(max_length=100, blank=True, null=True)
   locality = models.CharField(max_length=50, blank=True, null=True)
   landmark = models.CharField(max_length=50, blank=True, null=True)
   city = models.CharField(max_length=50, blank=True, null=True)
   state = models.CharField(max_length=50, blank=True, null=True,choices=state_choices)
   country = models.CharField(max_length=50, blank=True, null=True)
   zipcode = models.CharField(max_length=50, blank=True, null=True)
   timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
   users=models.ForeignKey(Users, blank=True, null=True)
   class Meta:
      managed = True
      db_table = 'address'
   def __unicode__(self):
      return_string = (str(self.building_number) if self.building_number != None else '') + ' ' + \
         (str(self.street) if self.street != None else '') + ' ' + (str(self.locality) if self.locality != None else '')
      return unicode(return_string)

class Main_Preferences(models.Model):
   id = models.AutoField(primary_key=True)
   user = models.ForeignKey(Users)
   date = models.DateField(blank=True, null=True)
   location = models.CharField(max_length=50, blank=True, null=True)
   sublocation = models.CharField(max_length=50, blank=True, null=True)
   
   class Meta:
      managed = True
      db_table = 'main_preferences'
   def __unicode__(self):
      return unicode(self.name)

class Budget(models.Model):
   id = models.AutoField(primary_key=True)
   user = models.ForeignKey(Users)
   min_master = models.FloatField(blank=True, null=True)
   max_master = models.FloatField(blank=True, null=True)
   min_venue = models.FloatField(blank=True, null=True)
   max_venue = models.FloatField(blank=True, null=True)
   min_card = models.FloatField(blank=True, null=True)
   max_card = models.FloatField(blank=True, null=True)
   min_beautician = models.FloatField(blank=True, null=True)
   max_beautician = models.FloatField(blank=True, null=True)
   min_mehendi = models.FloatField(blank=True, null=True)
   max_mehendi = models.FloatField(blank=True, null=True)
   min_music = models.FloatField(blank=True, null=True)
   max_music = models.FloatField(blank=True, null=True)
   min_gift = models.FloatField(blank=True, null=True)
   max_gift = models.FloatField(blank=True, null=True)
   min_tent = models.FloatField(blank=True, null=True)
   max_tent = models.FloatField(blank=True, null=True)
   
   class Meta:
      managed = True
      db_table = 'budget'
   def __unicode__(self):
      return unicode(self.name)
      
class Vendors(models.Model):
   id = models.AutoField(primary_key=True)
   user = models.ForeignKey(Users)
   name = models.CharField(max_length=100, unique=True)
   address = models.ForeignKey(Address, blank=True, null=True)
   official_email = models.EmailField(max_length=100, blank=True, null=True)
   phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
   contact1 = models.CharField(validators=[phone_regex], max_length=50, blank=True, null=True) # validators should be a list
   contact2 = models.CharField(validators=[phone_regex], max_length=50, blank=True, null=True) # validators should be a list
   contact3 = models.CharField(validators=[phone_regex], max_length=50, blank=True, null=True) # validators should be a list
   
   class Meta:
      managed = True
      db_table = 'vendors'
   def __unicode__(self):
      return unicode(self.name)

class Vendor_Cordinators(models.Model):
   id = models.AutoField(primary_key=True)
   vendor_id = models.ForeignKey(Vendors, blank=True, null=True)
   coordinator_name = models.CharField(max_length=100, unique=True)
   email = models.EmailField(max_length=100, blank=True, null=True)
   phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
   contact1 = models.CharField(validators=[phone_regex], max_length=50, blank=True) # validators should be a list
   contact2 = models.CharField(validators=[phone_regex], max_length=50, blank=True) # validators should be a list
   contact3 = models.CharField(validators=[phone_regex], max_length=50, blank=True) # validators should be a list
   
   class Meta:
      managed = True
      db_table = 'vendor_coordinators'
   def __unicode__(self):
      return unicode(self.coordinator_name)
  
class Venue_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'venue_types'
   def __unicode__(self):
      return unicode(self.name)

class Card_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'card_types'
   def __unicode__(self):
      return unicode(self.name)

class Beautician_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'beautician_types'
   def __unicode__(self):
      return unicode(self.name)


class Music_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'music_types'
   def __unicode__(self):
      return unicode(self.name)

class Gift_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'gift_types'
   def __unicode__(self):
      return unicode(self.name)
      
class Photo_Video_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'photo_video_types'
   def __unicode__(self):
      return unicode(self.name)

class Bakery_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'bakery_types'
   def __unicode__(self):
      return unicode(self.name)

class Ghodi_Bagghi_Types(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'ghodi_bagghi_types'
   def __unicode__(self):
      return unicode(self.name)

class Band_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'band_types'
   def __unicode__(self):
      return unicode(self.name)

class Mehendi_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'mehendi_types'
   def __unicode__(self):
      return unicode(self.name)

class Fireworks_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'fireworks_types'
   def __unicode__(self):
      return unicode(self.name)

class Tent_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'tent_types'
   def __unicode__(self):
      return unicode(self.name)

class Videos(models.Model):
   id = models.AutoField(primary_key=True)
   vendor_id = models.ForeignKey(Vendors, blank=True, null=True)
   ref_id = models.CharField(max_length=100)
   video_name = models.CharField(max_length=50)
   video_link = models.CharField(max_length=100)
   
   class Meta:
      managed = True
      db_table = 'videos'
   def __unicode__(self):
      return unicode(self.ref_id)
      
class Venues(models.Model):
   id = models.AutoField(primary_key=True)
   ref_id = models.CharField(max_length=100, unique=True)
   vendor = models.ForeignKey(Vendors)
   name = models.CharField(max_length=100)
   type = models.ForeignKey(Venue_Types, blank=True, null=True)
   address = models.ForeignKey(Address, blank=True, null=True)
   short_description = models.CharField(max_length=100)
   long_description = models.CharField(max_length=800)
   max_capacity = models.IntegerField()
   accomodation_available = models.NullBooleanField()
   rooms_details = models.CharField(max_length=800, blank=True, null=True)
   number_of_rooms = models.IntegerField(blank=True, null=True)
   per_room_per_day_cost = models.FloatField(blank=True, null=True)
   actual_price = models.FloatField()
   discount_perc = models.FloatField(blank=True, null=True)
   discount_rs = models.FloatField(blank=True, null=True)
   discounted_price = models.FloatField(blank=True, null=True)
   food_types = models.CharField(max_length=800, blank=True, null=True)
   per_plate_cost_veg = models.FloatField(blank=True, null=True)
   per_plate_cost_nonveg = models.FloatField(blank=True, null=True)
   outside_catering_allowed = models.NullBooleanField()
   alcohol_serving = models.NullBooleanField()
   outside_decoration_allowed = models.NullBooleanField()
   function_types = models.CharField(max_length=800, blank=True, null=True)
   valet_parking = models.NullBooleanField()
   parking_capacity_4_wheelers = models.IntegerField(blank=True, null=True)
   parking_capacity_2_wheelers = models.IntegerField(blank=True, null=True)
   generator_available = models.NullBooleanField()
   generator_cost_type = models.CharField(max_length=50, blank=True, null=True) #included or excluded
   generator_cost = models.FloatField(blank=True, null=True)
   generator_details = models.CharField(max_length=800, blank=True, null=True)
   audio_video_equipment_details = models.CharField(max_length=800, blank=True, null=True)
   wheelchair_accessibility = models.CharField(max_length=50, blank=True, null=True)
   stage_details = models.CharField(max_length=800, blank=True, null=True)
   cutlery_and_crockery_details = models.CharField(max_length=800, blank=True, null=True)   
   service_staff_details = models.CharField(max_length=800, blank=True, null=True)
   timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
   
   class Meta:
      managed = True
      db_table = 'venues'
   def __unicode__(self):
      return unicode(self.name)

class Cards(models.Model):
   id = models.AutoField(primary_key=True)
   ref_id = models.CharField(max_length=100, unique=True)
   vendor = models.ForeignKey(Vendors)
   name = models.CharField(max_length=100)
   address = models.ForeignKey(Address, blank=True, null=True)
   type = models.ForeignKey(Card_Types, blank=True, null=True)
   short_description = models.CharField(max_length=100)
   long_description = models.CharField(max_length=800)
   min_numbers = models.IntegerField()
   max_numbers = models.IntegerField()
   actual_price = models.FloatField()
   printing_price = models.FloatField(blank=True, null=True)
   discount_perc = models.FloatField(blank=True, null=True)
   discount_rs = models.FloatField(blank=True, null=True)
   discounted_price = models.FloatField(blank=True, null=True)
   length = models.FloatField(blank=True, null=True)
   width = models.FloatField(blank=True, null=True)
   weight = models.FloatField(blank=True, null=True)
   barati_confidence_perc = models.FloatField(blank=True, null=True)
   timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
   
   class Meta: 
      managed = True
      db_table = 'cards'
   def __unicode__(self):
      return unicode(self.ref_id)

#will also be used for card content      
class Cards_Preferences(models.Model):
   id = models.AutoField(primary_key=True)
   card = models.ForeignKey(Cards)
   ref_id = models.CharField(max_length=100)
   avail_printing = models.NullBooleanField(blank=True)
   user = models.ForeignKey(Users, blank=True, null=True)   
   
   class Meta: 
      managed = True
      db_table = 'cards_preferences'
   def __unicode__(self):
      return unicode(self.ref_id)

class Card_Colors(models.Model):
   id = models.AutoField(primary_key=True)
   card = models.ForeignKey(Cards, blank=True, null=True)
   ref_id = models.CharField(max_length=100,blank=True, null=True)
   color = models.CharField(max_length=20, blank=True, null=True)
   hexcode = models.CharField(max_length=7, blank=True, null=True)

   class Meta: 
      managed = True
      db_table = 'card_colors'
   def __unicode__(self):
      return unicode(self.card)
      
class Card_Deities(models.Model):
   id = models.AutoField(primary_key=True)
   card = models.ForeignKey(Cards, blank=True, null=True)
   ref_id = models.CharField(max_length=100, blank=True, null=True)
   top_deity_image_path = models.CharField(max_length=200, blank=True, null=True)
   top_deity_name = models.CharField(max_length=30, blank=True, null=True)
   inner_deity_image_path = models.CharField(max_length=200, blank=True, null=True)
   inner_deity_name = models.CharField(max_length=30, blank=True, null=True)
   
   class Meta: 
      managed = True
      db_table = 'card_deities'
   def __unicode__(self):
      return unicode(self.card)      

class Beauticians(models.Model):
   id = models.AutoField(primary_key=True)
   ref_id = models.CharField(max_length=100, unique=True)
   vendor = models.ForeignKey(Vendors)
   name = models.CharField(max_length=100)
   address = models.ForeignKey(Address, blank=True, null=True)
   type = models.ForeignKey(Beautician_Types, blank=True, null=True)
   GENDER_CHOICES = (
      ('male', 'male'),
      ('female', 'female'),
      ('neutral', 'neutral'),
   )
   gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
   short_description = models.CharField(max_length=100, blank=True, null=True)
   long_description = models.CharField(max_length=800, blank=True, null=True)
   services = models.CharField(max_length=800, blank=True, null=True)
   actual_price = models.FloatField()
   discount_perc = models.FloatField(blank=True, null=True)
   discount_rs = models.FloatField(blank=True, null=True)
   discounted_price = models.FloatField(blank=True, null=True)
   female_person_available = models.NullBooleanField(blank=True)
   home_visit_charge = models.FloatField(blank=True, null=True)
   home_visit_policy = models.CharField(max_length=800, blank=True, null=True)
   barati_confidence_perc = models.FloatField(blank=True, null=True)
   timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
   
   class Meta: 
      managed = True
      db_table = 'beauticians'
   def __unicode__(self):
      return unicode(self.ref_id)

class Cart(models.Model):
   id = models.AutoField(primary_key=True)
   ref_id = models.CharField(max_length=100)
   user = models.ForeignKey(Users)
   product_type = models.CharField(max_length=50)
   checked_out = models.BooleanField(default=False)
   quantity = models.IntegerField(blank=True, null=True)
   total_price = models.FloatField(blank=True, null=True)
   
   class Meta: 
      managed = True
      db_table = 'cart'
   def __unicode__(self):
      return unicode(self.ref_id)

def get_image_path(instance, filename):
   return os.path.join(str(instance.picture_path), filename)

#To store paths of the pictures on the server      
class Product_Pictures(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100, blank=True, null=True, unique=True)
   ref_id = models.CharField(max_length=100, blank=True, null=True)
   picture_path = models.CharField(max_length=200, blank=True, null=True)
   picture = models.FileField(upload_to=get_image_path, blank=True, null=True)
   class Meta: 
      managed = True
      db_table = 'product_pictures'
   def __unicode__(self):
      return unicode(self.ref_id)
      
class Orders(models.Model):
   order_id = models.AutoField(primary_key=True)
   user = models.ForeignKey(Users, blank=True, null=True)
   vendor = models.ForeignKey(Vendors, blank=True, null=True)
   ref_id = models.CharField(max_length=100)
   quantity = models.IntegerField(blank=True, null=True)
   total_price = models.FloatField(blank=True, null=True)
   package_id = models.CharField(max_length=100, unique=True)
   vendor_acknowledgement = models.CharField(max_length=51)
   payment_done = models.BooleanField(default = False)
   payment_received = models.BooleanField(default = False)
   payment_method = models.CharField(max_length=100, blank=True, null=True)
   product_type = models.CharField(max_length=100, blank=True, null=True)
   timestamp = models.DateTimeField(auto_now_add=True)
   last_status_time = models.DateTimeField(blank=True, null=True)
   comment = models.CharField(max_length=500, blank=True, null=True)
   address = models.ForeignKey(Address, blank=True, null=True)
   
   class Meta: 
      managed = True
      db_table = 'orders'
   def __unicode__(self):
      return unicode(self.ref_id)

class Delivery_Status(models.Model):
   id = models.AutoField(primary_key=True)
   ref_id = models.CharField(max_length=100, blank=True, null=True)
   name = models.CharField(max_length=100, blank=True, null=True)
   status = models.CharField(max_length=100, blank=True, null=True)
   link = models.CharField(max_length=200, blank=True, null=True)
   timestamp = models.DateTimeField(auto_now_add=True)
   order = models.ForeignKey(Orders, blank=True, null=True)
   
   class Meta: 
      managed = True
      db_table = 'delivery_status'
   def __unicode__(self):
      return unicode(self.ref_id)

class Wishlist(models.Model):
   id = models.AutoField(primary_key=True)
   user = models.ForeignKey(Users, blank=True, null=True)
   ref_id = models.CharField(max_length=100, blank=True, null=True)
   timestamp = models.DateTimeField(auto_now_add=True)
   
   class Meta: 
      managed = True
      db_table = 'wishlist'
   def __unicode__(self):
      return unicode(self.ref_id)

class Reviews(models.Model):
   id = models.AutoField(primary_key=True)
   user = models.ForeignKey(Users, blank=True, null=True)
   ref_id = models.CharField(max_length=100, blank=True, null=True)
   timestamp = models.DateTimeField(auto_now_add=True)
   title = models.CharField(max_length=200, blank=True, null=True)
   detailed_review = models.CharField(max_length=1000, blank=True, null=True)
   recommended = models.CharField(max_length=10, blank=True, null=True)
   
   class Meta: 
      managed = True
      db_table = 'reviews'
   def __unicode__(self):
      return unicode(self.ref_id)
      
class Tax_And_Refund_Policies(models.Model):
   id = models.AutoField(primary_key=True)
   product_type = models.CharField(max_length=100, blank=True, null=True, unique=True)
   #All figures in percentage
   #Tax breakdown
   total_tax = models.FloatField(blank=True, null=True)
   #Payment policies
   min_payment_needed_before_confirmation = models.FloatField(blank=True, null=True)
   #Refund policies
   refund_before_confirmation = models.FloatField(blank=True, null=True)
   refund_within_2_days = models.FloatField(blank=True, null=True)
   refund_between_2_7_days = models.FloatField(blank=True, null=True)
   refund_between_7_15_days = models.FloatField(blank=True, null=True)
   refund_between_15_30_days = models.FloatField(blank=True, null=True)
   refund_after_30_days_or_processing = models.FloatField(blank=True, null=True)
   #Only for cards
   refund_after_die_preparing = models.FloatField(blank=True, null=True)
   timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
   
   class Meta: 
      managed = True
      db_table = 'tax_and_refund_policies'
   def __unicode__(self):
      return unicode(self.product_type)
