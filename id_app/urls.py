from django.urls import path
from .import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('generator',views.generator,name='generator'),
    path('institutions',views.institutions,name='institutions'),
    path('addinstitutions',views.addinstitutions,name='addinstitutions'),
    path('postinstitutions',views.postinstitutions,name='postinstitutions'),
    path('editinstitutions<int:id>',views.editinstitutions,name='editinstitutions'),
    path('updateinstitution<int:id>',views.updateinstitution,name='updateinstitution'),
    path('students',views.students,name='students'),
    path('addstudents',views.addstudents,name='addstudents'),
    path('poststudents',views.poststudents,name='poststudents'),
    path('editstudents<int:id>',views.editstudents,name='editstudents'),
    path('updatestudents<int:id>',views.updatestudents,name='updatestudents'),
]
