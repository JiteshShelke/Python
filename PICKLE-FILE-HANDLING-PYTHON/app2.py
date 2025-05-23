# class parent:
#   def add(self):
#     print('this is parent class')
# class child(parent):
#   def add(self):
#     print('this is child class')
#     super().add()
# class little(child):
#   def add(self):
#     print('this is little class')
#     super().add()

# obj=little()

# obj.add()

strr='hello i am jitesh shelke from pali khurd HELLO Helloadf90 my gmail is jitesh09@gmai.com mobile number is 9139848248'

import re

res=re.match('hello',strr)
print(res)
print(res.start())
print(res.end())
print(res.group())

