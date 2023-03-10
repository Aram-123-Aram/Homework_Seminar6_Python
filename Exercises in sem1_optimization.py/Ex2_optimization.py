'''
Напишите программу, которая принимает на вход координаты двух точек и находит 
расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''
distance = lambda Ax,Ay,Bx,By: round(((Ax-Bx)**2+(Ay-By)**2)**0.5, 2)

print(distance(3,6,2,1))
print(distance(7,-5,1,-1))