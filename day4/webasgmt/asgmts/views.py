from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.urls import reverse
from django.views import generic, View

from .models import Sneaker
from .forms import SneakerForm


# Create your views here.
def introduction(request):
    return render(request, 'introduction.html')


# class IndexView(generic.ListView):
#     template_name = 'index.html'
    
#     def get_queryset(self):
#         return Sneaker.objects.all()

class IndexView(View):
    form_class = SneakerForm
    template_post = 'post_form.html'
    template_detail = 'detail.html'

    def get_queryset(self):
        return Sneaker.objects.all()

    def get(self, request, *args, **kwargs):
        sneaker_list = self.get_queryset()
        render_params = {'sneaker_list': sneaker_list}
        
        if (pk := self.kwargs.get('pk')):
            obj = get_object_or_404(Sneaker, id=pk)
            form = self.form_class(instance=obj)

            render_params['obj'] = obj
            template_to_render = self.template_detail
        else:
            template_to_render = self.template_post
            form = self.form_class    
        
        render_params['sneaker_form'] = form
        return render(request, template_to_render, render_params)

    def post(self, request, *args, **kwargs):
        if (pk := self.kwargs.get('pk')):
            obj = get_object_or_404(Sneaker, id=pk)

        if request.POST.get('DELETE', '') == 'Delete':
            obj.delete()
            return redirect('post_form')
        
        form = self.form_class(request.POST, instance=obj)
        if form.is_valid():
            if request.POST.get('UPDATE', '') == 'Update':
                obj = form.save(commit=False)
                obj.save()
            else:
                form.save()
        return HttpResponseRedirect(self.request.path_info)
