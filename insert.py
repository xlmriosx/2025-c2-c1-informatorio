import apsw as sql
con = sql.Connection("mi_db.sqlite")

# Insertar PROVEEDORES
con.execute("INSERT INTO PROVEEDOR (ID, NOMBRE) VALUES (1, 'TechSupply SA')")
con.execute("INSERT INTO PROVEEDOR (ID, NOMBRE) VALUES (2, 'ElectroPartes Ltda')")
con.execute("INSERT INTO PROVEEDOR (ID, NOMBRE) VALUES (3, 'ComponentesPro')")

# Insertar COMPONENTES
con.execute("INSERT INTO COMPONENTE (ID, NOMBRE, DESCRIPCION, CANTIDAD) VALUES (1, 'Procesador', 'Intel Core i7', 50)")
con.execute("INSERT INTO COMPONENTE (ID, NOMBRE, DESCRIPCION, CANTIDAD) VALUES (2, 'Memoria RAM', 'DDR4 16GB', 100)")
con.execute("INSERT INTO COMPONENTE (ID, NOMBRE, DESCRIPCION, CANTIDAD) VALUES (3, 'Disco SSD', 'Samsung 1TB', 75)")
con.execute("INSERT INTO COMPONENTE (ID, NOMBRE, DESCRIPCION, CANTIDAD) VALUES (4, 'Placa Madre', 'ASUS ROG', 30)")

# Insertar PRODUCTOS
con.execute("INSERT INTO PRODUCTO (ID, NOMBRE, DESCRIPCION, CANTIDAD) VALUES (1, 'Laptop Gaming', 'Laptop de alto rendimiento', 20)")
con.execute("INSERT INTO PRODUCTO (ID, NOMBRE, DESCRIPCION, CANTIDAD) VALUES (2, 'PC Escritorio', 'Computadora de oficina', 35)")
con.execute("INSERT INTO PRODUCTO (ID, NOMBRE, DESCRIPCION, CANTIDAD) VALUES (3, 'Servidor', 'Servidor empresarial', 10)")

# Insertar relación PROVEEDOR suministra COMPONENTE
con.execute("INSERT INTO proveedor_suministra_componente (ID_PROVEEDOR, ID_COMPONENTE) VALUES (1, 1)")
con.execute("INSERT INTO proveedor_suministra_componente (ID_PROVEEDOR, ID_COMPONENTE) VALUES (1, 2)")
con.execute("INSERT INTO proveedor_suministra_componente (ID_PROVEEDOR, ID_COMPONENTE) VALUES (2, 3)")
con.execute("INSERT INTO proveedor_suministra_componente (ID_PROVEEDOR, ID_COMPONENTE) VALUES (2, 4)")
con.execute("INSERT INTO proveedor_suministra_componente (ID_PROVEEDOR, ID_COMPONENTE) VALUES (3, 1)")
con.execute("INSERT INTO proveedor_suministra_componente (ID_PROVEEDOR, ID_COMPONENTE) VALUES (3, 3)")

# Insertar relación PRODUCTO compone COMPONENTE
con.execute("INSERT INTO producto_compone_componente (ID_PRODUCTOS, ID_COMPONENTE) VALUES (1, 1)")
con.execute("INSERT INTO producto_compone_componente (ID_PRODUCTOS, ID_COMPONENTE) VALUES (1, 2)")
con.execute("INSERT INTO producto_compone_componente (ID_PRODUCTOS, ID_COMPONENTE) VALUES (1, 3)")
con.execute("INSERT INTO producto_compone_componente (ID_PRODUCTOS, ID_COMPONENTE) VALUES (2, 1)")
con.execute("INSERT INTO producto_compone_componente (ID_PRODUCTOS, ID_COMPONENTE) VALUES (2, 4)")
con.execute("INSERT INTO producto_compone_componente (ID_PRODUCTOS, ID_COMPONENTE) VALUES (3, 1)")
con.execute("INSERT INTO producto_compone_componente (ID_PRODUCTOS, ID_COMPONENTE) VALUES (3, 2)")

# Insertar PIEZAS (relación 1:N con COMPONENTE)
con.execute("INSERT INTO PIEZA (ID, STOCK, DESCRIPCION, ID_COMPONENTE) VALUES (1, 200, 'Transistor tipo A', 1)")
con.execute("INSERT INTO PIEZA (ID, STOCK, DESCRIPCION, ID_COMPONENTE) VALUES (2, 150, 'Capacitor 10uF', 1)")
con.execute("INSERT INTO PIEZA (ID, STOCK, DESCRIPCION, ID_COMPONENTE) VALUES (3, 300, 'Chip memoria', 2)")
con.execute("INSERT INTO PIEZA (ID, STOCK, DESCRIPCION, ID_COMPONENTE) VALUES (4, 100, 'Controlador NAND', 3)")
con.execute("INSERT INTO PIEZA (ID, STOCK, DESCRIPCION, ID_COMPONENTE) VALUES (5, 80, 'Socket CPU', 4)")

# Insertar CONVENIOS (relación 1:N con PROVEEDOR, con ON DELETE CASCADE)
con.execute("INSERT INTO CONVENIO (ID, DESCRIPCION, ID_PROVEEDOR) VALUES (1, 'Convenio anual 2024', 1)")
con.execute("INSERT INTO CONVENIO (ID, DESCRIPCION, ID_PROVEEDOR) VALUES (2, 'Descuento por volumen', 1)")
con.execute("INSERT INTO CONVENIO (ID, DESCRIPCION, ID_PROVEEDOR) VALUES (3, 'Contrato exclusivo', 2)")
con.execute("INSERT INTO CONVENIO (ID, DESCRIPCION, ID_PROVEEDOR) VALUES (4, 'Acuerdo de distribución', 3)")

con.close()