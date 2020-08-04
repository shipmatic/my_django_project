from django.shortcuts import render
from django.http import HttpResponse
from account.models import Profile #класс который описывает нашу таблицу

# Create your views here.
def get_profiles_list(request):
    objects = Profile.objects.all()
    result = '<br>'.join((str(obj) for obj in objects))
    # print(object)
    return HttpResponse(result)
    