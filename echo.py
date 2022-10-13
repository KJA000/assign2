
def exit(a):
   if a=="exit":
      return 0
   else: return 1

while(1):
 a = input()
 if not exit(a): break
 else:
   print(a) 
   continue 