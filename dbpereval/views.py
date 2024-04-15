from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers
from rest_framework.views import APIView

from .serializers import *
from .models import *

# for yaml-swagger-schema implementation:
from django.http import HttpResponse
import yaml
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import DocumentationRenderer

# from drf_yasg.generators import OpenAPISchemaGenerator
#
# schema_generator = OpenAPISchemaGenerator(
#     title="Документация по функциям RestAPI",
#     description="Описание API-функций",
#     version="v1",
#     url="/api/v1/",
#     patterns=None,
# )

def yaml_to_markdown(yaml_str):
    data = yaml.safe_load(yaml_str)
    markdown = f"# {data['info']['title']}\n\n"
    markdown += f"## {data['info']['description']}\n\n"
    markdown += f"* Версия: {data['info']['version']}\n"
    markdown += f"* Условия использования: [{data['info']['termsOfService']}]({data['info']['termsOfService']})\n"
    markdown += f"* Контакт: {data['info']['contact']['email']}\n"
    markdown += f"* Лицензия: {data['info']['license']['name']}\n\n"
    markdown += "### Базовая информация\n\n"
    markdown += f"* Хост: {data['host']}\n"
    markdown += f"* Протоколы: {', '.join(data['schemes'])}\n"
    markdown += f"* Базовый путь: {data['basePath']}\n\n"
    markdown += "### Форматы данных\n\n"
    markdown += f"* Входные данные: {', '.join(data['consumes'])}\n"
    markdown += f"* Выходные данные: {', '.join(data['produces'])}\n\n"
    markdown += "### Безопасность\n\n"
    markdown += f"* Описание: {', '.join(data['securityDefinitions'])}\n\n"
    markdown += "## Маршруты\n\n"
    for path, path_data in data['paths'].items():
        markdown += f"### {path}\n\n"
        for method, method_data in path_data.items():
            markdown += f"#### {method.upper()} {path}\n\n"
            if isinstance(method_data, list):
                continue  # Пропускаем список, так как не можем получить описание
            markdown += f"* Описание: {method_data.get('description', '')}\n"
            if 'parameters' in method_data:
                markdown += "* Параметры:\n"
                for param in method_data['parameters']:
                    markdown += f"  - {param['name']}: {'обязательный' if param.get('required', False) else 'необязательный'}, {param['type']}, в {param['in']}\n"
            if 'responses' in method_data:
                markdown += "* Ответ:\n"
                for resp_code, resp_data in method_data['responses'].items():
                    markdown += f"  - {resp_code}: {resp_data['description']}\n"
            markdown += "\n"
    return markdown

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

def generate_markdown(request):
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
        renderer_classes=[DocumentationRenderer],
    )

    generator = schema_view.with_ui('swagger')
    schema = generator.get_schema(request=request)
    yaml_data = schema.yaml()
    markdown_data = yaml_to_markdown(yaml_data)
    # markdown_data = schema.to_markdown()

    # Сохраняем Markdown-файл на диск
    with open('swagger.md', 'w') as f:
        f.write(markdown_data)

    return HttpResponse(markdown_data, content_type='text/markdown')

@api_view(['GET'])
def generate_yaml(request):
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

    generator = schema_view.with_ui('swagger')
    schema = generator.get_schema(request=request)
    yaml_data = schema.yaml()
    # schema = schema_view.get_schema(request=request)
    # yaml_data = yaml.dump(schema, default_flow_style=False)
    # yaml_data = schema_view.get_schema_yaml()
    # yaml_data = get_schema_view().get_schema_yaml(request=request)

    # Сохраняем YAML-файл на диск
    with open('swagger.yaml', 'w') as f:
        f.write(yaml_data)

    return HttpResponse(yaml_data, content_type='text/yaml')


class ContactForm(serializers.Serializer):
    # simple serializer for emails
    email = serializers.EmailField()
    message = serializers.CharField()

# simple endpoint to take the serializer data
class SendEmail(APIView):
      # permission class set to be unauthenticated
    permission_classes = (permissions.AllowAny,)
    # this is where the drf-yasg gets invoked
    @swagger_auto_schema(request_body=ContactForm)
    def post(self, request):
          # serializer object
        serializer = ContactForm(data=request.data)
        # checking for errors
        if serializer.is_valid():
            json = serializer.data
            return Response(
                data={"status": "OK", "message": json},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PerevalRecordView(APIView):
    """
    Класс для просмотра и редактирования конкретной записи. Обрабатывает команды GET и PUT
    Вызывается по ссылке http://.../submitData/<int:pk>/
    """
    def get(self, request, pk):
        if dbPereval.objects.filter(id=pk).exists():
            pereval = dbPereval.objects.get(id=pk)
            return Response(self.prepare_result(pereval))
        else:
            result = {"status": "503", "message": "Record not found"}
            return Response(result, status=503)

    def put(self, request, pk):
        if dbPereval.objects.filter(id=pk).exists():
            pereval = dbPereval.objects.get(id=pk)
            serializer = PerevalSerializer(pereval, data=request.data)
            if serializer.is_valid():
                pereval = serializer.save()
                result = {"status": "200", "message": f'pereval updated. Id {pereval.pk}'}
                return Response(result, status=200)
            else:
                result = {"status": "400", "message": f'{serializer.errors}'}
                return Response(result, status=400)
        else:
            result = {"status": "503", "message": "Record not found"}
            return Response(result, status=503)

    # Метод для подготовки ответа на GET-запрос
    def prepare_result(self, pereval):
        serializer = PerevalSerializer(pereval, many=False)
        return serializer.data


class PerevalStatusView(PerevalRecordView):
    """
    Наследник класса PerevalRecordView. Обрабатывает GET-запрос статуса записи
    Вызывается по ссылке http://.../submitData/<int:pk>/status
    """
    def prepare_result(self, pereval):
        result = {"status": f'{pereval.status}'}
        return result


class PerevalView(APIView):
    """
    Класс для просмотра и добавления новых записей
    Вызывается по ссылке http://.../submitData/
    """
    def get(self, request):
        # username = 'vpupkin' # for test
        username = request.user.username
        queryset = dbPereval.objects.filter(raw_data__user__contains={'id': username})
        serializer = PerevalSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            pereval = serializer.save()
            result = {"status": "200", "message": f'pereval added. New Id {pereval.pk}'}
            return Response(result, status=200)
        else:
            result = {"status": "400", "message": f'{serializer.errors}'}
            return Response(result, status=400)
