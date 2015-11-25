from django.db import models
from django.core.validators import RegexValidator #For phone number validation

class Religion(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50, unique=True)
   
   class Meta:
      managed = True
      db_table = 'religion'
   def __unicode__(self):
      return unicode(self.name)

class Address(models.Model):
   id = models.AutoField(primary_key=True)
   building_number = models.CharField(max_length=50, blank=True, null=True)
   street = models.CharField(max_length=100, blank=True, null=True)
   locality = models.CharField(max_length=50, blank=True, null=True)
   landmark = models.CharField(max_length=50, blank=True, null=True)
   city = models.CharField(max_length=50, blank=True, null=True)
   state = models.CharField(max_length=50, blank=True, null=True)
   country = models.CharField(max_length=50, blank=True, null=True)
   zipcode = models.CharField(max_length=50, blank=True, null=True)
   
   class Meta:
      managed = True
      db_table = 'address'
   def __unicode__(self):
      return unicode(self.id)
     

class Users(models.Model):
   id = models.AutoField(primary_key=True)
   username = models.CharField(max_length=50, unique=True)
   first_name = models.CharField(max_length=50, blank=True, null=True)
   middle_name = models.CharField(max_length=100, blank=True, null=True)
   last_name = models.CharField(max_length=50, blank=True, null=True)
   religion = models.ForeignKey(Religion, blank=True, null=True)
   email = models.EmailField(max_length=100, blank=True, null=True)
   phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
   contact1 = models.CharField(validators=[phone_regex], max_length=50, blank=True, null=True) # validators should be a list
   contact2 = models.CharField(validators=[phone_regex], max_length=50, blank=True, null=True) # validators should be a list
   contact3 = models.CharField(validators=[phone_regex], max_length=50, blank=True, null=True) # validators should be a list
   address = models.ForeignKey(Address, blank=True, null=True)
   
   class Meta:
      managed = True
      db_table = 'users'
   def __unicode__(self):
      return unicode(self.username)
		
class Vendors(models.Model):
   id = models.AutoField(primary_key=True)
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
      
class Photo_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'photo_types'
   def __unicode__(self):
      return unicode(self.name)

class Video_Types(models.Model):
   id = models.AutoField(primary_key=True)   
   name = models.CharField(max_length=50)
   
   class Meta:
      managed = True
      db_table = 'video_types'
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
   ref_id = models.CharField(max_length=100)
   vendor_id = models.ForeignKey(Vendors)
   name = models.CharField(max_length=100)
   type = models.ForeignKey(Venue_Types, blank=True, null=True)
   address = models.ForeignKey(Address, blank=True, null=True)
   short_description = models.CharField(max_length=100)
   long_description = models.CharField(max_length=800)
   min_capacity = models.IntegerField()
   max_capacity = models.IntegerField()
   accomodation_available = models.BooleanField()
   
   class Meta:
      managed = True
      db_table = 'venues'
   def __unicode__(self):
      return unicode(self.name)

class Cards(models.Model):
   id = models.AutoField(primary_key=True)
   ref_id = models.CharField(max_length=100)
   vendor_id = models.ForeignKey(Vendors)
   name = models.CharField(max_length=100)
   type = models.ForeignKey(Card_Types, blank=True, null=True)
   short_description = models.CharField(max_length=100)
   long_description = models.CharField(max_length=800)
   min_numbers = models.IntegerField()
   max_numbers = models.IntegerField()
   price = models.IntegerField()
   
   class Meta: 
      managed = True
      db_table = 'cards'
   def __unicode__(self):
      return unicode(self.ref_id)
      
class Cart(models.Model):
   id = models.AutoField(primary_key=True)
   ref_id = models.CharField(max_length=100)
   user = models.ForeignKey(Users)
   product_type = models.CharField(max_length=50)
   checked_out = models.BooleanField(default=False)
   quantity = models.IntegerField(blank=True, null=True)
   total_price = models.IntegerField(blank=True, null=True)
   
   class Meta: 
      managed = True
      db_table = 'cart'
   def __unicode__(self):
      return unicode(self.ref_id)

#To store paths of the pictures on the server      
class Product_Pictures(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100, blank=True, null=True)
   ref_id = models.CharField(max_length=100, blank=True, null=True)
   picture_path = models.CharField(max_length=200, blank=True, null=True)
   
   class Meta: 
      managed = True
      db_table = 'product_pictures'
   def __unicode__(self):
      return unicode(self.ref_id)
