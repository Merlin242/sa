#A = int(input('1 chislo'))
#B = int(input('2 chislo'))

#for i in range(A, B + 1):
 #   print(i)
#A = int(input('1 chislo'))
#B = int(input('2chislo'))

#if A < B:

#  for i in range(A, B + 1):
 #       print(i)
#else:
  #  for i in range(A, B - 1, -1):
 #       print(i)
#N = int(input('1 chislo'))
#sum = 0

#for i in range(N):
#    num = int(input('2chislo'))
#    sum += num
#print(('Suma chisel')
#p = int(input('kolichestva chisel ctypene'))

#for i in range(1, p + 1):
   # for j in range(1, i + 1):
  #      print(j, end='')
 #   print()

#print()
#N = int(input('Ведите целое число'))

#i = 1
#while i ** 2 <= N:
    #print((i ** 2))
   # i += 1

#N = int(input('Ведите натуральное число N'))

#num = 0
#result = 1

#while result * 2 <= N:
 #   result *= 2
 #   num += 1

#print('f Наибольшие целая степен , не превосходящие {N} равно result')

#x = int(input())
#y = int(input())
#day = 1

#while x <= y:
 #   x += 0.1*x
 #   day += 1

#print('На',day ,'День пробег спротсмена составляет не менее',y , 'километров40')

#count = 0

#while True:
#    num = int(input("Введите число: "))

  #  if num == 0:
   #     break

  #  count += 1

#print("Количество членов последовательности:", count)

#count = 0
#prev_num = None

#while True:
   # num = int(input("Введите число: "))

  #  if num == 0:
  #      break

  #  if prev_num is not None and num > prev_num:
      #  count += 1

  #  prev_num = num

#print("Количество элементов больше предыдущего:", count)

#def fibon(p):
  #  if p < 2:
     #   return p
   # else:
    #    return fibon(p - 1) + fibon(p - 2)


#p = int(input("Введите номер числа Фибоначчи (p): "))


#result = fibon(p)


#print(f"{p}-е число Фибоначчи: {result}")


#length = 0
#current = 1

#prev_num = int(input("Введите число (0 для завершения): "))

#while prev_num != 0:
 #   num = int(input("Введите число (0 для завершения): "))

    #if num == prev_num:
    #    current += 1
   # else:
   #     length = max(length, current)
  #      current = 1

 #   prev_num = num

#print("Наибольшее число подряд идущих элементов:", length)



