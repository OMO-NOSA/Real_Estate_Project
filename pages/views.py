from django.shortcuts import render
from listings.models import Listings
from listings.choices import bedroom_choices , price_choices , state_choices
from realtors.models import Realtor
# Create your views here.

def index(request):
    listing = Listings.objects.all().order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listing': listing,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices

    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get realtors from Database
    realtors = Realtor.objects.order_by('-hire_date')
    # Get MVP realtor
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realtors,
        'mvp_realtor': mvp_realtor
    }


    return render(request, 'pages/about.html', context)


