from django.shortcuts import render
from.models import Sendemail
from django.core.mail import send_mail
# Create your views here.
def send_email(request):
	obj=Sendemail.objects.first()

	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		description=request.POST['description']

		print(name)
		print(email)
		print(description)

	return render(request,'send_form.html')