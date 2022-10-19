dt = int(input())
a = int(dt / 365)
dt -= a * 365
m = int(dt / 30)
dt -= m * 30

#print("{} ano (s)", "{} mes (es)", "{} dia (a)".format(a, m, dt), sep='\n')

print(a, 'ano(s)')
print(m, 'mes(es)')
print(dt, 'dia(s)')