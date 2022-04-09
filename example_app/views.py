from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'example_value': '***this is an example_app value from the App***'}
    return render(request, 'example_app/index.html', context=my_dict)

