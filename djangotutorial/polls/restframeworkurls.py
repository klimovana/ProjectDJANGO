from django.urls import path  # Для определения URL-маршрутов
from django.urls import include  # Для включения других маршрутов
from rest_framework import routers, serializers, viewsets  # Для работы с API
from .models import User, Measurement  # Импортируем модели из текущего приложения

# Сериализатор для модели User
# Сериализатор преобразует данные модели в формат JSON и обратно
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User  # Указываем модель, которую сериализуем
        fields = ['url', 'first_name', 'last_name', 'email', 'registration_date']  # Поля, которые будут доступны через API

# Сериализатор для модели Measurement
# Аналогично UserSerializer, но для модели Measurement
class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurement  # Указываем модель Measurement
        fields = [
            'url',
            'user',  # Связь с пользователем (ForeignKey)
            'waist_circumference',  # Обхват талии
            'chest_circumference',  # Обхват груди
            'torso_length',  # Длина торса
            'hip_circumference',  # Обхват бедер
            'leg_length',  # Длина ноги
            'sleeve_length'  # Длина рукава
        ]  # Поля, которые будут доступны через API

# ViewSet для модели User
# ViewSet предоставляет CRUD-операции для модели
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Определяем набор данных (все объекты модели User)
    serializer_class = UserSerializer  # Указываем сериализатор для преобразования данных

# ViewSet для модели Measurement
# Аналогично UserViewSet, но для модели Measurement
class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()  # Определяем набор данных (все объекты модели Measurement)
    serializer_class = MeasurementSerializer  # Указываем сериализатор для преобразования данных

# Роутер для автоматической генерации URL
# DefaultRouter автоматически создает URL-маршруты для ViewSet'ов
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)  # Регистрируем маршрут для UserViewSet
router.register(r'measurements', MeasurementViewSet)  # Регистрируем маршрут для MeasurementViewSet

# Подключаем маршруты API
urlpatterns = [
    path('', include(router.urls)),  # Включаем маршруты, сгенерированные роутером
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))  # Добавляем маршруты для аутентификации DRF
]