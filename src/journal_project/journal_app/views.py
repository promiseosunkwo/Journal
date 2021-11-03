from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateRegisterForm,AuthorForm, my_userForm,ManuscriptForm,UploadsForm,CoauthorFormset,CoauthorList,CoauthorListAuthor,CoauthorListForm,Manuscript,CoAuthors,Uploads,ManuscriptFormEditor,publishForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Author, CoAuthors,my_user,Status,Journal,publish,front_page
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
# from formtools.wizard.views import SessionWizardView
from django.core.files.storage import DefaultStorage
import datetime
from urllib.parse import urlencode
import random
import urllib.request
from django.forms.models import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import mimetypes
import os

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

def register(request):
    form = CreateRegisterForm()
    my_userModel = my_user()
    # coauthorList = CoauthorListAuthor()
    # coauthorform = CoauthorListForm()
    if request.method == "POST":
        form = CreateRegisterForm(request.POST)
        user = request.user
        if form.is_valid():
            form.save()

            my_userModel.user = user
            my_userModel.username = form.cleaned_data.get('username')
            my_userModel.save()

            # coauthorList.name = my_userModel.username
            # if coauthorList.is_valid():
            #     coauthorList.save()

            # send_activation_email(user,request)
          
            messages.success(request, 'Account created Successfully. Check your Email for Link to Proceed')
            form = CreateRegisterForm()

    context = { 'form' : form}
    return render(request, "register.html", context)



# @login_required
def dashboard(request):
    context = {}

    return render(request, "dashboard/dashboard.html", context)




def loginPage(request):
    if request.method == "POST":
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)

            check_user = User.objects.get(username=request.POST.get('username'))
            if user and check_user.is_staff:
                return redirect('editor_overview')

            if not check_user.is_active:
                messages.info(request, 'This has been disabled! Contact Admin')
                return redirect('login')



                
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
        formset = CoauthorFormset(request.POST or None)
        uploadform = UploadsForm(request.POST or None, request.FILES)
        manuscriptform = ManuscriptForm(request.POST or None)
        main_author = Author.objects.get(user=request.user)
        userr = User.objects.get(username=request.user)
        randvalue = random.randint(1,10000000)
        pending_status = Status.objects.get(pk=1)

        try: 
            form_user = CoauthorList.objects.get(name = request.user)
        except:
            form_user = CoauthorList.objects.create(name = request.user)

        
        if request.method == "POST":
            formset.instance = form_user
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.rand = randvalue
                    instance.save()
                        # formset.save()

            if  manuscriptform.is_valid():
                manuscriptform.instance.author = request.user
                manuscriptform.instance.status = pending_status
                manuscriptform.instance.rand = randvalue
                manuscriptform.save()
                
            if  uploadform.is_valid():
                uploadform.instance.author = userr
                uploadform.instance.rand = randvalue
                uploadform.save()
                messages.info(request, 'Your Manuscript Submitted Successfully, We will get back to you within 10 working days')
                return redirect('submit_script')

            
        context = {
            'userr':userr,
            'main_author':main_author,
            'formset':formset,
            'uploadform':uploadform,
            'manuscriptform':manuscriptform

        }
        return render(request, "dashboard/submit_script2.html", context)



def display_script(request):
    
        # uploadform = UploadsForm(request.POST or None, request.FILES)
    manuscriptform = Manuscript.objects.filter(author = request.user)
    try:
        Author = CoauthorList.objects.get(name = request.user)
        coauthorList = CoAuthors.objects.filter(author = Author)
    except:
        coauthorList = None

    uploadList = Uploads.objects.filter(author = request.user)
    
        # uploadform = UploadsForm(request.POST or None, request.FILES)


    context = {
        'manuscriptform': manuscriptform,
        'coauthorList':coauthorList,
        'uploadList':uploadList,
        # 'rand':rand,
    }
    return render(request, "dashboard/display_script.html", context)



