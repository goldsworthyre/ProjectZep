from django.shortcuts import render


# Create your views here.
def control(request):
    context = {}
    return render(request, 'control.html', context)