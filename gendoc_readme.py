from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import os

# Определяем путь к файлу README.md
README_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
print("Readme generation path: "+README_PATH)

# Функция для генерации README.md
def generate_readme():
    schema_view = get_schema_view(
        openapi.Info(
            title="Документация по функциям RestAPI",
            default_version='v1',
            description="Описание API-функций",
            terms_of_service="https://www.example.com/policies/terms/",
            contact=openapi.Contact(email="contact@example.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    # Генерируем спецификацию OpenAPI
    schema = schema_view.without_ui(cache_timeout=0)

    # Получаем спецификацию в формате Markdown
    swagger_md = schema.to_yaml()

    # Записываем спецификацию в файл README.md
    with open(README_PATH, 'w') as f:
        f.write(swagger_md)

# Вызываем функцию для генерации README.md
generate_readme()