def edit_script(request, rand):

    if request.method == "GET":
        # formset = CoauthorFormset(request.POST or None)
        main_author = Author.objects.get(user=request.user)
        userr = User.objects.get(username=request.user)


        manuscriptrand = Manuscript.objects.get(rand=rand)
        manuscriptform = ManuscriptForm(instance = manuscriptrand)



        uploadrand = Uploads.objects.get(rand=rand)
        uploadform = UploadsForm(instance = uploadrand)

        # coauthorrand = CoAuthors.objects.filter(rand=rand)
        form_user = CoauthorList.objects.get(name = request.user)
        formset = CoauthorFormset(instance = form_user, queryset=CoAuthors.objects.filter(rand=rand))

        context = {
                    'manuscriptform':manuscriptform,
                    'formset':formset,
                    'uploadform':uploadform,
                    'userr':userr,
                    'main_author':main_author,
                    }


        return render(request, "dashboard/submit_script2.html", context)
    


    else:
        # UNCOMPLETED EDIT SCRIPT! EDIT FORMSET STILL NOT WORKING
        # main_author = Author.objects.get(user=request.user)
        # userr = User.objects.get(username=request.user)
        pending_status = Status.objects.get(pk=1)
        form_user = CoauthorList.objects.get(name = request.user)
        coauthor = CoAuthors.objects.filter(rand=rand)
        formset = CoauthorListForm(request.POST, instance=form_user)
       
        # formset = CoauthorFormset(request.POST, instance = form_user, queryset=CoAuthors.objects.filter(rand=rand))


        manuscriptrand = Manuscript.objects.get(rand=rand)
        manuscriptform = ManuscriptForm(request.POST, instance = manuscriptrand)

        uploadrand = Uploads.objects.get(rand=rand)
        uploadform = UploadsForm(request.POST, request.FILES, instance = uploadrand)


        # formset.instance = form_user


        if formset.is_valid():
            # instances = formset.save(commit=False)
            # for instance in instances:
            #     instance.rand = rand
            #     instance.save()
            formset.save()

        if  manuscriptform.is_valid():
            instance = manuscriptform.save(commit=False)
            instance.status = pending_status
            instance.save()
            
        if  uploadform.is_valid():
            uploadform.save()
            messages.info(request, 'Your Manuscript has updated successfully')
            return redirect('display_script')

        # context = {
        #     'manuscriptform':manuscriptform,
        #     'formset':formset,
        #     'uploadform':uploadform,
        #     'userr':userr,
        #     'main_author':main_author,
        #         }
        # return render(request, "dashboard/submit_script2.html", context)






def delete_script(request, rand):
    manuscriptform = Manuscript.objects.get(rand=rand)
    manuscriptform.delete()
        
    coauthorList = CoAuthors.objects.filter(rand=rand)
    coauthorList.delete()

    uploadList = Uploads.objects.get(rand=rand)
    uploadList.delete()

    messages.info(request, 'Manuscript deleted Successfully')
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    context = {}
    return render(request, "", context)



def delete_user(request, id):
    check_user = User.objects.get(pk=id) 
    username = check_user.username
    coauthor_user = CoauthorList.objects.get(name = username) 
    user_verify = my_user.objects.get(username = username)
    manuscripts = Manuscript.objects.filter(author=id)
    try:
        manuscripts.delete()
        coauthor_user.delete()
        check_user.delete()  
        user_verify.delete()
    except:
        check_user.delete()  
        user_verify.delete()
    messages.info(request, 'User deleted Successfully')
    return redirect('all_users')   



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



def all_users(request):
    users = User.objects.all()

    context = {
        'users':users,
        # 'author':author,
    }
    return render(request, "editor/all_users.html", context)




def editor_overview(request):
    
    context = {
        
    }
    return render(request, "editor/overview.html", context)






def pending_journals(request):
    pendings = Manuscript.objects.filter(status=1, published_status = False)
    context = {'pendings':pendings,}
    return render(request, "editor/pending_journals.html", context)



def accepted_journals(request):
    accepted = Manuscript.objects.filter(status=4, published_status = False)
    




    context = {
            'accepted':accepted,
        
            }
    return render(request, "editor/accepted_journals.html", context)


def inreview_journals(request):  
    inreview = Manuscript.objects.filter(status=3, published_status = False)
    context = {'inreview':inreview,}
    return render(request, "editor/inreview_journals.html", context)


def revision_journals(request):
    revision = Manuscript.objects.filter(status=2, published_status = False)
    context = {'revision':revision,}
    return render(request, "editor/revision_journals.html", context)


def rejected_journals(request):   
    rejected = Manuscript.objects.filter(status=5, published_status = False)
    context = {'rejected':rejected,}
    return render(request, "editor/rejected_journals.html", context)



def full_details(request,rand): 

    main_author = Author.objects.get(user=request.user)
    userr = User.objects.get(username=request.user)


    manuscriptrand = Manuscript.objects.get(rand=rand)
    manuscriptform = ManuscriptFormEditor(instance = manuscriptrand)



    uploadrand = Uploads.objects.get(rand=rand)
    uploadform = UploadsForm(instance = uploadrand)

    # coauthorrand = CoAuthors.objects.filter(rand=rand)
    form_user = CoauthorList.objects.get(name = request.user)
    formset = CoauthorFormset(instance = form_user, queryset=CoAuthors.objects.filter(rand=rand))  

    if request.method == "POST":
        uploadrand = Uploads.objects.get(rand=rand)
        uploadform = UploadsForm(request.POST, request.FILES, instance = uploadrand)


        manuscriptrand = Manuscript.objects.get(rand=rand)
        manuscriptform = ManuscriptFormEditor(request.POST, instance = manuscriptrand)

        if  manuscriptform.is_valid():
            manuscriptform.save()
            
        if  uploadform.is_valid():
            uploadform.save()
            messages.info(request, 'Change added Successfully')
            return redirect('pending_journals')

        # uploadrand = Uploads.objects.get(rand=rand)
        # uploadform = UploadsForm(request.POST, request.FILES, instance = uploadrand)


    context = {
        'manuscriptform':manuscriptform,
        'formset':formset,
        'uploadform':uploadform,
        'userr':userr,
        'main_author':main_author,
        }
    return render(request, "editor/full_details.html", context)


