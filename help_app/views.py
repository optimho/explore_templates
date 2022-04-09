from django.shortcuts import render

# Create your views here.

def help_app(request):
    help_dict = {'example_item': " here is some help on the example item lorem"}
    return render(request, 'help_app/index.html', context=help_dict)
