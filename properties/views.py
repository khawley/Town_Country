# Create your views here.
from properties.models import Homes, Photos
from django.shortcuts import render_to_response
from django import forms

#city_choices=Homes.objects.filter(city__isnull=False).distinct().values('city')


"""class SearchBar(forms.Form):
    beds=forms.IntegerField(min_value='0')
    min_price=forms.IntegerField(min_value='0', max_value='2000')
    max_price=forms.IntegerField(min_value='0', max_value='2000'
#    city=forms.ChoiceField(choices=city_choices, required=False)"""


def index(request):
    properties_list= Homes.objects.all()
    photo_list = Photos.objects.all()
    return render_to_response('properties/index.html',{'properties_list' : properties_list, 'photo_list': photo_list,})
""""    if request.method=='GET':
        form = SearchBar(request.GET)
        if form.is_valid():
            curr_beds=form.cleaned_data['beds']
            min_price=form.cleaned_data['min_price']
            max_price=form.cleaned_data['max_price']
            #curr_city=form.cleaned_data['city']
            if curr_beds!='None':
                properties_list=properties_list.filter(beds__gte=curr_beds)
            if min_price !='None':
                properties_list=properties_list.filter(price__lte=min_price)
            if max_price!='None':
                properties_list=properties_list.filter(price__lte=max_price)
            #if curr_city!='None':
            #    properties_list=properties_list.filter(city__exact=curr_city)
            return render_to_response('properties/index.html', {'properties_list':properties_list, 'photo_list': photo_list, 'form':form,})
    else:
        form = SearchBar()
        return render_to_response('properties/index.html',{'properties_list' : properties_list, 'photo_list': photo_list, 'form':form,})"""
    