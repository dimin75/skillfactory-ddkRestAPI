Итоговое задание (HW-03)
========================================================================================================================

ТЗ:

Задача 1. Создание базы данных
На основании базы данных формата PostgreSQL
(пример: https://drive.google.com/file/d/1TuFcH5k-lU21b6xQtCeQ_UTW8OJwR9f3/view?usp=sharing)
использовать существующую или доработать БД для фиксации горных перевалов.

Задача 2. Создание класса по работе с данными

Необходимо создать класс (модель) для работы с БД ФСТР.
Реализовать методы, с помощью которых будет пополнятся информация в таблицах БД.
Для этого необходимо создать REST API, который вызывается методом POST при обращении
к странице серевера submitData.
При добавлении новой записи в БД поле "status" установливается в значение "new".


Задача 3. Создание REST API c одним методом — POST submitData

Реализация модели в Django на основании задач 1 и 2.

========================================================================================================================

Реализация ТЗ:

1. Для реализации проекта была использована база PostgreSQL, установленная в unix-виде следующими командами:

-- установка:
	sudo apt update
	sudo apt install postgresql postgresql-contrib
-- запуск:
	sudo service postgresql start
-- выполнение авторизации, присвоение пароля:
	psql -U postgres -W
	password: admin24
-- создание базы:
	CREATE DATABASE db_pereval;
-- импорт данных из существующей базы ФСТР:
	psql -U postgres -d db_pereval_fstr -f pereval_2022-02-22-2021.sql

2. Создан проект ddkDbRestAPI, включающий в себя приложение dbpereval, реализующе функции ввода данных в БД
ФСТР по горным перевалам в соответствии с требованиями ТЗ. Реализация выполнена на основе библиотеки rest_framework.
(подробнее - https://www.django-rest-framework.org/)
Для использования необходимо доустановить необходимые компоненты методом:

	pip install -r requirements.txt

3. Проверка работоспособности выполняется при включенной базе данных. Необходимо выполнить в командной строке unix:
     
        sudo service postgresql start

   - при правильном запуске получим ответ:

         * Starting PostgreSQL 12 database server                                                             [ OK ]

   - проверка работы базы данных, ее наличия:

	psql -U postgres -d db_pereval

        в случае правильной работы системы получаем приглашение для работы с БД в виде:

        b_pereval=# 
        
        проверка наличия и работоспособности таблиц:

         db_pereval=# \dt
                   List of relations
 Schema |            Name            | Type  |  Owner
--------+----------------------------+-------+----------
 public | auth_group                 | table | postgres
 public | auth_group_permissions     | table | postgres
 public | auth_permission            | table | postgres
 public | auth_user                  | table | postgres
 public | auth_user_groups           | table | postgres
 public | auth_user_user_permissions | table | postgres
 public | django_admin_log           | table | postgres
 public | django_content_type        | table | postgres
 public | django_migrations          | table | postgres
 public | django_session             | table | postgres
 public | pereval_added              | table | postgres
 public | pereval_areas              | table | postgres
 public | pereval_images             | table | postgres
 public | spr_activities_types       | table | postgres

4. Запуск приложения REST API:

	python .\manage.py runserver


5. Проверка работоспособности класса. В командной строке браузера задать команду:

       -- вывод класса для ввода сырых данных JSON:

	http://127.0.0.1:8000/submitData

       -- обращение к 1-ой записи в БД (должна быть импортирована на шаге 1 данного readme):

	http://127.0.0.1:8000/submitData/1

       -- вывод статуса записи в БД:

	http://127.0.0.1:8000/submitData/1/status

Таким образом, класс реализован, приложение работоспособно. При использовании базы ФСТР в среде
PostgreSQL с другими пользователями и паролями необходимо исправить файл settings.py в каталоге
ddkDbRestAPI, который по умолчанию в данной реализации имеет вид:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'db_pereval'),
        'USER': os.getenv('FSTR_DB_LOGIN', 'postgres'),
        'PASSWORD': os.getenv('FSTR_DB_PASS', 'admin24'),
        'HOST': os.getenv('FSTR_DB_HOST', 'localhost'),
        'PORT': int(os.getenv('FSTR_DB_PORT', '5432')),
    }
}
