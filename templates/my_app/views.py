from django.shortcuts import render


# Create your views here.
def example_view(request):
    return render(request, 'my_app/example.html')


def variable_view(request):

    my_var = {'first_name': 'BUBUBL', 'last_name': 'kake',
              'some_list': [1, 2, 3], 'some_dict': {'some_key': 'some_value'},
              'if_dict': {'user_auth': True}
              }

    return render(request, 'my_app/variable.html', context=my_var)
