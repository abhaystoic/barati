from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json
from datetime import datetime,timedelta



class Save_Card_Preferences(View):
    try:
        def __init__(self):
            pass

        def get_context_data(self, **kwargs):
            context = {}
            return context

        def get_date_time(self,date_time):
            if len(date_time) == 0:
                return ''
            date,time=date_time.split()
            return datetime.strptime("-".join(reversed(date.split('/'))) + ' ' + time, "%Y-%m-%d %H:%M")

        def post(self, request, **kwargs):
            lang = request.POST.get('select_lang')
            user_id = m.Users.objects.get(username=request.user.username)

            card = m.Cards.objects.get(pk = kwargs['card_id'])
            ref_id = card.ref_id

            obj = m.Cards_Preferences.objects.get_or_create(
                card=card, user=user_id, ref_id=ref_id
            )
            # avail_printing = models.NullBooleanField(blank=True)

            shloka = request.POST.get('popular_shloka').encode("utf-8")
            if shloka == u'nothing':
                shloka = request.POST.get('custom_shloka').encode("utf-8")
            obj[0].sholka = shloka
            obj[0].bride_name = request.POST.get(lang + '_bride_name').encode("utf-8")
            obj[0].groom_name = request.POST.get(lang + '_groom_name').encode("utf-8")
            obj[0].groom_grandfather_name = request.POST.get(lang + '_grandfather_groom').encode("utf-8")
            obj[0].bride_grandfather_name = request.POST.get(lang + '_grandfather_bride').encode("utf-8")
            obj[0].groom_grandmother_name = request.POST.get(lang + '_grandmother_groom').encode("utf-8")
            obj[0].bride_grandmother_name = request.POST.get(lang + '_grandmother_bride').encode("utf-8")
            obj[0].groom_father_name = request.POST.get(lang + '_father_groom').encode("utf-8")
            obj[0].bride_father_name = request.POST.get(lang + '_father_bride').encode("utf-8")
            obj[0].groom_mother_name = request.POST.get(lang + '_mother_groom').encode("utf-8")
            obj[0].bride_mother_name = request.POST.get(lang + '_mother_bride').encode("utf-8")
            tilak_tika_time = self.get_date_time(request.POST.get('tilak_date'))
            if tilak_tika_time != '':
                obj[0].tilak_tika_time = tilak_tika_time
            swagat_bhoj_time = self.get_date_time(request.POST.get('swagat_date'))
            if swagat_bhoj_time != '':
                obj[0].swagat_bhoj_time = swagat_bhoj_time
            mandap_time = self.get_date_time(request.POST.get('mandap_date'))
            if mandap_time != '':
                obj[0].mandap_time = mandap_time
            vidai_time = self.get_date_time(request.POST.get('vidai_date'))
            if vidai_time != '':
                obj[0].tilak_tika_time = vidai_time
            obj[0].tilak_tika_venue = request.POST.get(lang + '_tilak_venue').encode("utf-8")
            obj[0].swagat_bhoj_venue = request.POST.get(lang + '_swagat_venue').encode("utf-8")
            obj[0].mandap_venue = request.POST.get(lang + '_mandap_venue').encode("utf-8")
            obj[0].relatives_names_darshanabhilashi = request.POST.get(lang + '_relative_names').encode("utf-8")
            obj[0].relatives_names_swagatecchuk = request.POST.get(lang + '_relative_names_2').encode("utf-8")
            obj[0].kids_names_darshanabhilashi = request.POST.get(lang + '_kids_name').encode("utf-8")
            obj[0].kids_quote = request.POST.get(lang + '_quote').encode("utf-8")
            obj[0].save()

            message = "success_card_preferences_saved"
            return HttpResponse(json.dumps(message))

    except Exception as general_exception:
        print 'Hello'
        print general_exception
        print sys.exc_traceback.tb_lineno
