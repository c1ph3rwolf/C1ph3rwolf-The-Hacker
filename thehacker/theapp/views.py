from django.shortcuts import render

# Create your views here.
from django.template  import loader

# def tools_view(request):
#     template = loader.get_template('streams.html')
#     context = {
#         'title' : '',
#     }
#     return HttpResponse(template.render(context,request))




def home_view(request):
    return render(request, 'home.html')


def base_view(request):
    return render(request, 'base.html')

def browse_view(request):
    return render(request, 'browse.html')

def details_view(request):
    return render(request, 'details.html')

def profile_view(request):
    return render(request, 'profile.html')

def tools_view(request):
    context = {
        'heading': 'Services Offered'
    }
    return render(request, 'tools.html', context)
