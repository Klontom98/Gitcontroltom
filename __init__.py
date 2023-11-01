


from operaciones import add 
from operaciones import subtraction
from operaciones import multiply
from operaciones import division
from operaciones import potencia

def game():
  score = 1
  while True:
    print('======== Menu ========'
    '\n1. Add'
    '\n2. resta'
    '\n3. multi'
    '\n4. division'
    '\n5. potencia'
    '\n0. Exit')
    option = int(input('\nChoose an option: '))
    if option == 0:
      break
    num_1 = float(input('Enter the first number: '))
    num_2 = float(input('Enter the second number: '))
    answer = float(input('Enter your answer: '))
    
    if option == 1:
      result = add(num_1, num_2)
      if result == answer:
         score += 1
         print('Correct!!')
      else:
         print('Incorrect')
    elif option == 2:
      result = subtraction(num_1, num_2)
      if result == answer:
         score += 1
         print('Correct!!')
      else:
         print('Incorrect')
    elif option == 4:
      result = division(num_1, num_2)
      if result == answer:
         score += 2
         print("Correct")
      else:
        print("Incorrect")
      
    elif option == 5:
      result = potencia(num_1, num_2)
      if result == answer:
        score += 4
        print('Correct')
      else:
        print("Incorrect")

    elif option == 3:
       result = multiply(num_1, num_2)
       if result == answer:
          score += 2
          print('Correct!!')
       else:
          print('Incorrect')

  print(f'======== Game Over ========'
        f'\nYour score is {score}'
        '\nKeep going!')

game()
