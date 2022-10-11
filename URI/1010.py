L1 = input().split("");
L2 = input().split("");
cod1, NPeca1, VUnit1 = L1
cod2, NPeca2, VUnit2 = L2
total = (int(NPeca1)* float(VUnit1)) + (int(NPeca2) *float(VUnit2));
print('VALOR A PAGAR:%0.2f'%total);
