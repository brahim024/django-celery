from django import forms

class ReviewForm(forms.Form):
	name=forms.CharField(
		label='Firstname',min_length=4,max_length='50',widget=forms.TextInput(
			attrs={'class':'form-conrol mb-3','placeholder','Firstname','id':'form-firstname'}))

	email=forms.EmailField(
		max_length=200,widget=forms.TextInput(
			attrs={'class':'form-control mb-3','placeholder','Email','id':'form-firstname'}))

	review=forms.CharField(
			label='Review',widget=forms.Textarea(attrs={'class':'form-control','row':'5'})
			
		)