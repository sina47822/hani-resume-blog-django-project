from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
#forms
from django.views.generic import CreateView
from .forms import ContactForm, NewsLetterForm
from django.contrib import messages

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
    return render(request, 'website/about-us.html')

# Contact Us View
def contactus(request):
    return render(request, 'website/contact-us.html')

# Resume View
def resume(request):
    return render(request, 'website/resume.html')

def TermsAndCondition(request):
    return render (request , 'website/termandcondition.html')

class SendContactView(CreateView):
    """
    a class based view to show index page
    """
    http_method_names = ['post']
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'تیکت شما با موفقیت ثبت شد و در اسرع وقت با شما تماس حاصل خواهد شد')
        return super().form_valid(form)

    def form_invalid(self, form):
        # handle unsuccessful form submission
        messages.error(
            self.request, 'مشکلی در ارسال فرم شما پیش آمد لطفا ورودی ها رو بررسی کنین و مجدد ارسال نمایید')
        return redirect(self.request.META.get('HTTP_REFERER'))

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
    
class NewsletterView(CreateView):
    http_method_names = ['post']
    form_class = NewsLetterForm
    success_url = '/'

    def form_valid(self, form):
        # handle successful form submission
        messages.success(
            self.request, 'از ثبت نام شما ممنونم، اخبار جدید رو براتون ارسال می کنم 😊👍')
        return super().form_valid(form)

    def form_invalid(self, form):
        # handle unsuccessful form submission
        messages.error(
            self.request, 'مشکلی در ارسال فرم شما وجود داشت که می دونم برا چی بود!! چون ربات هستید!')
        return redirect('website:index')
    