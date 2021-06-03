from django.urls import path
from . import views


urlpatterns = [
    path('shows', views.allShows),
    path('shows/addshow', views.AddShow),
    path('shows/new', views.index),
    path('shows/info/<int:showId>', views.ShowPage),
    path('shows/edit/<int:showId>', views.EditPage),
    path('shows/editshow/<int:showId>', views.EditShow),
    path('shows/delete/<int:showId>', views.DeleteShow),
]