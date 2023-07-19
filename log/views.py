from django.shortcuts import render, redirect
from .forms import SetPasswordForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
def navredirect():
	return redirect("nav")
def login_request(request):
	x=False
	clicked=False
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			clicked=True
			if user is not None:
				login(request,user)
				return redirect("nav")
				
			else:
				x=True
				
		else:
			x=True
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form, "x":x, "clicked":clicked})
def register(request):
	context={}
	form=CreateUserForm
	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	
	return render(request,'register.html',{"form":form})
@login_required
def pagelogout(request):
    logout(request)
    return redirect('home')
    
def ResetPassView(request):
	return render(request,"reset.html",{})
@login_required
def setPass(request):
	user=request.user
	if request.method == "POST":
		form =SetPasswordForm(user,request.POST)
		if form.is_valid():
			return redirect('login')
			messages.success(request,"your password has successfully been changed")
		else:
			for error in list(form.errors.values()):
				messages.error(request,error)

	form= SetPasswordForm(user)
	return render(request, "setpass.html",{'form':form})

@login_required
class PasswordChangeView(PasswordChangeView):
	pass
