# Exercicio 2006 "Indentificando chá"
t = int(input())
resp = list(map(int, input().split()))
point = 0
# (1) o chá branco; (2) chá verde; (3) chá preto; ou (4) chá de ervas. 
for i in resp:
    if i == t:
        point += 1
print(point)
