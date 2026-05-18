from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from accounts.views import (
    register,
    user_login,
    user_logout
)

from services.views import (
    home,
    add_service,
    book_service,
    add_review,
    dashboard,
    my_bookings
)

urlpatterns = [

    path('', home),

    path('services/', home),

    path('register/', register),

    path('login/', user_login),

    path('provider-login/', user_login),

    path('logout/', user_logout),

    path('add-service/', add_service),

    path('book/<int:id>/', book_service),

    path('review/<int:id>/', add_review),

    path('dashboard/', dashboard),
    path('my-bookings/', my_bookings),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)