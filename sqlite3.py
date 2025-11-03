import apsw as sql
con = sql.Connection("mi_db.sqlite")
print("¡Conexión exitosa de base de datos!")

con.execute('''
            CREATE TABLE IF NOT EXISTS PERSONA(
            ID INT PRIMARY KEY NOT NULL, 
            NOMBRE TEXT NOT NULL,
            EDAD INT NOT NULL,
            DIRECCION CHAR(50));''')

print("¡Tabla creada exitosamente!")

# con.execute("INSERT INTO PERSONA(ID,NOMBRE,EDAD,DIRECCION) VALUES (1,'Pablo',32,'Av. Chaco 123')")
# con.execute("INSERT INTO PERSONA (ID,NOMBRE,EDAD,DIRECCION) VALUES (2, 'Ana', 25, 'Av. Nueva 123')")

con.execute('''
            CREATE TABLE IF NOT EXISTS PRODUCTO(
            ID INT PRIMARY KEY NOT NULL, 
            NOMBRE TEXT NOT NULL,
            STOCK INT NOT NULL,
            PRECIO_UNITARIO INT,
            DESCRIPCION TEXT
            );''')

con.execute('''
            CREATE TABLE IF NOT EXISTS COMPRA(
            ID INT PRIMARY KEY NOT NULL, 
            ID_PERSONA INT,
            ID_PRODUCTO INT,
            FOREIGN KEY(ID_PERSONA) REFERENCES PERSONA(ID),
            FOREIGN KEY(ID_PRODUCTO) REFERENCES PRODUCTO(ID)
            );''')

con.close()