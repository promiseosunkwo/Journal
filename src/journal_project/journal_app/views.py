from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateRegisterForm,AuthorForm, my_userForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Author,my_user
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import  force_bytes,  force_text, force_str, DjangoUnicodeDecodeError
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
import threading
from .utils import generate_token
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
User = get_user_model()


# class EmailThread(threading.Thread):
#     def __init__(self,email) -> None:
#         self.email = email
#         threading.Thread.__init__(self)

#     def run(self):
#         self.email.send()





def send_activation_email(user, request):
    # My_user = my_user()
    # timestamp = My_user.timestamp
    current_site = get_current_site(request)
    email_subject = 'Activate your Account'
    email_body = render_to_string('email_validation/activation.html',{
        'user':user, 
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)

         })

    compose_email=EmailMessage(
        email_subject,
        email_body,
        settings.EMAIL_HOST_USER,
        [user.email]
        )
    compose_email.send(fail_silently = False)
    # email = EmailMessage(subject=email_subject,body=email_body,from_email=settings.EMAIL_HOST_USER,to=[user.email])
    

    # EmailThread(email).start



def home(request):
    context = {}

    return render(request, "index.html", context)


def article(request):
    context = {}

    return render(request, "article.html", context)



def register(request):
    form = CreateRegisterForm()
    my_userModel = my_user()
    if request.method == "POST":
        form = CreateRegisterForm(request.POST)
        user = request.user
        if form.is_valid():
            form.save()

            my_userModel.user = user
            my_userModel.username = form.cleaned_data.get('username')
            # my_userModel.is_email_verified = True
            my_userModel.save()

            # send_activation_email(user,request)
          
            messages.success(request, 'Account created Successfully. Check your Email for Link to Proceed')
            form = CreateRegisterForm()

    context = { 'form' : form}
    return render(request, "register.html", context)




def dashboard(request):
    context = {}

    return render(request, "dashboard/dashboard.html", context)




def loginPage(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)
            
            # try block to check if get_my_user is a valid name of database
            try:
                get_my_user = my_user.objects.get(username=request.POST.get('username'))

            except:
                messages.info(request, 'Username or Password is Invalid')
                return redirect('login')

            if not get_my_user.is_email_verified:
                messages.info(request, 'Your account is not Verified. Use the link on your Email to verify your account')
                return redirect('login')

            if user:
                login(request, user)
                try:
                    author = Author.objects.get(user=request.user)
                    form = AuthorForm(instance = author)
                    return redirect('dashboard')
                except:
                    return redirect('login_edit_profile')
            
            else:
                messages.info(request, 'Username or Password is Incorrect')

    context = {}
    return render(request, "login.html", context)



def logoutUser(request):
    logout(request)
    return redirect('login')



def edit_profile(request):
    if request.method == "GET":
        try:
            author = Author.objects.get(user=request.user)
            form = AuthorForm(instance = author)
        except:
            return redirect('login_edit_profile')
    
    else:
        author_user= Author.objects.get(user=request.user)
        form = AuthorForm(request.POST, instance = author_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully')
    context = {'form': form}
    return render(request, 'dashboard/edit_profile.html', context)



def login_edit_profile(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            form = AuthorForm()
            messages.info(request, 'Updated Successfully')
            return redirect('dashboard')
 
    context = {'form': form}
    return render(request, 'dashboard/login_edit_profile.html', context)




def profile(request):
    context = {}
    return render(request, "dashboard/profile.html", context)



def submit_script(request):
    context = {}
    return render(request, "dashboard/submit_script.html", context)



def activate_user(request,uidb64,token):
    my_userModel = my_user()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user is not None and generate_token.check_token(user,token):

        my_userModel.is_email_verified = True
        my_userModel.save()
        messages.success(request, 'Email Verified Successfully. Please Login')
        return redirect('login')

    return render(request, 'email_validation/verification_failed.html', {'user':user})

