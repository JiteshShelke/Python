# import pickle

# # with open('file.bin','wb') as f:
# #   pickle.dump('hello my name is jitesh',f)
  
  
# # with open('file.bin','rb') as f:
# #   print(pickle.load(f))


# var=open('new.bin','wb')
# data='hello this is master jitesh'
# pickle_data=pickle.dumps(data)
# var.write(pickle_data)
# var.close()

# print(pickle.loads(pickle_data))


import pickle 

# data="hello my name is jitesh"
# data=pickle.dumps(data)
# print(pickle.loads(data))
# with open('new.bin','wb') as f:
#   f.write(data)

with open('new.bin','rb') as f:
  print(pickle.load(f))