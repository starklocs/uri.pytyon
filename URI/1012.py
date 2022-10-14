#L1 = input().split();
#a = float(L1[0]);
#b = float(L1[1]);
#c = float(L1[2]);
#
#triangulo = (a  * c) / 2;
#circulo = 3.14159 * (c*c)
#trapezio = ((a + b) * c) / 2;
#quadrado = b * b;
#retangulo = a * b;
#
#print("TRIANGULO: %0.3f" %triangulo)
#print("CIRCULO: %0.3f" %circulo)
#print("TRAPEZIO: %0.3f" %trapezio)
#print("QUADRADO: %0.3f" %quadrado)
#print("RETANGULO: %0.3f" %retangulo)
a, b,c = [float(x) for x in str(input()).split()];
print('TRIANGULO: {:.3f}'.format((a  * c) / 2));
print('CIRCULO: {:.3f}'.format(3.14159 * (c*c)));
print('TRAPEZIO: {:.3f}'.format(((a + b) * c) / 2));
print('QUADRADO: {:.3f}'.format(b * b));
print('RETANGULO: {:.3f}'.format(a * b));