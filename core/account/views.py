from django.shortcuts import redirect, render
from django.contrib.auth import views as auth_views
from django.contrib import messages  # To display feedback messages

from account.forms import AuthenticationForm,UserCreationForm_email
from account.models import User

from OTP.models import OTPRequest
# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = "account/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True

class LogoutView(auth_views.LogoutView):
    pass

def RegisterView(request):
    if request.method == 'POST':
        form = UserCreationForm_email(request.POST)

        if  form.is_valid():
            # Save the form data without committing to trigger OTP verification
            request.session['user_data'] = form.cleaned_data
            
            # Generate and store the OTP request_id in the session
            otp_request = OTPRequest.objects.generate({'channel': 'email', 'receiver': form.cleaned_data['email']})
            request.session['otp_request_id'] = str(otp_request.request_id)
            
            return redirect('account:verify_otp')
    else:
        form = UserCreationForm_email()

    return render(request, "account/sign-up.html", {'form':form})

def VerifyOTPView(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        email = request.session.get('user_data').get('email')
        request_id = request.session.get('otp_request_id')  # Retrieve request_id from the form or session

        if OTPRequest.objects.is_valid(email,request_id, otp):
            user_data = request.session.get('user_data')
            # Create the user now after OTP verification
            user = User.objects.create(
                first_name=user_data.get('first_name'),
                last_name=user_data.get('last_name'),
                email=user_data.get('email'),
            )
            user.set_password(user_data.get('password'))
            user.save()
            

            # Clear session data
            del request.session['user_data']
            del request.session['otp_request_id']
            messages.success(request, 'User has been created and verified successfully!')
            return redirect('accounts:login')  # Redirect to login after success
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
    
    return render(request, 'accounts/verify_otp.html')