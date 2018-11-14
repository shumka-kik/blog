from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def login_user(request):
	if request.method == "POST":
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = authenticate(request, username=username, password=password)
	
		if user is not None:
			login(request, user)
			# redirect to a success page
			return HttpResponseRedirect(reverse('blog:main'))
		else:
			# retutn to an invalid error message
			messages.error(request, "Bad username or password")
	return render(request, 'accounts/login.html', {})
	