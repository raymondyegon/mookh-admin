from django.urls import path, include
from languages import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

router1 = routers.DefaultRouter()
router1.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('new_user/', include(router1.urls)),

]
