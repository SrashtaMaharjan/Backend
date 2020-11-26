from django.shortcuts import render
from .models import mutual_table

# Create your views here.
from django.http import HttpResponse


#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    latest_mutual_list = mutual_table.objects.all().filter(needLevel = 3)
    context = {'latest_mutual_list': latest_mutual_list}
    return render(request, 'first_app/index.html', context)
