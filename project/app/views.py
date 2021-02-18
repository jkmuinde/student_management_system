from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    template_name='admin/home.html'
    return render(request, template_name, context)