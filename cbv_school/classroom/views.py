from django.urls import reverse_lazy
from django.views.generic import (TemplateView, FormView,
                                  CreateView, ListView,
                                  DetailView, UpdateView,
                                  DeleteView)
from .forms import ContactForm
from .models import Teacher

# Create your views here.


# def home_view(request):
#     return render(request, 'classroom/home.html')


class HomeView(TemplateView):
    template_name = 'classroom/home.html'  # that's enough to render template


class ThankView(TemplateView):
    template_name = 'classroom/thank_you.html'

# TemplateViews should be used in cases where all work will be done inside template


class TeacherCreateView(CreateView):
    # for generic views working with models there is a convention how templates should be named:
    # model_form.html -> i.e. teacher_form.html\
    # does .save() if all fields are valid
    # !! creates a new instance
    model = Teacher # 1st step
    # fields = ['first_name', 'subject']  # choose fields you want to work with
    fields = "__all__"  # if you want to use all fields
    success_url = reverse_lazy('classroom:thank_you')


class TeacherListView(ListView):
    # --> model_list.html
    model = Teacher
    # by default queryset = Teacher.objects.all()
    queryset = Teacher.objects.order_by('first_name')  # dunno why it's ordering in reverse. use minus
    # in case if you want to change name of variable for context instead of using default "object_list"
    context_object_name = "teacher_list"


class TeacherDetailView(DetailView):
    # returns only one entry from a model using their PK
    # --> model_detail.html
    model = Teacher
    # finds PK then sends it to context teacher


class TeacherUdpateView(UpdateView):
    # share model_form.html but for specific PK
    model = Teacher
    # fields = ['last_name']  # fields you want to allow to update
    fields = '__all__'
    success_url = reverse_lazy('classroom:list_teacher')


class TeacherDeleteView(DeleteView):
    # form --> confirm delete button
    # default template name:
    # model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')


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
