from django.urls import path
from basicapp import views

# Template Tagging
app_name = 'basicapp'

urlpatterns = [
    path('relative/', views.relative_url_templates_page, name='relative'),
    path('other/', views.other_page, name='other'),
]
