#coding: utf-8

from django.shortcuts import get_object_or_404
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
# from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.views import generic
from django.contrib import auth
from django.core.paginator import Paginator

from .models import Advertisement, Bicycle
from .forms import NameForm, BicycleForm

# научиться передавать пользователя в Index и Detail (или отказаться от их использования)
# передвать пользователя в глобальный шаблон (глобальная переменная?)

# class AdvListView(generic.ListView):
#   template_name = 'advertisement/index.html'
#   context_object_name = 'latest_advertisement_list'
#   paginate_by = 2
#
#   def get_queryset(self):
#     return Advertisement.objects.order_by('-date')#[:5]

# class AdvDetailView(generic.DetailView):
#     model = Advertisement
#     template_name = 'advertisement/view.html'
#     context_object_name = 'latest_advertisement_list'

def list(request, page_number=1):
    args = {}
    adv_list = Advertisement.objects.order_by('-date')
    current_page = Paginator(adv_list, 6)
    args['adv_list'] = current_page.page(page_number)
    # args['username'] = request.user.username
    return render(request, 'advertisement/list.html', args )

def view(request, advertisement_id):
    args = {}
    args['adv_list'] = get_object_or_404(Advertisement, id=advertisement_id)
    args['username'] = request.user.username
    return render(request, 'advertisement/view.html', args)

def new(request):
    # @login_required
    args = {}
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.ident = 123
            advertisement.user = User.objects.get(id=request.user.id) #auth.get_user(request).id
            advertisement.save()
            return redirect('view', advertisement_id=advertisement.pk)
    else:
        args['form'] = NameForm()
        args['username'] = request.user.username
        return render(request, 'advertisement/new.html', args )

def edit(request, advertisement_id):
    args = {}
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.ident = 123
            advertisement.user = User.objects.get(id=request.user.id)
            advertisement.save()
            return redirect('view', advertisement_id=advertisement.pk)
    else:
        advertisement = Advertisement.objects.get(pk=advertisement_id)
        args['form'] = NameForm(instance=advertisement)
        args['advertisement_id'] = advertisement_id
        args['username'] = request.user.username #auth.get_user(request).username
        return render(request, 'advertisement/edit.html', args )

####### BICYCLE ######

def view_bicycle(request, advertisement_id):
    args = {}
    # args['adv_list'] = get_object_or_404(Advertisement, id=advertisement_id)
    args['bicycle_list'] = get_object_or_404(Bicycle, advertisement=advertisement_id)
    args['id'] = advertisement_id
    args['username'] = request.user.username
    return render(request, 'advertisement/view_bicycle.html', args)

def edit_bicycle(request, advertisement_id):
    args = {}
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    if request.method == 'POST':
        form = BicycleForm(request.POST)
        if form.is_valid():
            bicycle = form.save(commit=False)
            bicycle.ident = 123
            bicycle.user = User.objects.get(id=request.user.id)
            bicycle.save()
            return redirect('view_bicycle', advertisement_id=bicycle.advertisement)
    else:
        bicycle = Bicycle.objects.get(advertisement=advertisement_id)
        args['form'] = BicycleForm(instance=bicycle)
        args['advertisement_id'] = advertisement_id
        args['username'] = request.user.username #auth.get_user(request).username
        return render(request, 'advertisement/edit_bicycle.html', args )
