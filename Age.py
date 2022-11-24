#.....this code will help your to know your age  created on 01 Mar 2021 

print("do you want to know how old you are?")

print("what is the year now? e.g 2020")

year_now = int(input('the year now; '))

print("in which year were you born e.g 1980. if you want to go back enter \'0\'")

year_born = int(input('enter the year you were born; '))

if year_born == 0 :
  year_now = int(input('the year now; '))
  year_born = int(input('enter the year you were born; '))
else:
  pass

if year_born > 0 :
  age = year_now - year_born

print(f'you are {age} years old' )

quit()