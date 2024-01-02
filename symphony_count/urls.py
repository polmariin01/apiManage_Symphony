from django.urls import path

from . import views
from .views import Symphony_ListView, count_interaction, get_interactions

urlpatterns = [
    #path("", views.index, name="index"),
    path('composer/<int:pk>/count/', count_interaction, name='count_interaction'),
    path('composer/<int:pk>/get/', get_interactions, name='get_interactions')
]