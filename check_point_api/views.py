from django.db import connection
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def dictfetchall(cursor):
    columns = [cols[0] for cols in cursor.description]
    return [dict(zip(columns, row))
            for row in cursor.fetchall()]


@csrf_exempt
def api_visitors(request):
    if request.method in 'POST':
        in_lastname_visitor = request.POST.get('in_lastname_visitor')
        in_firstname_visitor = request.POST.get('in_firstname_visitor')
        in_middlename_visitor = request.POST.get('in_middlename_visitor', None)
        in_organization = request.POST.get('in_organization', None)
        in_telephone_number = request.POST.get('in_telephone_number')
        in_email_visitor = request.POST.get('in_email_visitor')
        in_notice = request.POST.get('in_notice')
        in_date_of_birthday = request.POST.get('in_date_of_birthday')
        in_passport_series = request.POST.get('in_passport_series')
        in_passport_number = request.POST.get('in_passport_number')
        in_black_list_visit = request.POST.get('in_black_list_visit', 0)

        in_middlename_visitor = None if in_middlename_visitor == '' else in_middlename_visitor
        in_organization = None if in_organization == '' else in_organization
        with connection.cursor() as cursor:
            cursor.callproc('visitor_insert', [in_lastname_visitor,
                                                in_firstname_visitor,
                                                in_middlename_visitor,
                                                in_organization,
                                                in_telephone_number,
                                                in_email_visitor,
                                                in_notice,
                                                in_date_of_birthday,
                                                in_passport_series,
                                                in_passport_number,
                                                in_black_list_visit])
            max_visitor = dictfetchall(cursor)
        return JsonResponse(max_visitor, safe=False)
    else:
        return HttpResponse(status=404)


@csrf_exempt
def api_orders(request):
    if request.method == 'POST':
        in_date_time_begin_wish = request.POST.get('in_date_time_begin_wish')
        in_date_time_end_wish = request.POST.get('in_date_time_end_wish')
        in_count_visitors = request.POST.get('in_count_visitors', 1)
        id_type_order = request.POST.get('id_type_order', 2)
        id_target = request.POST.get('id_target')
        id_status = request.POST.get('id_status', 2)
        id_sub_unit = request.POST.get('id_sub_unit')
        id_employee = request.POST.get('id_employee')

        with connection.cursor() as cursor:
            cursor.callproc('order_insert', [in_date_time_begin_wish,
                                            in_date_time_end_wish,
                                            in_count_visitors,
                                            id_type_order,
                                            id_target,
                                            id_status,
                                            id_sub_unit,
                                            id_employee])
            max_order = dictfetchall(cursor)
        return JsonResponse(max_order, safe=False)
    else:
        return HttpResponse(status=404)


def api_sub_units(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.callproc('sub_unit_select_all')
            sub_units = dictfetchall(cursor)
        return JsonResponse(sub_units, safe=False)
    else:
        return HttpResponse(status=404)


def api_targets(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.callproc('target_select_all')
            targets = dictfetchall(cursor)
        return JsonResponse(targets, safe=False)
    else:
        return HttpResponse(status=404)


def api_employees(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.callproc('employees_select_all')
            targets = dictfetchall(cursor)
        return JsonResponse(targets, safe=False)
    else:
        return HttpResponse(status=404)
# Create your views here.
