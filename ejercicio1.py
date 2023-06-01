import datetime
import subprocess
import re

hora_actual = datetime.datetime.now()
ult_hora = hora_actual - datetime.timedelta(hours=1)
ult_hora = ult_hora.replace(minute=0, second=0, microsecond=0)
ini_hora = ult_hora.replace(hour=ult_hora.hour - 1) if ult_hora >=1 else ult_hora.replace(hour=23)
fin_hora = ult_hora
inicial = ini_hora.strftime('%H:%M:%S')
final = fin_hora.strftime('%H:%M:%S')
ruta = '/var/log/auth.log'
contra = r"\bFailed password\b"
int_fa = 0
with open(ruta, 'r') as registros:
    for linea in registros:
        tiempo = linea.split()[2]
        total = tiempo.split(':')
        hora = int(total[0])
        minuto = int(total[1])

        if ini_hora.hour <= hora <= fin_hora.hour and ini_hora.minute <= minuto <= fin_hora.minute:
            if re.search(contra, linea):
                int_fa=int_fa+1

print(f"La cantidad de intentos fallidos en el rango de tiempo de {inicial} hasta {final} es de: {int_fa}")
