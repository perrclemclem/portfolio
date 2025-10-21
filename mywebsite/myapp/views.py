from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
    """Shows the home page"""
    allproduct = Product.objects.all()
    context = {'pd': allproduct}
    return render(request, 'myapp/home.html', context)

def aboutUs(request):
    """Shows the about us page"""
    return render(request, 'myapp/aboutus.html')

def contact(request):
    """
    Shows the contact page, 
    sends information on the contact request in the database when the topic, 
    email and details of the contact demand are filled 
    and the submit button has been clicked.
    """

    context = {} #messge to notify

    if request.method == 'POST':
        data = request.POST.copy()
        topic = data.get('topic')
        email = data.get('email')
        detail = data.get('detail')

        if (topic == '' or email == '' or detail == ''):
            context['message'] = 'Please, fill in all contact informations'
            return render(request, 'myapp/contact.html', context)

        newRecord = contactList() # create object
        newRecord.topic = topic
        newRecord.email = email
        newRecord.detail = detail
        newRecord.save() # save data

        context['message'] = 'The message has been received'

    return render(request, 'myapp/contact.html', context)

def userLogin(request):
    """
    Shows the login page,
    when login information has been filled and login button clicked, 
    if the login info is right, redirects to the home page,
    else comes back to login page again with "username or password is incorrect." message.
    """
    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        username  = data.get('username')
        password = data.get('password')

        try:
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home-page')
        except:
            context['message'] = "username or password is incorrect."
    
    return render(request, 'myapp/login.html', context)

@login_required(login_url='/login')
def showContact(request):
    """
    Shows the show contact page if the user is already logged in, 
    shows the previous contact demands sent
    """
    allcontact = contactList.objects.all()
    context = {'contact': allcontact}
    return render(request, 'myapp/showcontact.html, context')


def userRegist(request):
    """
    Shows the register page.
    When the neccessary information has been filled and submit button clicked, 
    if the username is already used by someone else, 
    shows "Username duplicate" message and the user can modify the information
    if the username is okay but the password and re-password given are not the same,
    shows "password or re-password is incorrect" message and the user can modify the information.
    else shows message "register complete".
    """
    context = {}

    if request.method == 'POST':
        data =request.POST.copy()
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        repassword = data.get('repassword')

        try:
            User.objects.get(username=username)
            context['message'] = "Username duplicate"
        except:
            newuser = User()
            newuser.username = username
            newuser.first_name = firstname
            newuser.last_name = lastname
            newuser.email =email
            
            if (password == repassword):
                newuser.set_password(password)
                newuser.save()
                newprofile = Profile()
                newprofile.user = User.objects.get(username=username)
                newprofile.save()
                context['message'] = "register complete"
            else:
                context['message'] = "password or re-password is incorrect"
    return render(request, 'myapp/register.html', context)

def userProfile(request):
    """
    Shows profile page with the profile information of the user
    (page only available if the user is already logged in)
    if the user clicks on the edit profile button,
    redirects to the edit profile page. 
    """
    context = {}
    userprofile = Profile.objects.get(user=request.user)
    context['profile'] = userprofile
    return render(request, 'myapp/profile.html', context)

def editProfile(request):
    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        current_user = User.objects.get(id=request.user.id)
        current_user.first_name = firstname
        current_user.last_name = lastname
        current_user.username = username
        current_user.email = email
        current_user.set_password(password)
        current_user.save()

        try:
            user = authentificate(username=current_user.username,
                                    password=current_user.password)
            login(request, user)
            return redirect('home-page')
        except:
            context['message'] = "edit profile fail"
    
    return render(request, 'myapp/editprofile.html')

def actionPage(request, cid):
    """No idea, don't remember ;-;"""
    # cid = contactlist ID
    context = {}
    contect = contactList.objects.get(id=cid)
    context['contact'] = contact

    try:
        action = Action.objects.get(contactList=contact)
        context['action'] = action
    except:
        pass

    if request.method == 'POST':
        data = request.POST.copy()
        actiondetail = data.get('actiondetail')

        if 'save' in data:
            try:
                check = Action.objects.get(contactList=contact)
                check.actionDetail = actiondetail
                check.save()
                contaxt['action'] = check
            except:
                new = Action.objects.get(contactList=contact)
                new.contactList = contact
                new.actionDetail = actiondetail
                new.save()
        elif 'complete' in data:
            contact.complete = True
            contact.save()
            return redirect(request, 'myapp/action.html', context)
        
    return render(request, 'myapp/action.html', context)

def addProduct(request):
    """
    Shows add product page 
    (only if user is an admin and is already logged in)
    if user fills all the information and clicks on the add product button, 
    the product is added to the database with an eventual image and other file.
    """
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        description = data.gat('description')
        price = data.get('price')
        quantity = data.get('quantity')
        instock = data.get('instock')

        new = Product()
        new.title = title
        new.descrition = description
        new.price = float(price)
        new.quantity = int(quantity)

        if instock == "instock":
            new.instock = True
        else:
            new.instock = False

        if 'picture' in request.FILES:
            file_image = request.FILES['picture']
            file_image_name = file_image.name.replace(' ', '')
            # File system: from django.core.files.storage import FileSystemStorage
            fs = FileSystemStorage(location='media/product')
            filename = fs.save(file_image_name, file_image)
            upload_file_url = fs.url(fiename)
            print('Picture url:', upload_file_url)
            new.picture = 'product' + upload_file_url[6:]

        if 'specfile' in request.FILES:
            file_specfile = request.FILES['picture']
            file_specfile_name = file_specfile.name.replace(' ', '')
            # File system: from django.core.files.storage import FileSystemStorage
            fs = FileSystemStorage(location='media/specfile')
            filename = fs.save(file_specfile_name, file_specfile)
            upload_file_url = fs.url(fiename)
            print('Picture url:', upload_file_url)
            new.picture = 'product' + upload_file_url[6:]

        new.save()

        print(title)
        print(description)
        print(price)
        print(quantity)
        print(instock)
        print('File:', request.FILES)

    return render(request, 'myapp/addproduct.html')