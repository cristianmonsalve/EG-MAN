from flask import jsonify, request
from db.db import cnx

class Central:
    global cur  
    cur = cnx.cursor()
    
    def list():
        lista = []
        cur.execute("SELECT * FROM central_telefonica")
        rows = cur.fetchall()
        colums = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(colums,row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close


    def insert(body):
        data = (body['origen'],body['destinatario'],body['estado_conexion'],body['estado_actual'],body['fecha'])
        sql = "INSERT INTO central_telefonica(origen, destinatario, estado_conexion,estado_actual,fecha) VALUES (%s,%s,%s,%s,%s)"
        cur.execute(sql,data)
        cnx.commit()
        return{'estado': "OK"}, 200

    def delete(body):
        id_central = (body['id_central'])
        sql = "DELETE FROM central_telefonica WHERE id_central=" + id_central
        cur.execute(sql,id_central)
        cnx.commit()
        return {"status": "OK"}, 200



