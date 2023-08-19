from pyfiglet import Figlet

f = Figlet(font= "standard")

print(f.renderText("Store mahdi"))



def show_menu():

    print("1- Add product")

    print("2- Edit product")

    print("3- Delete product")

    print("4- Search")

    print("5- Show list")

    print("6- Buy")

    print("7- exit")



show_menu()

choice = int(input("please choice a number:"))

# !!! attention !!!

#chang the path aftery moving the database accuralty



rotation = True

while rotation :

    

    myfile = open("agnas1.txt" , "r")

data = myfile.read()







PRODUCT = []

product_list = data.split("\n")

for i in range(len(product_list)):

    product_info  =product_list[i].split(",")

    mydict = {}

    mydict["id"] = product_info[0]

    mydict["name"] = product_info[1]

    mydict["price"] = product_info[2]

    mydict["count"] = product_info[3]

    PRODUCT.append(mydict)






#Add product


def Addproduct ():
            break

  id=input("cod ganse ra bego :")

name=input("asme gans ra bego :")

price=input("ghaymat gans ra bego:")

count=input("tadad gans ra bego:")

myfile = open("agnas1.txt" , "a") 

myfile.write("/n" + id +name + price + count) 

myfile.cloes()

print("gans azafe shod")



#Edit product

def Editproduct():
            break


   print(PRODUCT)

for x in range(len(PRODUCT)):

    print(PRODUCT[x][name])

name = input("codame ra mekhahy taghir bedy:")

for i in range(len(PRODUCT)-1):

  print(i)

  if name == PRODUCT[i]["name"]:

      PRODUCT.pop(i)

      id = input("cod ra varad conid:")

      name = input("name ra vared conid:")

      price = input ("ghaymat ra vared conid ")

      count = input("tadad ra vared conid:")

      mydict = {"id":id,"name":name,"price":price,"count":count}

      PRODUCT.append(mydict)

      data=""#storemahdi

      for y in range(len(PRODUCT)):

          data+= PRODUCT[y]["id"] +","+PRODUCT[y]["price"]+"," + PRODUCT[y]["count"]

          if y !=len(PRODUCT)-1:

              #by mahdi

              data+="/n"

              myfile = open("agnas1.txt" , "w")

              myfile.write(data)

              myfile.close()

              print("product editend!")

              

#Delete product


def Deleteproduct():
            break

    for x in range(len(PRODUCT)):

        print(PRODUCT[x]["name"])

        name  = input("che gansi ra mikhahy taghir dahid")

        for i in range(len(PRODUCT)):

            if name == PRODUCT[i]["name"]:

                #by mahdi

                PRODUCT.pop(i)

                data = ""

                for y in range (len(PRODUCT)):

                    data+=PRODUCT[y]["id"] +"," + PRODUCT[y]["name"]+","+("agnas1.txt" , "w")

                    myfile.write(data)

                    myfile.close()

                    print("delet shod")



                    
#search product                

def Searchproduct():
                break

    name=input("name ra vared conid:")

    for i in range(len(PRODUCT)):

        if PRODUCT[i]["name"] == name:

            print("atelat gans shoma amade")

            print("id:",PRODUCT[i]["id"])

            print("name:",PRODUCT[i]["name"])

            print("price:",PRODUCT[i]["price"])

            print("count:", PRODUCT[i][count])

        else:#by mahdi

            print("gans paida nemy shavad!")

            

#Show list      
def Showlist():
            print(PRODUCT[i]["code"]," -",PRODUCT[i]["


    print("list of producte in{id/name}order:")

    print("id/name/price/count")

    for i in range(len(PRODUCT)):

        print(PRODUCT[i]["id"],"/",PRODUCT[i]["price"],"/",PRODUCT[i]["count"])



#buy product

def Buy():
            break


while True:

    print("list of product in {id/name}oder :")

    #by mahdi

    for i in range(len(PRODUCT)):

        #by mahdi

        print(PRODUCT[i]["id"],"/",PRODUCT[i]["name"])

        id = input("che chizy ra mekhahy:")

        quan = input("enter the quan bought product:")

        for i in range(len(PRODUCT)):

            if id == PRODUCT[i]["id"]:

                count = int(PRODUCT[i]["id"]["count"])

                count=quan

                PRODUCT[i]["count"]=str(count)

                print("angame shod")



#exit product

elif choice ==7:

    rotation = False

    print("khareg shodin")





















   

