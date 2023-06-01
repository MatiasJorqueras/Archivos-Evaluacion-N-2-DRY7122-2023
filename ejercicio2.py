import subprocess

Disco = subprocess.check_output("df -h /", text=True, shell=True)
Memoria = subprocess.check_output("free -h", text=True, shell=True)
Cpu = subprocess.check_output("lscpu", text=True, shell=True)
Red = subprocess.check_output("ifconfig", text=True, shell=True)

print("Especificaciones del Disco:")
print(Disco)
print("\n")
print("Especificaciones de la Memoria:")
print(Memoria)
print("\n")
print("Especificaciones de la CPU:")
print(Cpu)
print("\n")
print("Especificaciones de la red:")
print(Red)
