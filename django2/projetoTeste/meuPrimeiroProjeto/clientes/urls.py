from django.urls import path
from .views import persons_list, persons_new, person_update, person_delete

urlpatterns = [
    path('new/', persons_new, name='person_new'),
    path('list/', persons_list, name='person_list'),
    path('update/<int:id>/', person_update, name='person_update'),
    path('delete/<int:id>/', person_delete, name='person_delete'),
]
