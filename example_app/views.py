from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'example_value': '***this is an example_app value from the App***'}
    return render(request, 'explore_templates/index.html', context=my_dict)

