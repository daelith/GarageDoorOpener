import subprocess
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
            pass
        elif smsbody == 'Bmf On':
            subprocess.call(['/Library/Application\ Support/Perceptive\ Automation/Indigo\ 5/IndigoPluginHost.app/Contents/MacOS/IndigoPluginHost --port=1199 -e "indigo.device.turnOn(\'Basement Media Fluorescent\')"'], shell=True)
        elif smsbody == 'Bmf Off':
            subprocess.call(['/Library/Application\ Support/Perceptive\ Automation/Indigo\ 5/IndigoPluginHost.app/Contents/MacOS/IndigoPluginHost --port=1199 -e "indigo.device.turnOff(\'Basement Media Fluorescent\')"'], shell=True)
    return HttpResponse("Thanks!")




