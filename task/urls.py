from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),

    path("", RedirectView.as_view(url="/todo/")),

    path('todo/', include('todo.urls')),
    path('weather/', include('weather.urls')),
    path('expense/', include('expense.urls')),
    path('chatbot/', include('chatbot.urls')),

]

