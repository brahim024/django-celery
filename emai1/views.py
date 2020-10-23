from django.shortcuts import render
from emai1.forms import ReviewForm
from django.http import HttpResponse
# Create your views here.
class ReviewForm(FormView):
	template_name='review.html'
	form_class=ReviewForm
	def form_valid(self,form):
		form.send_email()
		msg='Thank for the review !'
		return HttpResponse(msg)

