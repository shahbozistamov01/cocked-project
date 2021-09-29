from django.db import connection


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]



def info_users():
    with connection.cursor() as cursor:
        cursor.execute("""
            select * from config_bootstrap_user
            order by id DESC
        """)
        data = dictfetchall(cursor)
    return data