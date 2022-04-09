from django.shortcuts import render
import random
import time
import logging

# Create your views here.

def help_app(request):
    help_dict = {'example_item': " here is some help on the example item lorem", "random_number": 0}
    logging.basicConfig(filename='help.log', encoding='utf-8', level=logging.INFO)

    while True:

        n = random.randint(0, 100)
        help_dict.update({"random_number": n})
        logging.info(" This is the random {} number".format(help_dict.get("random_number")))
        return render(request, 'help_app/index.html', context=help_dict)
        time.sleep(10)
