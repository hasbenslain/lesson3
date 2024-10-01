myfavfruits =  int(input("pila akong ganahan nga fruits"))
myfavfruit =[]

for i in range(myfavfruits):
    myfavfruits = input("enter a fruits")
    myfavfruit.append(myfavfruits)
    
    print(myfavfruit)
    
    for data in myfavfruits:
        if data == "banana":
            break
        elif data == "apple":
            print ("happy eating")       
       

    
