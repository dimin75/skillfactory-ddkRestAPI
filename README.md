# ������������ �� �������� RestAPI

## �������� API-�������.
 ��������� �������� ���������� ������������ � yaml-�������:
<a href='/swagger.yaml'> ������� swagger.yaml</a> 
<a href='/generate_yaml/'> ������������� � ������� � �������  YAML</a> 


* ������: v1
* �������: dimatest24@yandex.ru
* ��������: BSD License

### ������� ����������

* ����: 127.0.0.1:8000
* ���������: http
* ������� ����: /

### ������� ������

* ������� ������: application/json
* �������� ������: application/json

### ������������

* ��������: Basic

## ��������

### /submitData/

#### GET /submitData/

* ��������: ����� ��� ��������� � ���������� ����� �������
���������� �� ������ http://.../submitData/
* ���������:
* �����:
  - 200: 

#### POST /submitData/

* ��������: ����� ��� ��������� � ���������� ����� �������
���������� �� ������ http://.../submitData/
* ���������:
* �����:
  - 201: 

#### PARAMETERS /submitData/

### /submitData/{id}

#### GET /submitData/{id}

* ��������: ����� ��� ��������� � �������������� ���������� ������. ������������ ������� GET � PUT
���������� �� ������ http://.../submitData/<int:pk>/
* ���������:
* �����:
  - 200: 

#### PUT /submitData/{id}

* ��������: ����� ��� ��������� � �������������� ���������� ������. ������������ ������� GET � PUT
���������� �� ������ http://.../submitData/<int:pk>/
* ���������:
* �����:
  - 200: 

#### PARAMETERS /submitData/{id}

### /submitData/{id}/status

#### GET /submitData/{id}/status

* ��������: ��������� ������ PerevalRecordView. ������������ GET-������ ������� ������
���������� �� ������ http://.../submitData/<int:pk>/status
* ���������:
* �����:
  - 200: 

#### PUT /submitData/{id}/status

* ��������: ��������� ������ PerevalRecordView. ������������ GET-������ ������� ������
���������� �� ������ http://.../submitData/<int:pk>/status
* ���������:
* �����:
  - 200: 

#### PARAMETERS /submitData/{id}/status

