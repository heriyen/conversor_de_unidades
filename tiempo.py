"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """

def segundo_a_minutos(sec):
    min = sec / 60
    return min

def segundo_a_horas(sec):
    hr = sec / 3600
    return hr

def minutos_a_segundos(min):
    sec = min * 60
    return sec

def minutos_a_horas(min):
    hr = min / 60
    return hr

def horas_a_segundo(hr):
    sec = hr *3600
    return sec

def horas_a_minutos(hr):
    min = hr * 60
    return min
if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplos de conversión de tiempo:")
    print("250 sec a minutos:",segundo_a_minutos(250))
    print("980 sec a horas:",segundo_a_horas(980))
    print("20 min a segundos:",minutos_a_segundos(20))
    print("270 min a horas:",minutos_a_horas(270))
    print("360 hr a segundos:",horas_a_segundo(360))
    print("10 hr a minutos:",horas_a_minutos(10))