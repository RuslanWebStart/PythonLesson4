# -*- coding: cp1251 -*-
print('���� 4')
print('������ 1')
# ������ 1
a, b = map(float, input('������� ������� �������������� ����� ������: ').split())
# ������� 
s = a * b
# ��������
p = (a + b) * 2
print('������� �������������� S: ', s)
print('�������� ��������������: ', p)

print('������ 2')
# ������ 2
a, b, c, d, i = map(int, input('������� �����: '))
x = ((d**i) * c) / (a - b)
print('X �����: ', x)
