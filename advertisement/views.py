#coding: utf-8

from django.shortcuts import get_object_or_404
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
# from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.views import generic
from django.contrib import auth
from django.core.paginator import Paginator

from .models import Bicycle, Ski
from .forms import BicycleForm, SkiForm

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

# def list(request, page_number=1):
#     args = {}
#     adv_list = Advertisement.objects.order_by('-date')
#     current_page = Paginator(adv_list, 6)
#     args['adv_list'] = current_page.page(page_number)
#     # args['username'] = request.user.username
#     return render(request, 'advertisement/list.html', args )
#
# def view(request, advertisement_id):
#     args = {}
#     args['adv_list'] = get_object_or_404(Advertisement, id=advertisement_id)
#     args['username'] = request.user.username
#     return render(request, 'advertisement/view.html', args)
#
# def new(request):
#     # @login_required
#     args = {}
#     if not request.user.is_authenticated():
#         return render(request, 'user/login_error.html')
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             advertisement = form.save(commit=False)
#             advertisement.ident = 123
#             advertisement.user = User.objects.get(id=request.user.id) #auth.get_user(request).id
#             advertisement.save()
#             return redirect('view', advertisement_id=advertisement.pk)
#     else:
#         args['form'] = NameForm()
#         args['username'] = request.user.username
#         return render(request, 'advertisement/new.html', args )
#
# def edit(request, advertisement_id):
#     args = {}
#     if not request.user.is_authenticated():
#         return render(request, 'user/login_error.html')
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             advertisement = form.save(commit=False)
#             advertisement.ident = 123
#             advertisement.user = User.objects.get(id=request.user.id)
#             advertisement.save()
#             return redirect('view', advertisement_id=advertisement.pk)
#     else:
#         advertisement = Advertisement.objects.get(pk=advertisement_id)
#         args['form'] = NameForm(instance=advertisement)
#         args['advertisement_id'] = advertisement_id
#         args['username'] = request.user.username #auth.get_user(request).username
#         return render(request, 'advertisement/edit.html', args )

####### BICYCLE ######
def bicycles(request, page_number=1):
    args = {}
    bicycles = Bicycle.objects.order_by('-date')
    current_page = Paginator(bicycles, 1)
    args['bicycles'] = current_page.page(page_number)
    return render(request, 'advertisement/list_bicycle.html', args )

def new_bicycle(request):
    # @login_required
    args = {}
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    if request.method == 'POST':
        form = BicycleForm(request.POST)
        if form.is_valid():
            bicycle = form.save(commit=False)
            bicycle.ident = 123
            bicycle.user_id = User.objects.get(id=request.user.id) #auth.get_user(request).id
            bicycle.save()
            return redirect('view_bicycle', bicycle_id=bicycle.pk)
    else:
        args['form'] = BicycleForm()
        args['username'] = request.user.username
        return render(request, 'advertisement/new_bicycle.html', args )

def view_bicycle(request, bicycle_id):
    args = {}
    args['bicycle'] = get_object_or_404(Bicycle, id=bicycle_id)
    args['username'] = request.user.username
    return render(request, 'advertisement/view_bicycle.html', args)

def edit_bicycle(request, bicycle_id):
    args = {}
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    if request.method == 'POST':
        form = BicycleForm(request.POST)
        if form.is_valid():
            bicycle = form.save(commit=False)
            bicycle.ident = 123
            bicycle.user_id = User.objects.get(id=request.user.id)
            bicycle.id = bicycle_id
            bicycle.save( update_fields=['title', 'note', 'price', 'ident', 'year', 'size', 'weight', 'bicycle_type'],
                          force_update='True')
            return redirect('view_bicycle', bicycle_id=bicycle.id)
    else:
        bicycle = Bicycle.objects.get(id=bicycle_id)
        args['form'] = BicycleForm(instance=bicycle)
        args['bicycle_id'] = bicycle_id
        args['username'] = request.user.username #auth.get_user(request).username
        return render(request, 'advertisement/edit_bicycle.html', args )

####### SKI ######
def skis(request, page_number=1):
    args = {}
    skis = Ski.objects.order_by('-date')
    current_page = Paginator(skis, 1)
    args['skis'] = current_page.page(page_number)
    return render(request, 'advertisement/list_ski.html', args )

def new_ski(request):
    # @login_required
    args = {}
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    if request.method == 'POST':
        form = SkiForm(request.POST)
        if form.is_valid():
            ski = form.save(commit=False)
            ski.ident = 123
            ski.user_id = User.objects.get(id=request.user.id) #auth.get_user(request).id
            ski.save()
            return redirect('view_ski', ski_id=ski.pk)
    else:
        args['form'] = SkiForm()
        args['username'] = request.user.username
        return render(request, 'advertisement/new_ski.html', args )

def view_ski(request, ski_id):
    args = {}
    args['ski'] = get_object_or_404(Ski, id=ski_id)
    args['username'] = request.user.username
    return render(request, 'advertisement/view_ski.html', args)

def edit_ski(request, ski_id):
    args = {}
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    if request.method == 'POST':
        form = SkiForm(request.POST)
        if form.is_valid():
            ski = form.save(commit=False)
            ski.ident = 123
            ski.user_id = User.objects.get(id=request.user.id)
            ski.id = ski_id
            ski.save( update_fields=['title', 'note', 'price', 'ident', 'year', 'size', 'weight', 'for_weight', 'ski_type'],
                          force_update='True')
            return redirect('view_ski', ski_id=ski.id)
    else:
        ski = Ski.objects.get(id=ski_id)
        args['form'] = SkiForm(instance=ski)
        args['ski_id'] = ski_id
        args['username'] = request.user.username #auth.get_user(request).username
        return render(request, 'advertisement/edit_ski.html', args )
