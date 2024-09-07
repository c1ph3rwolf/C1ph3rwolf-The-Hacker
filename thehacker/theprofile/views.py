from django.shortcuts import render
from django.http      import HttpResponse
from django.template  import loader

def theprofile(request):
    template = loader.get_template('profile.html')
    context = {
        'sitetitle' : 'c1ph3rwolf',
    }
    return HttpResponse(template.render(context,request))

# Create your views here.
