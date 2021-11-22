#amt = 10
#if(amt >20):
    #print("you are eligiable to purchase")
#else:
    #print("you are not enligiable to purchase")
#...................................................#
#Exception - programe
#num = 100
#result = 100/0
#print("The result is : ",result) 
#..........................................................#
#
#a = [1,2,3]
#try:
 #   print("first element = %d" %(a[0]))
  #  print("second element = %d" %(a[1]))
   # print("fourth element = %d" %(a[3]))

    #   except:
     #       print("An error occoured")
    
 #.......................................................#
     #try with else clause
   # def fun(a,b):
    #     try:
     #        c = ((a+b)/(a-b))
      #       except zerodivisionerror:
       #          print("a/b results in 0")
        #         else:
         #            print(c)
##
  #                   fun(2,3)
   #                  fun(3,3)
   #........................................................#

   #finally block

   try:
       k = 5/0
       print(k)

   except ZeroDivisionError:
       print("values can't be divided by zero")

   else:
       print("Else block Exicutive")
       print(k)

   finally:
       print("this block always executes")



   

    

    
