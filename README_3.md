# Документация по функциям RestAPI

## Описание API-функций

* Версия: v1
* Условия использования: [https://www.example.com/policies/terms/](https://www.example.com/policies/terms/)
* Контакт: contact@example.com
* Лицензия: BSD License

### Базовая информация

* Хост: 127.0.0.1:8000
* Протоколы: http
* Базовый путь: /

### Форматы данных

* Входные данные: application/json
* Выходные данные: application/json

### Безопасность

* Описание: Basic

## Маршруты

### /submitData/

#### GET /submitData/

* Описание: Класс для просмотра и добавления новых записей
Вызывается по ссылке http://.../submitData/
* Параметры:
* Ответ:
  - 200: 

#### POST /submitData/

* Описание: Класс для просмотра и добавления новых записей
Вызывается по ссылке http://.../submitData/
* Параметры:
* Ответ:
  - 201: 

#### PARAMETERS /submitData/

### /submitData/{id}

#### GET /submitData/{id}

* Описание: Класс для просмотра и редактирования конкретной записи. Обрабатывает команды GET и PUT
Вызывается по ссылке http://.../submitData/<int:pk>/
* Параметры:
* Ответ:
  - 200: 

#### PUT /submitData/{id}

* Описание: Класс для просмотра и редактирования конкретной записи. Обрабатывает команды GET и PUT
Вызывается по ссылке http://.../submitData/<int:pk>/
* Параметры:
* Ответ:
  - 200: 

#### PARAMETERS /submitData/{id}

### /submitData/{id}/status

#### GET /submitData/{id}/status

* Описание: Наследник класса PerevalRecordView. Обрабатывает GET-запрос статуса записи
Вызывается по ссылке http://.../submitData/<int:pk>/status
* Параметры:
* Ответ:
  - 200: 

#### PUT /submitData/{id}/status

* Описание: Наследник класса PerevalRecordView. Обрабатывает GET-запрос статуса записи
Вызывается по ссылке http://.../submitData/<int:pk>/status
* Параметры:
* Ответ:
  - 200: 

#### PARAMETERS /submitData/{id}/status

