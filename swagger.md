swagger: '2.0'
info:
  title: Документация по функциям RestAPI
  description: Описание API-функций
  termsOfService: https://www.example.com/policies/terms/
  contact:
    email: contact@example.com
  license:
    name: BSD License
  version: v1
host: 127.0.0.1:8000
schemes:
- http
basePath: /
consumes:
- application/json
produces:
- application/json
securityDefinitions:
  Basic:
    type: basic
security:
- Basic: []
paths:
  /submitData/:
    get:
      operationId: submitData_list
      description: |-
        Класс для просмотра и добавления новых записей
        Вызывается по ссылке http://.../submitData/
      parameters: []
      responses:
        '200':
          description: ''
      tags:
      - submitData
    post:
      operationId: submitData_create
      description: |-
        Класс для просмотра и добавления новых записей
        Вызывается по ссылке http://.../submitData/
      parameters: []
      responses:
        '201':
          description: ''
      tags:
      - submitData
    parameters: []
  /submitData/{id}:
    get:
      operationId: submitData_read
      description: |-
        Класс для просмотра и редактирования конкретной записи. Обрабатывает команды GET и PUT
        Вызывается по ссылке http://.../submitData/<int:pk>/
      parameters: []
      responses:
        '200':
          description: ''
      tags:
      - submitData
    put:
      operationId: submitData_update
      description: |-
        Класс для просмотра и редактирования конкретной записи. Обрабатывает команды GET и PUT
        Вызывается по ссылке http://.../submitData/<int:pk>/
      parameters: []
      responses:
        '200':
          description: ''
      tags:
      - submitData
    parameters:
    - name: id
      in: path
      required: true
      type: string
  /submitData/{id}/status:
    get:
      operationId: submitData_status_list
      description: |-
        Наследник класса PerevalRecordView. Обрабатывает GET-запрос статуса записи
        Вызывается по ссылке http://.../submitData/<int:pk>/status
      parameters: []
      responses:
        '200':
          description: ''
      tags:
      - submitData
    put:
      operationId: submitData_status_update
      description: |-
        Наследник класса PerevalRecordView. Обрабатывает GET-запрос статуса записи
        Вызывается по ссылке http://.../submitData/<int:pk>/status
      parameters: []
      responses:
        '200':
          description: ''
      tags:
      - submitData
    parameters:
    - name: id
      in: path
      required: true
      type: string
definitions: {}
