from django.urls import path
from . import views 
app_name = 'service_page'

urlpatterns = [
    path('',views.render_services,name='service_page'),
    #path("<int:post_id>", views.post_detail, name="post_detail"),
]

