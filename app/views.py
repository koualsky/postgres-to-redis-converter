import os
import psycopg2
import json
import redis

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse
from celery import Celery
from time import sleep


@api_view(['GET'])
def convert(request):
    if request.method == 'GET':

        database = request.GET.get('database')
        table = request.GET.get('table')
        user = request.GET.get('user')
        password = request.GET.get('password')
        host = request.GET.get('host')
        port = request.GET.get('port')

        connection_conf = f"dbname={database} user={user} password={password} host={host} port={port}"
        try:
            conn = psycopg2.connect(connection_conf)
            conn.close()
        except:
            return Response(status=status.HTTP_502_BAD_GATEWAY)

        connection = psycopg2.connect(connection_conf)
        cursor = connection.cursor()
        postgres_select_query = f"select * from {table}"
        cursor.execute(postgres_select_query)
        records = cursor.fetchall()

        pk_query = f"""
            SELECT c.column_name
            FROM information_schema.table_constraints tc 
            JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name) 
            JOIN information_schema.columns AS c ON c.table_schema = tc.constraint_schema
            AND tc.table_name = c.table_name AND ccu.column_name = c.column_name
            WHERE constraint_type = 'PRIMARY KEY' and tc.table_name = '{table}';
        """
        cursor_pk = connection.cursor()
        cursor_pk.execute(pk_query)
        try:
            table_pk = cursor_pk.fetchall()[0][0]
        except IndexError:
            print('The given table does not have a PRIMARY KEY field')
            return Response(status=status.HTTP_404_NOT_FOUND)

        pre_json = {table: []}
        for row in records:
            output = {}
            for e in row:
                output[cursor.description[row.index(e)].name] = e
            pre_json[table].append(output)
            r = redis.Redis(host='redis', port=6379)
            json_clear = json.dumps(output)
            r.set(output[table_pk], json_clear)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_502_BAD_GATEWAY)


#app = Celery('views', broker='pyamqp://guest@localhost//')
#app = Celery('views', broker='amqp://guest@localhost//')
#app = Celery('views', backend='rpc://', broker='amqp://guest:guest@rabbitmq:5672')


#@app.task
def seler(request):
    #print('\nstart')
    #sleep(3)
    #print('end\n')

    from .tasks import seler as seler2
    #res = seler2.delay()
    #print(res.status)
    #print(res.get())
    seler2.delay()
    return HttpResponse('elo')
