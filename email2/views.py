from django.shortcuts import render
from.models import Sendemail
from django.core.mail import send_mail
from.forms import SendemailForm
# Create your views here.
def send_email(request):
	obj=Sendemail.object.first()
	if request.method=='POST':
		subject=request.POST['subject']
		email=request.POST['email']
		message=request.POST['message']

		
		context={'obj':obj}
	return render(request,'send_form.html',context)