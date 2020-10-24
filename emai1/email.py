from django.templates import Context
from django.templates import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings



def send_review_email(name,email,review):
	context={
		'name':name,
		'email':email,
		'review':review
	}