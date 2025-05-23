# READ 

# their are two ways to open file 

# first way
# var=open('file.txt')
# print(var.read())
# var.close() # we have to manually close the file

# second way - ** recommended ** # dont need to manullay close it auto close
# with open('file.txt') as f:
  # print(f.read())
  # print(f.readline())
  # print(f.readlines())  

# WRITE

# with open('hello.txt','w') as f:
  # f.write('hello this is jitesh shelke')
  # f.writelines(['hello this is jitesh shelke\n','this is second line\n','this is third line'])
  # print(f.tell())
  

# APPEND

# with open('hello.txt','a') as f:
#   f.write('\nthis is fourth line')


# USING r+ . read as well as write 

# with open('file.txt','r+') as f:
#   print(f.read())
#   print(f.tell())
#   f.write('\nthis is my cv')
  

# USINF W+ write as well as read

# with open('file.txt','w+') as f:
  # f.write('my name is jitesh')
  # f.writelines(['my name is jitesh\n','this is second line\n','this is third line'])
  # print(f.tell())
  # f.seek(0)
  # print(f.read())

  
# USING a+ write as well as read

with open('file.txt','a+') as f:
  print(f.write('\nthis is four line'))
  print(f.tell())
  f.seek(0)
  print(f.read())


