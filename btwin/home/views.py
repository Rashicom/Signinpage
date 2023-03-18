
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store = True)
def login(request):

    # if methord is POST
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)

        # password varification
        # if credencial matched
        if username == 'rashi' and password == '123':
            request.session['username'] = username
            return render(request,'home.html')
        
        # if credencial not matced
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    # if methord is GET
    else:
        if 'username' in request.session:
            # check the render vs redirect
            return render(request,'home.html') 
        else:
            return render(request,'login.html')


def homepage(request):
    if 'username' in request.session:
        return render(request,'home.html')
    else:
        return redirect('login')
# logout function


def logout(request):
    request.session.flush()
    return redirect('login')


    

# Create your views here.
