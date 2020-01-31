from django.shortcuts import render, redirect
from .models import WackyWidget
from .forms import WackyWidgetForm
from django.http import HttpResponse
from django.db.models import Sum

def wacky_widgets_index(request):
    form = WackyWidgetForm()
    wacky_widgets = WackyWidget.objects.all()
    total_quantity = WackyWidget.objects.aggregate(tot=Sum('quantity'))['tot']
    return render(request, 'home.html', {'wacky_widgets':wacky_widgets, 'total_quantity':total_quantity, 'wacky_widget_form':form})

def add_wacky_widget(request):
    form = WackyWidgetForm(request.POST)
    if form.is_valid():
        wacky_widget = form.save()
        print(wacky_widget)
        return redirect('/')
    return render(request, 'home.html')

def delete_wacky_widget(request, wacky_widget_id):
    print(wacky_widget_id)
    wacky_widget = WackyWidget.objects.get(pk=wacky_widget_id)
    wacky_widget.delete()
    return redirect('/', {'wacky_widget_id':wacky_widget_id})
