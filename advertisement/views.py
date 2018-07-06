#coding: utf-8
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
# from django.http import HttpResponseRedirect
from django.http import QueryDict

from django.contrib.auth.models import User
from django.views import generic, View
from django.contrib import auth
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType

# from django.core.urlresolvers import reverse

from PIL import Image

import os
# import urlparse
# import urllib

from .models import Advertisement, Bicycle, Ski, AdvertisementType
from photos.models import Photo
from .forms import BicycleForm, SkiForm, BaseFilterForm, BicycleFilterForm, AdvUserFilterForm


def categories(request):
    return render(request, 'advertisement/categories.html')

####### USER_ADV #######
def user_advertisements(request, user_id, page_number=1):
    args = {}
    args['user_id'] = user_id
    advertisements = Advertisement.objects.filter(user_id=user_id).order_by('-date')
    filter_form = AdvUserFilterForm(request.GET)

    # отфильтровываем данные из запроса
    if filter_form.is_valid():
        if filter_form.cleaned_data["price_min"]:
            advertisements = advertisements.filter(price__gte=filter_form.cleaned_data["price_min"])
        if filter_form.cleaned_data["price_max"]:
            advertisements = advertisements.filter(price__lte=filter_form.cleaned_data["price_max"])
        if filter_form.cleaned_data["weight_min"]:
            advertisements = advertisements.filter(weight__gte=filter_form.cleaned_data["weight_min"])
        if filter_form.cleaned_data["weight_max"]:
            advertisements = advertisements.filter(weight__lte=filter_form.cleaned_data["weight_max"])


        if filter_form.cleaned_data["adv_type"]:
            advertisements = advertisements.filter(adv_type__in=request.GET.getlist("adv_type"))

    current_page = Paginator(advertisements, 5)
    args['advertisements'] = current_page.page(page_number)
    for bicycle in args['advertisements']:
        if bicycle.photos.first():
            print(bicycle.photos.first().file_small.url)

    args['filter_form'] = filter_form
    return render(request, 'advertisement/user/adv_user_list.html', args )


####### BICYCLE #######
def bicycles(request, page_number=1):
    args = {}
    bicycles = Bicycle.objects.order_by('-date')
    filter_form = BicycleFilterForm(request.GET)

    # отфильтровываем данные из запроса
    if filter_form.is_valid():
        if filter_form.cleaned_data["price_min"]:
            bicycles = bicycles.filter(price__gte=filter_form.cleaned_data["price_min"])
        if filter_form.cleaned_data["price_max"]:
            bicycles = bicycles.filter(price__lte=filter_form.cleaned_data["price_max"])
        if filter_form.cleaned_data["weight_min"]:
            bicycles = bicycles.filter(weight__gte=filter_form.cleaned_data["weight_min"])
        if filter_form.cleaned_data["weight_max"]:
            bicycles = bicycles.filter(weight__lte=filter_form.cleaned_data["weight_max"])

        # if filter_form.cleaned_data["bicycle_type"]:
        #     bicycles = bicycles.filter(bicycle_type=filter_form.cleaned_data["bicycle_type"])

        if filter_form.cleaned_data["bicycle_type"]:
            bicycles = bicycles.filter(bicycle_type__in=request.GET.getlist("bicycle_type"))
        if filter_form.cleaned_data["jumper_front"]:
            bicycles = bicycles.filter(jumper_front__in=request.GET.getlist("jumper_front"))
        if filter_form.cleaned_data["jumper_back"]:
            bicycles = bicycles.filter(jumper_back__in=request.GET.getlist("jumper_back"))

    current_page = Paginator(bicycles, 5)
    args['bicycles'] = current_page.page(page_number)
    for bicycle in args['bicycles']:
        if bicycle.photos.first():
            print(bicycle.photos.first().file_small.url)

    args['filter_form'] = filter_form
    return render(request, 'advertisement/bicycle/list_bicycle.html', args )


# def new_bicycle(request):
#     if not request.user.is_authenticated():
#         return render(request, 'user/login_error.html')
#     args = {}
#     if request.method == 'POST':
#         formBicycle = BicycleForm(request.POST)
#         formSet = ImageFormSet(request.POST, request.FILES,
#                                queryset=Images.objects.none())
#
#         if formBicycle.is_valid() and formSet.is_valid():
#             bicycle = formBicycle.save(commit=False)
#             bicycle.user = request.user
#             bicycle.adv_type = AdvertisementType.objects.filter(code='Велосипед')[0]
#             bicycle.save()
#
#             for form in formSet.cleaned_data:
#                 image = form['image']
#                 photo = Images(advertisement=bicycle, image=image)
#                 photo.save()
#             # return redirect('view_bicycle', adv_id=bicycle.pk)
#             data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
#         else:
#             # print formBicycle.errors, formSet.errors
#             data = {'is_valid': False}
#         return JsonResponse(data)
#     else:
#         formBicycle = BicycleForm()
#         formSet = ImageFormSet(queryset=Images.objects.none())
#
#         args['form'] = formBicycle
#         args['formset'] = formSet
#         args['username'] = request.user.username
#     return render(request, 'advertisement/bicycle/new_bicycle.html', args )

