from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json
from itertools import chain
from dashboard import Dashboard


# @login_required(login_url='/auth/login/')
class Music(Dashboard, View):
    try:
        def __init__(self):
            self.template_name = 'customers/music.html'
            self.wishlist_list = []
            self.filter_values = (0, 10000)
            self.popular_price_filter_values = (2000, 7000)

        def get_context_data(self, **kwargs):
            context = super(Music, self).get_context_data(**kwargs)
            return context

        def get_queryset(self, **kwargs):
            query = "select id, name from music_types"
            self.Music_subcategories = m.Music_Types.objects.raw(query)
            return self.Music_subcategories

        def prepare_wishlist_data(self, *args, **kwargs):
            request = args[0]
            if request.user.username:
                user_id = m.Users.objects.get(username=request.user.username).id
                query = "select id, ref_id from wishlist where user_id=" + str(user_id)
                wishlist = m.Wishlist.objects.raw(query)
                for wish in wishlist:
                    self.wishlist_list.append(str(wish.ref_id))
            return self.wishlist_list

        def get_musicians(self, request, **kwargs):
            type = self.kwargs['type']
            confidence_check_filter = request.GET.get('confidence_check_filter')
            category = request.GET.get('for')

            #Filter by Category
            if category == None or category == 'all':
                self.musicians = m.Music.objects.filter(type_id=type,actual_price__range=self.popular_price_filter_values)  # raw(query)

            else:
                self.musicians = m.Music.objects.filter( \
                    type_id=type, category=str(category), \
                    actual_price__range=self.popular_price_filter_values)  # use raw query

            # Filter by barati confidence. Select only if confidence > 20%
            if confidence_check_filter == 'add_confidence':
                self.musicians = self.musicians.exclude(barati_confidence_perc__isnull=True)
                self.musicians = self.musicians.exclude(barati_confidence_perc__lte=20.0)

            #Filter by shift
            shift_dict = {
                'shift_morning': request.GET.get('shift_morning'),
                'shift_afternoon': request.GET.get('shift_afternoon'),
                'shift_evening': request.GET.get('shift_evening'),
                'shift_night': request.GET.get('shift_night'),
            }
            shift_musicians, musicians_morning, musicians_afternoon, musicians_evening, musicians_night = [], [], [], [], []
            shift_filter = False
            for key,value in shift_dict.iteritems():
                if value == 'filter':
                    shift_filter = True
                    if key == 'shift_morning':
                        if self.musicians:
                            musicians_morning = self.musicians.filter(morning_shift = True)
                    if key == 'shift_afternoon':
                        if self.musicians:
                            musicians_afternoon = self.musicians.filter(afternoon_shift = True)
                    if key == 'shift_evening':
                        if self.musicians:
                            musicians_evening = self.musicians.filter(evening_shift = True)
                    if key == 'shift_night':
                        if self.musicians:
                            musicians_night = self.musicians.filter(night_shift = True)

            if shift_filter:
                self.musicians = None
            shift_musicians = set(list(chain(musicians_morning, musicians_afternoon, musicians_evening, musicians_night)))
            if shift_musicians:
                self.musicians = shift_musicians

            # Filter by discount
            discounts_dict = {
                '0-10': request.GET.get('0-10'),
                '10-20': request.GET.get('10-20'),
                '20-30': request.GET.get('20-30'),
                '30-40': request.GET.get('30-40'),
                '40-100': request.GET.get('40-100'),
            }

            musicians, musicians_0_10, musicians_10_20, musicians_20_30, musicians_30_40, musicians_40_100 = [], [], [], [], [], []
            for key, value in discounts_dict.iteritems():
                if value == 'filter':
                    if key == '0-10':
                        if self.musicians:
                            musicians_0_10 = self.musicians.filter(discount_perc__range=(0, 10))
                    if key == '10-20':
                        if self.musicians:
                            musicians_10_20 = self.musicians.filter(discount_perc__range=(10, 20))
                    if key == '20-30':
                        if self.musicians:
                            musicians_20_30 = self.musicians.filter(discount_perc__range=(20, 30))
                    if key == '30-40':
                        if self.musicians:
                            musicians_30_40 = self.musicians.filter(discount_perc__range=(30, 40))
                    if key == '40-100':
                        if self.musicians:
                            musicians_40_100 = self.musicians.filter(discount_perc__range=(40, 100))

            for key, value in discounts_dict.iteritems():
                if value == 'filter':
                    self.musicians = None
            musicians = list(chain(musicians_0_10, musicians_10_20, musicians_20_30, musicians_30_40, musicians_40_100))
            if musicians:
                self.musicians = musicians
            return self.musicians

        def get_price_filtered_musicians(self, request, selected_filter_values, **kwargs):
            type = self.kwargs['type']
            category = request.GET.get('for')
            if category == None:
                self.musicians = m.Music.objects.filter(type_id=type, actual_price__range=selected_filter_values)#raw(query)
            else:
                self.musicians = m.Music.objects.filter(\
                   type_id=type, category=str(category),\
                   actual_price__range=selected_filter_values)# use raw query
            shift_dict = {
                'shift_morning': request.GET.get('shift_morning'),
                'shift_afternoon': request.GET.get('shift_afternoon'),
                'shift_evening': request.GET.get('shift_evening'),
                'shift_night': request.GET.get('shift_night'),
            }
            shift_musicians, musicians_morning, musicians_afternoon, musicians_evening, musicians_night = [], [], [], [], []
            shift_filter = False
            for key, value in shift_dict.iteritems():
                if value == 'filter':
                    shift_filter = True
                    if key == 'shift_morning':
                        if self.musicians:
                            musicians_morning = self.musicians.filter(morning_shift=True)
                    if key == 'shift_afternoon':
                        if self.musicians:
                            musicians_afternoon = self.musicians.filter(afternoon_shift=True)
                    if key == 'shift_evening':
                        if self.musicians:
                            musicians_evening = self.musicians.filter(evening_shift=True)
                    if key == 'shift_night':
                        if self.musicians:
                            musicians_night = self.musicians.filter(night_shift=True)

            if shift_filter:
                self.musicians = None
            shift_musicians = set(
                list(chain(musicians_morning, musicians_afternoon, musicians_evening, musicians_night)))
            if shift_musicians:
                self.musicians = shift_musicians
            return self.musicians

        # @login_required(login_url='/auth/login/')
        def get(self, request, **kwargs):
            subcategories = self.get_context_data()['music_types']
            musicians = self.get_musicians(request)
            wishlist_list = self.prepare_wishlist_data(request)
            filter_values = self.filter_values
            # Get tax
            tax = super(Music, self).get_tax('music')
            context_dict = {
                'subcategories': subcategories, 'musicians': musicians, 'category': 'music',
                'type': self.kwargs['type'], \
                'wishlist_list': wishlist_list, 'filter_values': filter_values, \
                'popular_price_filter_values': self.popular_price_filter_values, 'tax': tax
            }
            context_dict.update(self.get_context_data(request=request))
            return render(request, self.template_name, context_dict)

        def post(self, request, **kwargs):
            slider_values = request.POST.get('slider');
            selected_filter_values = None
            if slider_values is not None:
                selected_filter_values = tuple(slider_values.split(','))
            subcategories = self.get_context_data()['music_types']
            musicians = self.get_price_filtered_musicians(request, selected_filter_values)
            wishlist_list = self.prepare_wishlist_data(request)
            # Get tax
            tax = super(Music, self).get_tax('music')
            context_dict = {
                'subcategories': subcategories, 'musicians': musicians, 'category': 'music',
                'type': self.kwargs['type'], \
                'wishlist_list': wishlist_list, 'filter_values': self.filter_values, \
                'selected_filter_values': selected_filter_values, 'tax': tax
            }
            context_dict.update(self.get_context_data(request=request))
            return render(request, self.template_name, context_dict)

    except Exception as e:
        print e
        print sys.exc_traceback.tb_lineno
