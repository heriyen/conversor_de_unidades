"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """

def Kilogramos_a_Gramos(Kg):
    g = Kg * 1000
    return g

def Kilogramos_a_toneladas(kg):
    t = kg / 1000
    return t

def gramos_a_kilogramos(g):
    kg = g / 1000
    return kg

def Gramos_a_toneladas(g):
    t = g / 1000000
    return t

def toneladas_a_kilogramos(t):
    kg = t * 1000
    return kg

def toneladas_a_Gramos(t):
    g = t * 1000000
    return g
if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplos de conversión de masa:")
    print("250 kg a g:",Kilogramos_a_Gramos(250))
    print("98 kg a t :",Kilogramos_a_toneladas(98))
    print("20 g a kg:",gramos_a_kilogramos(20))
    print("270 g a t:", Gramos_a_toneladas(270))
    print("36 t a kg :",toneladas_a_kilogramos(36))
    print("10 t a g:",toneladas_a_Gramos(10))
