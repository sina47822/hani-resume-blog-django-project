from django.shortcuts import render
from django.views import View

# Create your views here.
def handler_404(request, exception=None, template_name='errors/404.html'):
    context = {}
    return render(request, template_name, context=context, status=404)
def handler_400(request, exception=None, template_name='errors/400.html'):
    context = {}
    return render(request, template_name, context=context, status=400)
def handler_403(request, exception=None, template_name='errors/403.html'):
    context = {}
    return render(request, template_name, context=context, status=403)
def handler_500(request, exception=None, template_name='errors/500.html'):
    context = {}
    return render(request, template_name, context=context, status=500)
class IndexView(View):
    template_name = "website/index.html"  # Define the template name
    
    def get(self, request):
        # You can add any context data you want to pass to the template
        context = {
            "message": "Welcome to the index page!"  # Example data to pass to template
        }
        return render(request, self.template_name, context)
# About Us View
def aboutus(request):
    return render(request, 'about-us.html')

# Contact Us View
def contactus(request):
    return render(request, 'contact-us.html')

# Resume View
def resume(request):
    return render(request, 'resume.html')