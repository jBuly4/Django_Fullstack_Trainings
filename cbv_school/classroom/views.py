from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactForm

# Create your views here.


# def home_view(request):
#     return render(request, 'classroom/home.html')


class HomeView(TemplateView):
    template_name = 'classroom/home.html'  # that's enough to render template


class ThankView(TemplateView):
    template_name = 'classroom/thank_you.html'

# TemplateViews should be used in cases where all work will be done inside template


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # what to do after success? where to redirect?
    # success_url = '/classroom/thank_you/'  # raw url not a template
    # also you can use reverse_lazy('classroom:thank_you') just like reverse in function base views
    success_url = reverse_lazy('classroom:thank_you')

    # what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        # ContactForm(request.POST)
        return super().form_valid(form)