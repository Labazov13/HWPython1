# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

rowChocolate=int(input("Сколько рядов в шоколадке: "))
columnChocolate=int(input("Сколько столбцов в шоколадке: "))

requiredChocolate=int(input("Сколько долек требуется получить: "))
if(requiredChocolate<rowChocolate*columnChocolate):
    if((rowChocolate*columnChocolate)%requiredChocolate==0 or requiredChocolate%rowChocolate==0 or requiredChocolate%columnChocolate==0):
        print("Это возможно!")
    else:
        print("Это не возможно")
