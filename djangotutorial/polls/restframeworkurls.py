from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from .models import User, Measurement

# Сериализатор для модели User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Сериализуем все поля модели

# Сериализатор для модели Measurement
class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'  # Сериализуем все поля модели

# ViewSet для модели User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSet для модели Measurement
class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# Создаем роутер и регистрируем ViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)  # Регистрируем ViewSet для User
router.register(r'measurements', MeasurementViewSet)  # Регистрируем ViewSet для Measurement

# Подключаем маршруты роутера и добавляем URL для авторизации
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Авторизация
    path('', include(router.urls)),  # Маршруты API
]