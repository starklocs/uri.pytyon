L1 = input().split();
cod1 = int(L1[0]);
NPeca1 = int(L1[1]);
VUnit1 = float(L1[2]);

L2 = input().split();
cod2 = int(L2[0]);
NPeca2 = int(L2[1]);
VUnit2 = float(L2[2]);
total = (NPeca1 * VUnit1) + (NPeca2 * VUnit2);
print('VALOR A PAGAR: R$ %0.2f'%total);

