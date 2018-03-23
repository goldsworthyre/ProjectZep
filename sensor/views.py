from django.shortcuts import render


# Create your views here.
def data(request):
    context = {}
    return render(request, 'data.html', context)