from django import forms


class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)  # explanation find in dojango docs
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='email')
    review = forms.CharField(label='Please write your review here',
                             widget=forms.Textarea(
                                     attrs={'class': 'myform',
                                            'rows': '2',
                                            'cols': '2'  # if we need to play with width of textarea
                                            }
                             ))

"""
after creating a form -> views import form -> change a view
all fields have many parameters. one of them is widget. 
read the docs to understand how changes of widget will change forms view
attrs -> dict with params -> styling class. that will allow to style exactly this form. -> no need to use myform in 
html for all forms
but you can do it only inside widget parameter.
"""