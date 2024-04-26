psql "host=rc1d-70faxy50p1gfw46z.mdb.yandexcloud.net \
    port=6432 \
    sslmode=verify-full \
    dbname=db_pereval \
    user=dimauser \
    password=admin24admin24 \
    target_session_attrs=read-write" -f pereval_2022-02-22-2021.sql
