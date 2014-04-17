from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def text_from_twilio(request, *args, **kwargs):
    phone_number = request.GET['From']
    smsbody = request.GET['Body']
    # validate phone_number
    if phone_number != "+14358494734":
        return HttpResponseNotFound("Nice try!")
    else:
        if smsbody == 'Activate':
            #activate garage
            pass
    return HttpResponse("Thanks!")




