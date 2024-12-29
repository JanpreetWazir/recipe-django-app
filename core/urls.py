from django.contrib import admin
from django.urls import path
from vegi.views import receipe, delete_receipe, update_receipe
from home.views import home, contact, signup, login_path , logout_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', login_path, name='login_path'),  # Updated to `login_path`
    path('logout/', logout_path, name='logout_path'),  # Updated to `login_path`

    path('receipe/', receipe, name='receipe'),
    path('delete_receipe/<int:id>/', delete_receipe, name='delete_receipe'),
    path('update_receipe/<int:id>/', update_receipe, name='update_receipe'),

    path('search/', receipe, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
