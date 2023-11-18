from django.shortcuts import render, redirect, reverse
# from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json

from django.views.decorators.csrf import csrf_exempt

from stats.weatherapi import *
from stats.aqiapi import *
# from stats.sportsapi import *

@csrf_exempt
def sdata(request):
    if request.method == "POST":
        theip = request.POST['ip']
        response = {
            'key1' : theip
        }
        print(response)
        render(request, "stats.html", response)
        return JsonResponse(response)
        # return redirect(homeview, response)
    elif request.method == "GET":
        return render(request, "stats.html")

@csrf_exempt
def tdata(request):
    if request.method == "POST":
        c_name = request.POST['c_name']
        latitude = request.POST['lat']
        longitude = request.POST['lon']
        country = request.POST['country']
        is_capital = request.POST['iscapital']
        population = request.POST['population']
        response = {
            'city_name' : c_name,
            'latitude' : latitude,
            'longitude' : longitude,
            'country' : country,
            'is_capital' : is_capital,
            'population' : population,
        }
        print(request)
        print(response)
        # return render(request, "astats.html", response)
        # return redirect("dash", response)
        # return JsonResponse(response)
        # return redirect(reverse('dash'),response)
        cn = response['city_name']
        clat = response['latitude']
        clon = response['longitude']
        # cn = json.loads(request.body)
        # cn = str(json.loads(request.body))
        # return redirect(reverse(dash(request, cn, clat, clon)))
        # return HttpResponseRedirect('/dash/'+cn+'/'+clat+'/'+clon)
        # return dash(request, cn, clat, clon)
        # return dash(request)
        return render(request, "astats.html", response)
        # return redirect(dash, cn, response['latitude'], response['longitude'])
        # return redirect(reverse(dash), cn)
        # return redirect(dash, response)
        # return "%s?%s" % (redirect('dash', args=(backend,))),urllib.urlencode(response)
    elif request.method == "GET":
        return render(request, "astats.html")

# def dash(request):
#     if request.method == "POST":
#         # print(c_name)
#         return render(request, "dash.html")
#     elif request.method == "GET":
#         # print(c_name)
#         return render(request, "dash.html")

# @csrf_exempt
# def dash(request, cn, clat, clon):
#     if request.method == "GET":
#         # data = request.GET
#         # return HttpResponse(request, {'cn':'one'})
#         print(clat, clon)
#         return render(request, "dash.html", {'cn': cn, 'clat': clat, 'clon': clon})
#     elif request.method == "POST":
#         print(clat, clon)
#         return render(request, "dash.html", {'cn': cn, 'clat': clat, 'clon': clon})

@csrf_exempt
def dash(request):
    if request.method == "GET":
        # data = request.GET
        # return HttpResponse(request, {'cn':'one'})
        # cn = request.GET['cn']
        # clat = request.GET['clat']
        # clon = request.GET['clon']
        rdata = str(request.GET.get('cn'))
        cdata = rdata.split("?")
        cn = cdata[0]
        clat = cdata[1][5:]
        clon = cdata[2][5:]
        weather = getweather(clat,clon)
        aqi = getaqi(clat,clon)
        print(cn, clat, clon, weather, aqi)
        context = {
            'cn': cn,
            'clat': clat,
            'clon': clon,
            'weather': weather,
            'aqi' : aqi
        }
        return render(request, "dash.html", context)
    elif request.method == "POST":
        # cn = request.POST['cn']
        # clat = request.POST['clat']
        # clon = request.POST['clon']
        cn = request.POST.get('cn')
        clat = request.POST.get('clat')
        clon = request.POST.get('clon')
        print(cn, clat, clon)
        return redirect(dash, {'cn': cn, 'clat': clat, 'clon': clon})
