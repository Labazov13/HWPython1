# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticketNumber=int(input("Введите номер билета: "))
if(ticketNumber>=100000 and ticketNumber<=999999):
    if((ticketNumber//100000)+((ticketNumber//10000)%10)+((ticketNumber//1000)%10)==((ticketNumber%1000)//100)+(((ticketNumber%1000)//10)%10)+((ticketNumber%1000)%10)):
       print("Ваш билет счастливый!")
    else:
        print("Ваш билет не счастливый(")
else:
    print("У вашего билета должно быть строго 6 цифр!")