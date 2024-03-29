from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


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
