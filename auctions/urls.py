from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("create", views.create, name="create"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("toggle/<int:id>", views.toggle_watchlist_item, name="toggle"),
    path("update/<int:pk>", views.update, name="update"),
    path("listing/<int:pk>", views.listing, name="listing"),
]
