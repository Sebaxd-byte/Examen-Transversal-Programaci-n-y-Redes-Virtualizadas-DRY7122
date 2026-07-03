"""
Asignatura: Programación y Redes Virtualizadas (DRY7122)
Script: app_segura.py
Objetivo: Crear un sitio web (puerto 7500) con persistencia en SQLite y contraseñas hash.
Integrantes: Sebastián Arcos y Jorge Manzo
"""

import sqlite3
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_NAME = "examen_integrantes.db"

def inicializar_base_datos():
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    ''')
    
   
    integrantes = [
        "Sebastián Arcos",
        "Jorge Manzo"
    ]
    
  
    credenciales_iniciales = {
        "Sebastián Arcos": "PassSec_Sebaxd2026",
        "Jorge Manzo": "NetSecure_Jorge2026"
    }
    
 
    for usuario in integrantes:
        clave_plana = credenciales_iniciales[usuario]
 
        hash_resultado = hashlib.sha256(clave_plana.encode('utf-8')).hexdigest()
        
        try:
            cursor.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)", (usuario, hash_resultado))
        except sqlite3.IntegrityError:
          
            pass
            
    conn.commit()
    conn.close()

@app.route('/auth/login', methods=['POST'])
def validar_usuario():
    
    datos = request.json
    usuario_ingresado = datos.get("username")
    clave_ingresada = datos.get("password")
    
    if not usuario_ingresado or not clave_ingresada:
        return jsonify({"status": "ERROR", "message": "Faltan parámetros obligatorios"}), 400
        
    
    hash_a_verificar = hashlib.sha256(clave_ingresada.encode('utf-8')).hexdigest()
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND password_hash=?", (usuario_ingresado, hash_a_verificar))
    registro = cursor.fetchone()
    conn.close()
    
    
    if registro:
        return jsonify({
            "status": "SUCCESS", 
            "message": f"Autenticación Exitosa. Bienvenido/a al sistema del ET, {usuario_ingresado}."
        }), 200
    else:
        return jsonify({
            "status": "DENIED", 
            "message": "Fallo de Autenticación. Credenciales inválidas o hash no coincide."
        }), 401

if __name__ == "__main__":
    
    inicializar_base_datos()
    print("\n[INFO] Servidor web de infraestructura iniciado correctamente.")
    print("[INFO] Escuchando peticiones HTTP en el puerto TCP 7500...\n")
    app.run(host="0.0.0.0", port=7500)
