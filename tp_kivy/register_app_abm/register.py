import sqlite3

def crear_tabla():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Persona(
                   idPersona INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT,
                   password TEXT,
                   email TEXT
                   )''')
    conn.commit()
    cursor.close()
    conn.close()

def registrar_persona(nombre, password, email):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Persona(nombre, password, email) VALUES(?,?,?)",(nombre,password,email))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_persona_email_password(id):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("SELECT email, password FROM Persona WHERE idPersona = ?", (id,))

    persona = cursor.fetchone()
    
    cursor.close()
    conn.close()

    return persona

def actualizar_persona(id, nombre, password, email):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Persona SET nombre=?, password=?, email=? WHERE idPersona=?", (nombre,password,email,id))

    conn.commit()
    cursor.close()
    conn.close()

def borrar_persona(id):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Persona WHERE idPersona=?", (id,))

    conn.commit()
    cursor.close()
    conn.close()

def listado():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * from Persona")

    personas = cursor.fetchall()

    print(personas)

    cursor.close()
    conn.close()

    return personas

def ids():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("SELECT idPersona from Persona")

    ids = cursor.fetchall()

    print(ids)

    cursor.close()
    conn.close()

    return ids

