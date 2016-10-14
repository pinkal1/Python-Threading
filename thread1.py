import threading


def fun1():                                   //created function 1
  print("Function 1")
  return

def fun2(args):                               //created function 2
  print("Number is:%s"%args)
  return

threads = []
for i in range(1):
  t=threading.Thread(target=fun1)             //Initializing thread 1
  threads.append(t)
  t.start()                                   //Starting Thread1

  t1=threading.Thread(target=fun2,args=(1,))  //Initializing thread 2
  threads.append(t1)
  t1.start()                                  //Starting Thread2


"""Output is :
             Function 1
             Number is: 1
"""
