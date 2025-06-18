from  django.urls import  path



from .views import (
    RegisterApiView,
    CookieTokenLoginView,
    PublicAPIView,
    ProtectedAPIView,
    register_page,
    TelegramUserCreateView,

)

urlpatterns = [

    path('register/', register_page, name='register'),
    path('api/register/',RegisterApiView.as_view(),name='register-api'),

    path('login/', CookieTokenLoginView.as_view(), name='token_obtain_pair'),

    path('public/',PublicAPIView.as_view(),name='public'),
    path('protected/',ProtectedAPIView.as_view(),name='protected'),

    path('telegram_user/',TelegramUserCreateView.as_view())

]





