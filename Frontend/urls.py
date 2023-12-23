from django.urls import path
from Frontend import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('download/', views.download, name='download'),
    path('contactdata/',views.contactdata,name="contactdata"),
]

