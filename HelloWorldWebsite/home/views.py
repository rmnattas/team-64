# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from .models import Counter
from opensky_api import OpenSkyApi
import json
import geopy.distance

# Create your views here.
class Home(generic.DetailView):
    model = Counter
    template_name = "home/index.html"

    def get(self, request, *args, **kwargs):
        context = {'our_counter' : Counter.objects.get(pk=1)}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        counter_object = Counter.objects.get(pk=1)
        counter_object.count += 1
        counter_object.save()
        return redirect('homepage')



class API(generic.DetailView):
    #model = Counter
    #template_name = "home/index.html"

    def get(self, request, *args, **kwargs):
        lat = float(request.GET["lat"])
        lon = float(request.GET["lon"])
        json = getPlanes(lat, lon)

        return HttpResponse(json, content_type='application/json')

def getPlanes(latitude, longitude):
    bbox = [latitude - 5, latitude + 5, longitude - 5, longitude + 5]
    s = OpenSkyApi().get_states(bbox=bbox)

    result = []
    for plane in s.states:
    	result.append({
    	"callsign": plane.callsign.strip(),
    	"latitude": plane.latitude,
    	"longitude": plane.longitude,
    	"heading": plane.heading,
    	"distance_km": geopy.distance.geodesic((latitude, longitude), (plane.latitude, plane.longitude)).km
    	})

    result.sort(key=lambda x: x["distance_km"])
    dump = json.dumps(result[:3])
    return(dump)



