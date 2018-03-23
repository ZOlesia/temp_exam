# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'exam/index.html')
def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(index)
    else:
        new_user = User.objects.create(
            name = request.POST['name'], 
            alias = request.POST['alias'], 
            email = request.POST['email'], 
            password = request.POST['password'], 
            conf_password = request.POST['confirm']
        )
        request.session['user_id'] = new_user.id
        return redirect(success)
        
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(index)
    else:
        request.session['user_id'] = User.objects.get(email = request.POST['email']).id
        return redirect(success)

def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    context =  {
        'user': User.objects.get(id = request.session['user_id']),
        'all_quotes': Quote.objects.all(),
        'favorite': Quote.objects.filter(liked_users=User.objects.get(id=request.session['user_id']))
    }
    return render(request, 'exam/success.html', context)

def add(request, id):
    # # q = Quote.objects.get(id=id)
    # Quote.objects.remove(id=id)
    return redirect(success)

def remove(request):
    return redirect(success)


def contribute(request):
    errors = Quote.objects.quote_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(success)
    else:
        new_quote = Quote.objects.create(
            name = request.POST['by'],
            content = request.POST['msg'],
            uploader = User.objects.get(id = request.session['user_id'])
        )
        return redirect(success)

def show(request, id):
    context = {
        'user': User.objects.get(id=id),
        'posts': Quote.objects.filter(uploader=id),
    }
    request.session['count'] = len(Quote.objects.filter(uploader=id))
    return render(request, 'exam/show.html', context)
