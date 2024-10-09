from django.urls import path
from .import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('generator',views.generator,name='generator'),
    path('institutions',views.institutions,name='institutions'),
    path('addinstitutions',views.addinstitutions,name='addinstitutions'),
    path('postinstitutions',views.postinstitutions,name='postinstitutions'),
]
