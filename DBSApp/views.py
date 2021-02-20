from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

def uptime(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT date_trunc('second', current_timestamp - pg_postmaster_start_time()) as uptime;")
        row = cursor.fetchone()

    return HttpResponse(row)
