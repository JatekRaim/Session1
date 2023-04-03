import requests
from django.shortcuts import render
from django.urls import reverse


def order_add(request):
    template = 'check_point_app/order_add.html'
    context = {}

    if 'order_insert' in request.POST:
        URL = request.build_absolute_uri(reverse('api_orders'))
        max_order = requests.post(URL, data=request.POST).json()[0]
        URL = request.build_absolute_uri(reverse('api_visitors'))
        max_visitor = requests.post(URL, data=request.POST).json()[0]
        URL = request.build_absolute_uri(reverse('api_order_details'))
        print(max_order)
        print(max_visitor)
        data = {
            'id_max_visitor': max_visitor['max_visitor'],
            'id_max_order': max_order['max_order']
        }
        requests.post(URL, data=data)

    URL = request.build_absolute_uri(reverse('api_sub_units'))
    response_sub_units = requests.get(URL)
    context['sub_units'] = response_sub_units.json()

    URL = request.build_absolute_uri(reverse('api_targets'))
    response_targets = requests.get(URL)
    context['targets'] = response_targets.json()

    URL = request.build_absolute_uri(reverse('api_employees'))
    response_employees = requests.get(URL)
    context['employees'] = response_employees.json()

    return render(request, template, context)
# Create your views here.
