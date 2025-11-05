import apsw as sql
con = sql.Connection("mi_db.sqlite")

# Proveedores y sus convenios
# cursor = con.execute('''
#     SELECT P.ID, P.NOMBRE, C.DESCRIPCION 
#     FROM PROVEEDOR P
#     LEFT JOIN CONVENIO C ON P.ID = C.ID_PROVEEDOR
# ''')

# for i in cursor:
#     print('---')
#     print(i[0], i[1])

# Proveedores y sus convenios
# cursor = con.execute('''
#     SELECT P.NOMBRE, C.NOMBRE, C.DESCRIPCION
#     FROM PROVEEDOR P
#     JOIN proveedor_suministra_componente PSC ON P.ID = PSC.ID_PROVEEDOR
#     JOIN COMPONENTE C ON PSC.ID_COMPONENTE = C.ID
# ''')

# for i in cursor:
#     print('---')
#     print(i[0], i[1], i[2])

# Componentes utilizados por cada producto
# cursor = con.execute('''
#     SELECT P.NOMBRE, C.NOMBRE, C.DESCRIPCION
#     FROM PRODUCTO P
#     JOIN producto_compone_componente PCC ON P.ID = PCC.ID_PRODUCTOS
#     JOIN COMPONENTE C ON PCC.ID_COMPONENTE = C.ID
# ''')

# for i in cursor:
#     print('---')
#     print(i[0], i[1], i[2])

# Consulta basica sobre proveedores
cursor = con.execute('''
    SELECT * FROM PROVEEDOR
''')

print('---PROVEEDORES---')
for i in cursor:
    print('---')
    print(i[0], i[1])

cursor = con.execute('''
    SELECT * FROM CONVENIO
''')

print('---CONVENIOS---')
for i in cursor:
    print('---')
    print(i[0], i[1], i[2])


# ELIMINO PROVEEDOR CON ID 1
print('---ELIMINO PROVEEDOR 1---')
con.execute("DELETE FROM CONVENIO WHERE ID = 3")

# Consulta basica sobre proveedores
cursor = con.execute('''
    SELECT * FROM PROVEEDOR
''')

print('---PROVEEDORES---')
for i in cursor:
    print('---')
    print(i[0], i[1])

cursor = con.execute('''
    SELECT * FROM CONVENIO
''')

print('---CONVENIOS---')
for i in cursor:
    print('---')
    print(i[0], i[1], i[2])

con.close()