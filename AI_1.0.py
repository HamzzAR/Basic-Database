from time import sleep
import glob
import os

def check_dir(p_name):
  filename = glob.glob('*.txt')
  reply = True
  for line in filename:
    if line[:-4] == p_name:
      reply = False
  return reply

def ask_Q():
  q = input('Enter Query: ')
  q = q.lower()
  if q:
    q = q.replace('?', '')
  print('Extracting Data...')
  sleep(1)
  print('Please Wait...')
  sleep(0.6)
  listt = q.split()
  count = 0
  filename = glob.glob('*.txt')
  for line in filename:
    if filename[count][:-4] in q:
      name = open('{}'.format(filename[count]), 'rt')
      lines = name.readlines()
      for line in lines:
        tem_line = line.lower()
        tem_line = tem_line.split()
        for i in listt:
          if i in tem_line:
            print(line)
            sleep(1)
            break
    count+=1
  
def add_details():
  name = str(input('Enter Name: '))
  name = name.lower()
  check = check_dir(name)
  if check == False:
    names = open('{}.txt'.format(name), 'a')
    title = 'None'
    while title != '':
      title = str(input('Enter a title (Or Press ENTER to Exit): '))
      if title != '':
        detail = str(input('Enter Details: '))
        names.write(title + ' : ' + str(detail) + '\n')
    print('Please Wait...')
    sleep(1.5)
    print('Customers Saved')
    sleep(2)
    names.close()
    
def delete():
  name = input('Enter name: ')
  name.lower()
  option = input('Are you sure you want to DELETE this file?(y/n): ')
  if option == 'y':
    print('Deleting..')
    sleep(2)
    check = check_dir(name)
    if check == False:
      full_name = name + '.txt'
      os.remove(full_name)
      print('File Deleted.')
      sleep(1)
    else:
      print('Not Found')
      sleep(1)
  else:
    print('Cancelled')
    sleep(1)
  
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
  else:
    print(name.upper(),'already exist')
    sleep(1)
  
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
    lines = names.readlines()
    print('Found: 1')
    sleep(1)
    print()
    for x in lines:
      print(x, end='')
    sleep(2)
  else:
    print(name.upper(),'does NOT exist')
    sleep(1)
