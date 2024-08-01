
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from api import customauthtoken
from  rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router=DefaultRouter()
router.register('stu',views.StudentView,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refreshtoken/', TokenRefreshView.as_view()),
    path('verifytoken/', TokenVerifyView.as_view()),


    # path('/', include('rest_framework.urls')),
    path('get/',customauthtoken.CustomAuthToken.as_view()),

]
