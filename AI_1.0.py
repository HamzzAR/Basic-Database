from time import sleep
import glob
import os
def main():
  print()
  option2 = int(input('1. Add\n2. Search\n3. Exit\n(1/2/3): '))
  if option2 == 1:
    add_file()
  elif option2 == 2:
    search_file()
  else:
    print('Exiting...')
    sleep(2)
    print('GoodBye!')

def check_dir(p_name):
  filename = glob.glob('*.txt')
  reply = True
  for line in filename:
    if line[:-4] == p_name:
      reply = False
  return reply

def add_file():
  name = str(input('Enter Name: '))
  name = name.lower()
  check = check_dir(name)
  if check == True:
    names = open('{}.txt'.format(name), 'wt')
    names.write('Name : '+ name + '\n')
    age = int(input('Enter age: '))
    fav = str(input('Enter Fav colour: '))
    names.write('Age : ' + str(age) + '\n')
    names.write('Favourite colour : ' + fav + '\n')
    title = 'None'
    while title != '':
      title = str(input('Enter more details(e.g Height,weight,employment status etc.)\nOr Press ENTER to skip\nEnter a title: '))
      if title != '':
        detail = str(input('Enter Detail: '))
        names.write(title + ' : ' + str(detail) + '\n')
    print('Please Wait...')
    sleep(1.5)
    print('Customers Saved')
    sleep(2)
    names.close()
    main()
  else:
    print(name.upper(),'already exist')
    sleep(1)
    main()
  
def search_file():
  name = str(input('Enter name: '))
  name = name.lower()
  print('Searching...')
  sleep(1.5)
  check = check_dir(name)
  if check == False:
    try:
      names = open('{}.txt'.format(name), 'rt')
    except:
      print('0 Customers Found! ')
      sleep(1)
      main()
    lines = names.readlines()
    print('Found: 1')
    sleep(1)
    print()
    for x in lines:
      print(x, end='')
    sleep(2)
    main()
  else:
    print(name.upper(),'does NOT exist')
    sleep(1)
    main()
main()
