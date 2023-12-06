
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('about/', about,name='about'),
    # path('contact/', contact,name='contact'),
    path('contact/', contact,name='contact'),
    path('service/', service,name='service'),
    path('project/', project,name='project'),
    path('team/', team,name='team'),
    path('testimonial/', testimonial,name='testimonial'),
    path('error_template/', error_template,name='error_template'),
    path('blog/', blog,name='blog'),
]
