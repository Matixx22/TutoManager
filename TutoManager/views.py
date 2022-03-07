from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from .forms import EntryForm
from .models import Entry


class IndexView(ListView):
    template_name = 'TutoManager/index.html'
    context_object_name = 'entry_list'

    def get_queryset(self):
        return Entry.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        price_sum = sum(e.price for e in Entry.objects.all())

        context['sum'] = price_sum
        return context


class AddView(CreateView):
    model = Entry
    template_name = 'TutoManager/add.html'

    form_class = EntryForm

    def get_success_url(self):
        return reverse('TutoManager:index')


class EditView(UpdateView):
    model = Entry
    template_name = 'TutoManager/edit.html'

    form_class = EntryForm

    def get_success_url(self):
        return reverse('TutoManager:index')
