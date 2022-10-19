v = float(input())
print("NOTAS:")

x = float(v // 100)
print('{} nota(s) de R$ 100.00'.format(x))
v -= x * 100

x = float(v // 50)
print('{} nota(s) de R$ 50.00'.format(x))
v -= x * 50

x = float(v // 20)
print('{} nota(s) de R$ 20.00'.format(x))
v -= x * 20

x = float(v // 10)
print('{} nota(s) de R$ 10.00'.format(x))
v -= x * 10

x = float(v // 5)
print('{} nota(s) de R$ 5.00'.format(x))
v -= x * 5

x = float(v // 2)
print('{} nota(s) de R$ 2.00'.format(x))
v -= x * 2

print('{} nota(s) de R$ 1.00'.format(v))

print("MOEDAS:")
x = float(v // 1)
print('{} moeda(s) de R$ 1.00'.format(x))
v -= x * 1

x = float(v // 0.50)
print('{} moeda(s) de R$ 0.50'.format(x))
v -= x * 0.50

x = float(v // 0.25)
print('{} moeda(s) de R$ 0.25'.format(x))
v -= x * 0.25

x = float(v // 0.10)
print('{} moeda(s) de R$ 0.10'.format(x))
v -= x * 0.10

x = float(v // 0.5)
print('{} moeda(s) de R$ 0.05'.format(x))
v -= x * 0.05

x = float(v // 0.5)
print('{} moeda(s) de R$ 0.01'.format(x))
v -= x * 0.01
