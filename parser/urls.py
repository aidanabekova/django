from django.urls import path
from parser import views


app_name = 'film'
urlpatterns = [
    path('anime/', views.AnimeView.as_view(), name='attakoftitan'),
    path('parser/', views.ParserAnimeView.as_view(), name='parser'),
    path('zetflix/', views.ZetflixView.as_view(), name='zetflix'),
    path('parser2/', views.ParserShowView.as_view(), name='zetflix parse'),

]
