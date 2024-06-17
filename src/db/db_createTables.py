import sqlite3


def dbCreateTables():
    conexion = sqlite3.connect("database.db")
    conexion.execute(
        """CREATE TABLE IF NOT EXISTS paciente (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT, 
            apellido TEXT,
            cedula INT,
            telefono INT,
            direccion TEXT,
            diagnostico TEXT
            )
        """
    )
    
    conexion.execute(
        """CREATE TABLE IF NOT EXISTS clinicalstaff (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT, 
            apellido TEXT,
            cedula INT,
            telefono INT,
            direccion TEXT,
            cargo TEXT
            )
        """
    )
    

    conexion.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """
    )
