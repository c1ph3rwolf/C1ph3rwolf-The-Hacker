from django.shortcuts import render
from django.http      import HttpResponse
from django.template  import loader

def thetools(request):
    template = loader.get_template('tools.html')
    context = {
        'title' : '',
    }
    return HttpResponse(template.render(context,request))
# Create your views here.
