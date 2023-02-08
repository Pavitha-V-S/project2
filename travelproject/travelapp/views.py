from django.shortcuts import render

from . models import destinations
from.models import team
def demo(request):
    obj=destinations.objects.all()
    obj1 = team.objects.all()
    return render(request,"index.html",{'result':obj,'results':obj1})





