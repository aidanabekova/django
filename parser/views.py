import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, FormView
from parser import models, forms, parser



class AnimeView(ListView):
    model = models.Film
    template_name = 'anime/anime_list.html'

    def get_queryset(self):
        return models.Film.objects.all()

class ParserAnimeView(FormView):
    template_name = 'anime/anime_parser.html'
    form_class = forms.ParserForm
    success_url = '/anime/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserAnimeView, self).post(request, *args, **kwargs)


class ZetflixView(ListView):
    model = models.Zetflix
    template_name = 'zet/zetflix_list.html'

    def get_queryset(self):
        return models.Zetflix.objects.all()

class ParserShowView(FormView):
    template_name = 'zet/zetflix_parser.html'
    form_class = forms.ParserForm
    success_url = '/zetflix/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserShowView, self).post(request, *args, **kwargs)