# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.models import User
from .models import Race, Milestone, Protocol, UserRaceLink
from .forms import ProtocolForm, UserRaceLinkForm

from django.db.models import Q
from django.views.decorators.http import condition

def milestones(request, race_code):
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    args = {}
    args['username'] = request.user.username

    race = Race.objects.filter(title = race_code)

    milestones = Milestone.objects.filter(race = race)#.select_related('protocol')

    protocols = [[0 for x in range(2)] for y in range(1000)]
    for milestone in milestones:
        protocols[milestone.id][0] = milestone
        protocols[milestone.id][1] = Protocol.objects.filter(race=race, user=request.user, milestone_id=milestone.id)

    args['protocols'] = protocols
    return render(request, 'race/milestones.html', args )

def milestone_check(request, race_code, milestone_id):
    # добавить проверку на пользователя
    if not request.user.is_authenticated():
        return render(request, 'user/login_error.html')
    args = {}

    milestone = Milestone.objects.filter(id = milestone_id)

    formMark = ProtocolForm().save(commit=False)
    formMark.user = request.user
    formMark.race_id = milestone[0].race.id
    formMark.milestone = milestone[0]

    formMark.save()

    return redirect('milestones', race_code=race_code)

def milestone_remove(request, race_code, protocol_id):
    protocol = Protocol.objects.get(id=protocol_id)
    # проверяем права на удаление
    if User.objects.get(id=request.user.id) == protocol.user:
        protocol.delete()
    return redirect('milestones', race_code=race_code)

def protocol_user(request, race_code, user_name):
    args = {}
    args['username'] = user_name

    user = User.objects.get(username = user_name)
    race = Race.objects.filter(title = race_code)

    milestones = Milestone.objects.filter(race = race)

    protocols = [[0 for x in range(2)] for y in range(1000)]
    for milestone in milestones:
        protocols[milestone.id][0] = milestone
        protocols[milestone.id][1] = Protocol.objects.filter(race=race, user=user, milestone_id=milestone.id)

    args['protocols'] = protocols
    return render(request, 'race/protocol_user.html', args )

def protocol_all(request, race_code):
    args = {}
    race = Race.objects.filter(title = race_code)

    users = User.objects.all()
    # milestones = Milestone.objects.filter(race = race)

    protocols = [[0 for x in range(3)] for y in range(1000)]
    for user in users:
        protocols[user.id][0] = user.username
        protocols[user.id][1] = Protocol.objects.filter(race=race, user=user).last()
        if request.user.is_authenticated():
            protocols[user.id][2] = UserRaceLink.objects.filter(user = user, race = race).first()

    args['protocols'] = protocols
    args['race_code'] = race_code
    args['races'] = Race.objects.all()

    return render(request, 'race/protocol_all.html', args )

def race_select(request):
    args = {}
    # args['races'] = Race.objects.all()

    races = [[0 for x in range(2)] for y in range(1000)]
    for race in Race.objects.all():
        races[race.id][0] = race
        if request.user.is_authenticated():
            races[race.id][1] = UserRaceLink.objects.filter(race=race, user=request.user)
    args['races'] = races
    return render(request, 'race/race_select.html', args )

def race_home(request, race_code):
    args = {}
    args['race'] = Race.objects.get(title = race_code)
    if request.user.is_authenticated():
        args['registration'] = UserRaceLink.objects.filter(race=args['race'], user=request.user)
    return render(request, 'race/race_home.html', args )

def registration(request, race_code):
    if request.user.is_authenticated():
        race = Race.objects.get(title = race_code)

        link = UserRaceLinkForm().save(commit=False)
        link.user = request.user
        link.race_id = race.id

        link.save()

    return redirect('race_select')

def registration_remove(request, race_code):
    if request.user.is_authenticated():
        race = Race.objects.get(title = race_code)
        link = UserRaceLink.objects.filter(user = request.user, race = race)
        link.delete()

    return redirect('race_select')
