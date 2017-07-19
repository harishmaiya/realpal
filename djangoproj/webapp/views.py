# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView 

class HomePageView(TemplateView):
    template_name = "index.html"

class PreparePageView(TemplateView):
    template_name = "prepare.html"

class BuyPageView(TemplateView):
    template_name = "buy.html"

class LivePageView(TemplateView):
    template_name = "live.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
