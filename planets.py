def weight_on_planets():
   # write your code here
   weight_earth = int(input('What do you weigh on Earth? '))
   
   print(f'\nOn Mars you would weigh {weight_earth*.38} pounds.' + \
         f'\nOn Jupiter you would weigh {weight_earth*2.34} pounds.')  
   
if __name__ == '__main__':
   weight_on_planets()
