import json
import logging

from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


from .models import Category, TimeLog


# Create your views here.
def hello_world(request):
    data = {"message": "Hello World!"}
    return JsonResponse(data)

def index(request):
    return render(request, )


@csrf_exempt
@require_http_methods(["GET", "POST"])
def categories(request: HttpRequest):
    if request.method == "GET":
        categories_available = list(Category.objects.all().values())
        return JsonResponse(categories_available, safe=False)

    try:
        data = json.loads(request.body)
        new_category = {
            'name': data['name'],
            'description': data.get('description')
        }
    except (json.JSONDecodeError, KeyError):
        raise HttpResponseBadRequest

    new_cat = Category.objects.create(**new_category)
    new_cat.save()
    return JsonResponse({"success": True}, status=201)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def timelogs(request: HttpRequest):
    if request.method == "GET":
        timelogs_ = list(
            TimeLog.objects.all().order_by('-added')[:20].values()
        )
        return JsonResponse(timelogs_, safe=False)
    try:
        data = json.loads(request.body)
        new_task = {
            'name': data['name'],
            'description': data.get('description'),
            'duration': data['duration'],
            'type': data['type'],
            'added': data['added']
        }
    except (json.JSONDecodeError, KeyError):
        raise HttpResponseBadRequest
    try:
        category = Category.objects.get(name=new_task['type'])
    except ObjectDoesNotExist:
        logging.warning("Got invalid category %s", new_task['type'])
        raise HttpResponseBadRequest

    # overriding type with category instance
    new_task['type'] = category
    new_task_obj = TimeLog.objects.create(**new_task)
    new_task_obj.save()
    return JsonResponse({"success": True}, status=201)
