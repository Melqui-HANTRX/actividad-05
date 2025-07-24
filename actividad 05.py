ventas = []

while menuinteractivo !=7 :
 print("---MENÚ ANALISIS DE VENTAS---")

 print("\n 1. Ingrese las ventas(solo valores enteros positivos)")
 print("2. Ver todas las ventas ingresadas)")
 print("3. Calcular la venta mas alta y la mas baja")
 print("4. Calcular promedio de ventas")
 print("5. Contar cuentos dias superaron los Q1000")
 print("6. Clasificar cada venta:(>1000), media (500-1000), baja(<500)")
 print("7. Salir")

menuinteractivo = input("Seleccione una opción: ")

match menuinteractivo:
 case "1":
  lista = input("Cuantos dias desea ingresar?: ")
  if lista.isdigit() and int(lista)>0:
   lista = int(lista)
   i =1
   while lista: !=0:
   ventasIngresadas = input(f"Favor de ingresar el valor de la venta del dia{i}: ")
   if ventasIngresadas.isdigit() and int(ventasIngresadas)>0:
    ventas.append(int(ventasIngresadas))
    lista = int(lista)
    i += 1
   else:
    print("La cantidad no es valida, el numero debe ser entero positivo.")
  else:
    print("La cantidad no es valida")
 case "2":
  if len(ventas)>0:
   print("Las ventas ingresadas son: ")
   for i in range(len(ventas)):
    print(f"En el dia {i+1}  las ventas fueron de Q{ventas[i]}")
   else:
    print("No hay ventas ingresadas.")
 case "3":
  if len(ventas)>0:
    ventas_maximas = ventas[0]
    ventas_minimas = ventas[0]
    for i in ventas:
      if i > ventas_maximas:
          ventas_maximas = i
      if i < ventas_minimas:
           ventas_minimas = i
    print(f"La venta minima(baja) fue Q{ventas_minimas} y la venta maxima(alta) fue Q{ventas_maximas}")
  else:
   print("No hay ventas ingresadas. ")
 case "4":
  if len(ventas)>0:
   totalventas = 0
   for i in ventas:
    totalventas += i
    recuentoventas = totalventas/len(ventas)
    print(f"El promedio de ventas fue de Q{recuentoventas,2}")














