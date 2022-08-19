from django import forms


class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)  # explanation find in dojango docs
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='email')
    review = forms.CharField(label='Please write your review here')

"""
after creating a form -> views import form -> change a view"""