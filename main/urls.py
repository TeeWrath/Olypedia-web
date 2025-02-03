from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('services/', views.services,name='services'),
    path('project/', views.project,name='project'),
    path('career/', views.career,name='career'),
    path('market/', views.market,name='market'),
    path('education/', views.education,name='education'),
    path('health/', views.health,name='health'),
    path('entertainment/', views.entertainment,name='entertainment'),
    path('travel/', views.travel,name='travel'),
    path('legal/', views.legal,name='legal'),
    path('corporate/', views.corporate,name='corporate'),
    path('finance/', views.finance,name='finance'),
]
