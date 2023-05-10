from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('detaile/<int:post_id>/', views.post_details, name='detaile'),
    path('programming', views.dev, name='programming'),
    path('Ethical_Hacking', views.EH, name='EH'),
    path('Markrting', views.Mark, name='Marketing'),
    path('Another', views.Another, name='Another'),
    path('new_post', views.PostCreatView.as_view(), name='new_post'),
    path('detaile/<slug:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('detaile/<slug:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),    
]
