"""1) Módulo temperatura.py: Este módulo debe contener funciones para convertir entre diferentes unidades de temperatura, como Celsius, Fahrenheit y Kelvin.(0.5 puntos) """
"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
"""3) Crear el primer versionamiento con git de los dos módulos creados de temperatura y masa (usar git add y git commit ). (0.5 puntos) """
"""4) Crear una nueva rama llamada “desarrollo” y en esta nueva rama agregar los módulos tiempo.py y convertidor.py (recuerda usar git branch ). (0.5 puntos) """
"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
"""6) Módulo convertidor.py: Este módulo importa los módulos de masa, temperatura y tiempo. Actúa como el punto de entrada del programa. Debe permitir a los usuarios seleccionar la categoría de conversión deseada (temperatura, masa o tiempo), ingresar el valor a convertir y las unidades de origen y destino, y obtener el resultado de la conversión.(2 puntos) """
"""7) Versionar esta rama “desarrollo” con git add y git commit para luego fusionar con la rama master (para fusionar, usar: git merge). (1 punto) """
""" Desde la rama main o master subir al nuevo repositorio de github llamado conversor_de_unidades. (1 punto) """

""" Recuerda que cada uno de los módulos, deben incluir el bloque if __name__ == "__main__" para sus pruebas en cada módulo. """

import temperatura 
import masa
import tiempo
def main():
    while True:
        # Muestra el menú principal
        print("Menú Principal:")
        print("[1]convertir celsius a fahrenheint")
        print("[2]convertirt celsius a kelvin")
        print("[3]convertir fahrenheit a celsius")
        print("[4]convertir fahrenheint a kelvin")
        print("[5]convertir kelvin a celsius")
        print("[6]convertir kelvin a fahrenheint")
        print("[7]convertir kilogramos a gramos")
        print("[8]convertir kilogramos a toneladas")
        print("[9]convertir gramos a kilogramos")
        print("[10]convertir gramos a toneladas")
        print("[11]convertir toneladas a kilogramos")
        print("[12]convertir toneladas a gramos")
        print("[13]convertir segundos a minutos")
        print("[14]convertir segundos a horas")
        print("[15]convertir minutos a horas")
        print("[16]convertir minutos a segundos")
        print("[17]convertir horas a segundos")
        print("[18]convertir horas a minutos")
        # Solicita al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")
        valorinicial= int(input("ingresa numero :"))

        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                resultado= temperatura.celsius_a_fahrenheit(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 2:
                resultado= temperatura.celsius_a_kelvin(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 3:
                resultado= temperatura.fahrenheit_a_celsius(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 4:
                resultado= temperatura.fahrenheit_a_kelvin(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 5:
                resultado= temperatura.kelvin_a_celsius(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 6:
                resultado= temperatura.kelvin_a_fahrenheit(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 7:
                resultado= masa.Kilogramos_a_Gramos(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 8:
                resultado= masa.Kilogramos_a_toneladas(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 9:
                resultado= masa.gramos_a_kilogramos(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 10:
                resultado= masa.Gramos_a_toneladas(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 11:
                resultado= masa.toneladas_a_kilogramos(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 12:
                resultado= masa.toneladas_a_Gramos(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 13:
                resultado= tiempo.segundo_a_minutos(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 14:
                resultado= tiempo.segundo_a_horas(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 15:
                resultado= tiempo.minutos_a_horas(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 16:
                resultado= tiempo.minutos_a_segundos(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 17:
                resultado= tiempo.horas_a_segundo(valorinicial)
                print("el resultado es :", resultado)
            elif opcion == 18:
                resultado= tiempo.horas_a_minutos(valorinicial)
                print("el resultado es :", resultado)
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

if __name__ == "__main__":
    main()

    