from django.shortcuts import render
from django.http import HttpResponse

from records.models import Records

def top(request):
    return render(request, "records/top.html")