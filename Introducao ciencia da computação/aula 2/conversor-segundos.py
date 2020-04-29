numerodesegundos = input("Por favor, entre com o número de segundos que deseja converter: ")

totalsegundos = int(numerodesegundos)
dias = totalsegundos // 86400
segundosrestantes = totalsegundos % 86400
horas = segundosrestantes // 3600
minutos = (segundosrestantes % 3600) // 60
segundos = (segundosrestantes % 3600) % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")


