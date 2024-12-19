from django.urls import path
from .views import IndexView,aboutus,contactus,TermsAndCondition,NewsletterView,resume

namespaces = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('aboutus/', aboutus, name='about'),
    path('contactus/', contactus, name='contact'),
    path('resume/', resume, name='resume'),  # Add URL pattern for the index view
    path('terms-and-conditions/', TermsAndCondition, name='Terms-and-conditions'),
    path("newsletter/", NewsletterView.as_view(), name="newsletter"),
]