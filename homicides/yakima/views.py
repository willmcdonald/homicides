from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Homicide
from .models import HomicideFilter


def index(request):
    f = HomicideFilter(request.GET, queryset=Homicide.objects.all())
    return render(request, 'yakima/index.html', {'filter': f})

def detail(request, homicide_id):
    homicide = get_object_or_404(Homicide, pk=homicide_id)
    related = Homicide.objects.order_by('-date')[:5]
    return render(request, 'yakima/detail.html', {'homicide': homicide, 'related':related})
