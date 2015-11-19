from django.db import models
from django.core.validators import RegexValidator #For phone number validation

class Religion(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50, unique=True)
   
   class Meta:
      managed = False
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
      managed = False
      db_table = 'address'
   def __unicode__(self):
      return unicode(self.name)
     

class Users(models.Model):
   id = models.AutoField(primary_key=True)
   username = models.CharField(max_length=50, primary_key=True)
   first_name = models.CharField(max_length=50, blank=True, null=True)
   middle_name = models.CharField(max_length=100, blank=True, null=True)
   last_name = models.CharField(max_length=50, blank=True, null=True)
   religion = models.ForeignKey(Religion, blank=True, null=True)
   email = models.EmailField(max_length=100, blank=True, null=True)
   phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
   contact1 = models.CharField(validators=[phone_regex], max_length=50, blank=True) # validators should be a list
   contact2 = models.CharField(validators=[phone_regex], max_length=50, blank=True) # validators should be a list
   contact3 = models.CharField(validators=[phone_regex], max_length=50, blank=True) # validators should be a list
   address = models.ForeignKey(Address, blank=True, null=True)
   class Meta:
      managed = False
      db_table = 'users'
   def __unicode__(self):
      return unicode(self.name)
		
