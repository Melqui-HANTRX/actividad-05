ventas = []

while True:
    print("---MENÚ ANALISIS DE VENTAS---\n ")

    print("1. Ingrese las ventas (solo valores enteros positivos)")
    print("2. Ver todas las ventas ingresadas")
    print("3. Calcular la venta más alta y la más baja")
    print("4. Calcular promedio de ventas")
    print("5. Contar cuántos días superaron los Q1000")
    print("6. Clasificar cada venta: alta (>1000), media (500-1000), baja (<500)")
    print("7. Salir")

    menuinteractivo = input("Seleccione una opción: ")

    match menuinteractivo:
        case "1":
            lista = input("¿Cuántos días desea ingresar?: ")
            if lista.isdigit() and int(lista) > 0:
                lista = int(lista)
                i = 1
                while lista != 0:
                    ventasIngresadas = input(f"Favor de ingresar el valor de la venta del día {i}: ")
                    if ventasIngresadas.isdigit() and int(ventasIngresadas) > 0:
                        ventas.append(int(ventasIngresadas))
                        lista -= 1
                        i += 1
                    else:
                        print("La cantidad no es válida, el número debe ser entero positivo.")
            else:
                print("La cantidad no es válida")

        case "2":
            if len(ventas) > 0:
                print("Las ventas ingresadas son:")
                for i in range(len(ventas)):
                    print(f"En el día {i+1} las ventas fueron de Q{ventas[i]}")
            else:
                print("No hay ventas ingresadas.")

        case "3":
            if len(ventas) > 0:
                ventas_maximas = ventas[0]
                ventas_minimas = ventas[0]
                for i in ventas:
                    if i > ventas_maximas:
                        ventas_maximas = i
                    if i < ventas_minimas:
                        ventas_minimas = i
                print(f"La venta mínima (baja) fue Q{ventas_minimas} y la venta máxima (alta) fue Q{ventas_maximas}")
            else:
                print("No hay ventas ingresadas.")

        case "4":
            if len(ventas) > 0:
                totalventas = 0
                for i in ventas:
                    totalventas += i
                recuentoventas = totalventas / len(ventas)
                print(f"El promedio de ventas fue de Q{round(recuentoventas, 2)}")
            else:
                print("No hay ventas ingresadas aún.")

        case "5":
            if len(ventas) > 0:
                conteoVentas = 0
                for i in ventas:
                    if i > 1000:
                        conteoVentas += 1
                print(f"En {conteoVentas} día(s) se superaron los Q1000 en ventas")
            else:
                print("No hay ventas ingresadas.")

        case "6":
            if len(ventas) > 0:
                ventasAltas = []
                ventasBajas = []
                ventasconmitidas = []
                for i in ventas:
                    if i > 1000:
                        ventasAltas.append(i)
                    elif i <= 1000 and i > 500:
                        ventasconmitidas.append(i)
                    elif i <= 500:
                        ventasBajas.append(i)
                print("Las ventas son:")
                print(f"Ventas más altas: {ventasAltas}")
                print(f"Ventas más bajas: {ventasBajas}")
                print(f"Ventas medias: {ventasconmitidas}")
            else:
                print("No hay ventas ingresadas.")

        case "7":
            print("\nGracias por visitarnos.....")
            break

        case _:
            print("Opción no válida.")