def new_bicycle(request):
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    args = {}
    if request.method == 'POST':
        formBicycle = BicycleForm(request.POST)

        if formBicycle.is_valid():
            bicycle = formBicycle.save(commit=False)
            bicycle.user = request.user
            bicycle.adv_type = AdvertisementType.objects.filter(code='Велосипед')[0]
            bicycle.save()

            # return redirect('view_bicycle', adv_id=bicycle.pk)
            # перенаправляем на страницу добавления фотографий
            return redirect('photos:advertisement_photo_edit', adv_id=bicycle.pk)
        else:
            print formBicycle.errors
    else:
        formBicycle = BicycleForm()

        args['form'] = formBicycle
        args['username'] = request.user.username
    return render(request, 'advertisement/bicycle/new_bicycle.html', args )

def view_bicycle(request, adv_id):
    args = {}
    args['bicycle'] = get_object_or_404(Bicycle, id=adv_id)
    args['photos'] = Photo.objects.filter(advertisement = adv_id)
    for photo in args['photos']:
        print(photo.file_medium.url)
        # print(image.image_medium.width)


    args['username'] = request.user.username
    return render(request, 'advertisement/bicycle/view_bicycle.html', args)

def edit_bicycle(request, adv_id):
    args = {}
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')

    if request.method == 'POST':
        form = BicycleForm(request.POST)
        if form.is_valid():
            bicycle = form.save(commit=False)
            bicycle.user = User.objects.get(id=request.user.id)
            bicycle.id = adv_id
            bicycle.save( update_fields=['title', 'note', 'price', 'year', 'size',
                                         'weight', 'bicycle_type', 'jumper_front', 'jumper_back'],
                          force_update='True')
            return redirect('view_bicycle', adv_id=bicycle.id)
    else:
        bicycle = Bicycle.objects.get(id=adv_id)
        # проверяем права на редактирование
        if not User.objects.get(id=request.user.id) == bicycle.user:
            return redirect('view_bicycle', adv_id=adv_id)
        args['form'] = BicycleForm(instance=bicycle)
        args['adv_id'] = adv_id
        args['username'] = request.user.username #auth.get_user(request).username
        return render(request, 'advertisement/bicycle/edit_bicycle.html', args )

def delete_bicycle(request, adv_id):
    bicycle = Bicycle.objects.get(id=adv_id)
    # проверяем права на удаление
    if not User.objects.get(id=request.user.id) == bicycle.user:
        return redirect('view_bicycle', adv_id=adv_id)
    else:
        bicycle.delete()
        return redirect('bicycles')
        # for image in bicycle.photo.all():
        #     image.delete()
        # os.remove('/home/sc04dlv/diplom/project/marketplace/' + image.image.url)



####### SKI ######
def skis(request, page_number=1):
    args = {}
    skis = Ski.objects.order_by('-date')
    current_page = Paginator(skis, 2)
    args['skis'] = current_page.page(page_number)
    return render(request, 'advertisement/ski/list_ski.html', args )

def new_ski(request):
    # @login_required
    args = {}
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    if request.method == 'POST':
        form = SkiForm(request.POST)
        if form.is_valid():
            ski = form.save(commit=False)
            ski.user = User.objects.get(id=request.user.id) #auth.get_user(request).id
            ski.save()
            return redirect('view_ski', adv_id=ski.pk)
    else:
        args['form'] = SkiForm()
        args['username'] = request.user.username
        return render(request, 'advertisement/ski/new_ski.html', args )

def view_ski(request, adv_id):
    args = {}
    args['ski'] = get_object_or_404(Ski, id=adv_id)
    args['username'] = request.user.username
    return render(request, 'advertisement/ski/view_ski.html', args)

def edit_ski(request, adv_id):
    args = {}
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    if request.method == 'POST':
        form = SkiForm(request.POST)
        if form.is_valid():
            ski = form.save(commit=False)
            ski.user = User.objects.get(id=request.user.id)
            ski.id = adv_id
            ski.save( update_fields=['title', 'note', 'price', 'year', 'size', 'weight', 'for_weight', 'ski_type'],
                          force_update='True')
            return redirect('view_ski', adv_id=ski.id)
    else:
        ski = Ski.objects.get(id=adv_id)
        args['form'] = SkiForm(instance=ski)
        args['adv_id'] = adv_id
        args['username'] = request.user.username #auth.get_user(request).username
        return render(request, 'advertisement/ski/edit_ski.html', args )
