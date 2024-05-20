# printing a multivalue data
print("pratik","emma",1,2.2,4j,True,False)
# output-  pratik emma 1 2.2 4j True False

# between the values default space is there
print("vishal","pratik",23,24)
# output- vishal pratik 23 24

#print function when end its goes to next line by default
print("vishal",24)
print("pratik",23)
# output-
# vishal 24
# pratik 23

#changing default seprator in print
print("pratik","emma",1,2.2,4j,True,False,sep="->")
print("Pratik",45,sep="=")
print("vishal",45,sep="\n")
# output-
# pratik->emma->1->2.2->4j->True->False
# Pratik=45
# vishal
# 45

#changing the default end (its skip to new line )
print("Pratik",45,end=" ")
print("vishal",47)
# output- Pratik 45 vishal 47