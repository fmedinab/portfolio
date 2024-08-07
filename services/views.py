from django.shortcuts import render

# Create your views here.
def render_services(request):
     return render(request, 'service_page.html')