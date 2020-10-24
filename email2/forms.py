from django import forms
from email2.models import Sendemail

class SendemailForm(forms.Form):
	class Meta:
		model:Sendemail
		fields='__all__'
		