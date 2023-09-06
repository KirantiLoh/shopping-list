from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'Maurice Yang',
        'class': 'PBP D'
    }
    return render(request, 'main.html', context)