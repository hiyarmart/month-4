from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.urls import reverse
from django.http import HttpResponse
from django.views import generic


class ShowlistView(generic.ListView):
    template_name = 'shows/show_list.html'
    model = models.Show

    def get_queryset(self):
        return self.model.objects.all()


class ShowDetailView(generic.DetailView):
    template_name = 'shows/show_detail.html'
    context_object_name = 'show_id'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Show, id=show_id)


class ShowCreateView(generic.CreateView):
    template_name = 'crud/create_show.html'
    model = models.Show
    form_class = forms.ShowForm
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ShowCreateView, self).form_valid(form=form)


def show_list_delete_view(request):
    if request.method == 'GET':
        show_delete = models.Show.objects.all()
        return render(request, template_name='crud/delete/show_list_delete.html',
                      context={'show_delete': show_delete})

def show_id_key(request, id):
    if request.method == "GET":
        show_id_ml = get_object_or_404(models.Show, id=id)
        return render(request, template_name='shows/show_id_key.html',
                      context={'show_id_ml': show_id_ml})


class ShowDropView(generic.DeleteView):
    template_name = 'crud/delete/confirm_delete.html'
    success_url = '/show_list_delete/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Show, id=show_id)


def show_list_edit_view(request):
    if request.method == 'GET':
        show_update = models.Show.objects.all()
        return render(request, template_name='crud/update/show_list_update.html',
                      context={'show_update': show_update})

class ShowUpdateView(generic.UpdateView):
    template_name = 'crud/update/show_update.html'
    form_class = forms.ShowForm
    success_url = '/show_list_update/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Show, id=show_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ShowUpdateView, self).form_valid(form=form)

class SearchView(generic.ListView):
    template_name = 'shows/show_list.html'
    paginate_by = 5

    def get_queryset(self):
        return models.Show.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context






































# from django.shortcuts import render, get_object_or_404, redirect
# from . import models, forms
# from django.urls import reverse
# from django.http import HttpResponse
#
#
# def show_list(request):
#     if request.method == 'GET':
#         shows = models.Show.objects.all()
#         return render(request, template_name='shows/show_list.html',
#                       context={'shows': shows})
#
#
# def show_detail(request, id):
#     if request.method == "GET":
#         show_id = get_object_or_404(models.Show, id=id)
#         return render(request, template_name='shows/show_detail.html',
#                       context={'show_id': show_id})
#
#

#
# def show_create_view(request):
#     if request.method == "POST":
#         form = forms.ShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('show_list'))
#     else:
#         form = forms.ShowForm()
#         return render(request, template_name='crud/create_show.html',
#                       context={"form": form})
#
#
# def show_list_delete_view(request):
#     if request.method == 'GET':
#         show_delete = models.Show.objects.all()
#         return render(request, template_name='crud/delete/show_list_delete.html',
#                       context={'show_delete': show_delete})
#
# def show_drop_view(request, id):
#     show_id = get_object_or_404(models.Show, id=id)
#     show_id.delete()
#     return redirect(reverse('show_list_delete'))
#
# # ________________________
#
# def show_list_edit_view(request):
#     if request.method == 'GET':
#         show_update = models.Show.objects.all()
#         return render(request, template_name='crud/update/show_list_update.html',
#                       context={'show_update': show_update})
#
#
#
#
# def show_update(request, id):
#     show_id = get_object_or_404(models.Show, id=id)
#
#     if request.method == 'POST':
#         form = forms.ShowForm(instance=show_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('show_list_update'))
#     else:
#         form = forms.ShowForm(instance=show_id)
#
#     return render(request, template_name='crud/update/show_update.html', context={
#         "form": form,
#         "show_id": show_id
#     })