def disable_user(request, id): 
    check_user = User.objects.get(pk=id)
    if check_user.is_active == True:
        check_user.is_active = False
        check_user.save()
        messages.info(request, 'User disabled')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        check_user = User.objects.get(pk=id)
        check_user.is_active = True
        check_user.save()
        messages.info(request, 'User Enabled')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        
    
    context = {}
    return render(request, "", context)



def journal_page(request,id):
    journals = Journal.objects.get(pk=id)
    manuscript = Manuscript.objects.filter(journal=journals,published_status = True)
    p = Paginator(manuscript, 6)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    except PageNotAnInteger:
        page = p.page(1)

    recent_manuscript = Manuscript.objects.order_by('-date_added')[0:3]
    
    
    context = {
                'journals':journals,
                'manuscript':page,
                'recent_manuscript':recent_manuscript,
                'page':page,
                'id':id,
    }
    return render(request, "journal.html", context)


def publish_journal(request,rand):
    publish_form = publishForm()
    # manuscriptform = ManuscriptForm()
    manuscriptrand = Manuscript.objects.get(rand=rand)
    manuscriptform = ManuscriptForm(instance=manuscriptrand)
    
    
    
    if request.method == "POST":
        manuscriptform = ManuscriptForm(request.POST, instance=manuscriptrand)
        publish_form = publishForm(request.POST or None, request.FILES)

        if publish_form.is_valid():
            publish_form.instance.rand = rand
            publish_form.instance.published_status = True
            publish_form.save()
            publish_form = publishForm() 

        
        if manuscriptform.is_valid():
            instance = manuscriptform.save(commit=False)
            instance.published_status = True
            instance.save()
            

        messages.info(request, 'Manuscript Published Successfully')
        return redirect('accepted_journals')
    
    context = {
            'manuscriptform':manuscriptform,
            'publish_form':publish_form,
    }
    return render(request, "editor/publish_journal.html", context)



def all_published(request):
    published = publish.objects.all()
    published_manuscript = Manuscript.objects.filter(published_status = True)
    objects_list = list(zip(published , published_manuscript))
    
    
    context = {
        # 'published':published,
        # 'published_manuscript':published_manuscript,
        'objects_list':objects_list,
        
    }
    return render(request, "editor/all_published.html", context)


def home(request):
    journals = Journal.objects.all()
    journal_count = Journal.objects.all().count()
    published = publish.objects.all()
    published_manuscript = Manuscript.objects.filter(published_status = True)
    objects_list = list(zip(published , published_manuscript))
    recent_manuscript = Manuscript.objects.all()[0:3]
    frontpage_sliders = front_page.objects.get(pk=1)

    context = {
        'journals':journals,
        'journal_count':journal_count,
        'objects_list':objects_list,
        'recent_manuscript':recent_manuscript,
        'frontpage_sliders':frontpage_sliders,
    }

    return render(request, "index.html", context)


def all_articles(request):
    journals = Journal.objects.all()
    journal_count = Journal.objects.all().count()
    published = publish.objects.all()
    p = Paginator(published, 8)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    published_manuscript = Manuscript.objects.filter(published_status = True)
    objects_list = list(zip(page, published_manuscript))
    recent_manuscript = Manuscript.objects.all()[0:3]

   

    context = {
        'journals':journals,
        'journal_count':journal_count,
        'objects_list':objects_list,
        'recent_manuscript':recent_manuscript,
        'page':page,
    }

    return render(request, "all_articles.html", context)


def article(request,rand):
    published = publish.objects.get(rand=rand,published_status=True)
    published_manuscript = Manuscript.objects.get(rand=rand,published_status=True)
    author = published_manuscript.author
    author_details = Author.objects.get(user=author)
    coauthors = CoAuthors.objects.filter(rand=rand)
 
    # objects_list = list(zip(published , published_manuscript))
    
    
    context = {
        'published':published,
        'published_manuscript':published_manuscript,
        'author_details':author_details,
        'coauthors':coauthors,
   
        
    }
    return render(request, "article.html", context)





