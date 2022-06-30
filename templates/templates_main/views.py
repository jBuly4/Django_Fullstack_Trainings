from django.shortcuts import render

def custom_error_404_view(request, exception):

    return render(request, 'error_view.html', status=404)