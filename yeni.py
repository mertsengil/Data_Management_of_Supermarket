import sqlite3
import time

class Product():

    def __init__(self,kind,name,price,stock):

        self.kind=kind
        self.name=name
        self.price=price
        self.stock=stock

    def __str__(self):
        return "kind of product:{}\nname of product:{}\nprice of product:{}$\nstock of product:{}".format(self.kind,self.name,self.price,self.stock)

class Supermarket():

    def __init__(self):
        self.makeconnection()

    def makeconnection(self):

        self.connection=sqlite3.connect('supermarket.db')
        self.cursor=self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS SUPERMARKET(
        kind text,
        name text,
        price integer,
        stock integer
        )
        """)
        self.connection.commit()

    def disconnect(self):
        self.connection.close()


    def show_all_products(self):
        show_command ="SELECT * from SUPERMARKET"
        self.cursor.execute(show_command)
        products = self.cursor.fetchall()

        if(len(products) == 0):
            print("There are not any products in supermarket")
        else:
            for i in products:
                product = Product(i[0],i[1],i[2],i[3])
                print(product)
                print("--------------------------------")


    def add_new_product(self,data):
        add_command = "INSERT INTO SUPERMARKET VALUES {}"
        data = (kind,name,price,stock)
        self.cursor.execute(add_command.format(data))
        self.connection.commit()

    def delete_product(self,name):

        delete_command="DELETE FROM SUPERMARKET where name = ? "
        self.cursor.execute(delete_command,(name,))
        self.connection.commit()

    def update_stock(self,name,new_stock):
        select_command="SELECT * FROM SUPERMARKET where name = ?"
        self.cursor.execute(select_command,(name,))

        products = self.cursor.fetchall()

        if(len(products)==0):
            print("There is no this product in the supermarket")
        else:

            stock = new_stock
            update_command = "UPDATE SUPERMARKET SET stock = ? where name = ?"

            self.cursor.execute(update_command,(stock,name))
            self.connection.commit()

    def update_price(self,name,new_price):
        select_command_1="SELECT * FROM SUPERMARKET where name = ?"
        self.cursor.execute(select_command_1,(name,))

        products = self.cursor.fetchall()

        if(len(products)==0):
            print("There is no this product in the supermarket")
        else:

            price = new_price
            update_command_1 = "UPDATE SUPERMARKET SET price = ? where name = ?"

            self.cursor.execute(update_command_1,(price,name))
            self.connection.commit()


supermarket=Supermarket()
print("""
********************** welcome to Interface of your Supermarket **********************

1-) All products
2-) Add a new product
3-) Delete a product
4-) Update stock
5-) Update price
""")
while True:
    selection = input("Select an action(press 'q' for exit:")

    if(selection == "q"):
        print("Checking out...")
        time.sleep(1)
        break
    elif(selection == "1"):

        print("Printing...")
        time.sleep(2)
        supermarket.show_all_products()


    elif(selection == "2"):

        kind = input("Kind:")
        name = input("name:")
        price = int(input("price:"))
        stock = int(input("stock:"))
        new_product = Product(kind,name,price,stock)

        print("Adding the new product. . .")
        time.sleep(2)
        supermarket.add_new_product(new_product)
        print("Completed")

    elif(selection == "3"):

        delete= input("What do you want to delete:")
        print("deleting...")
        time.sleep(2)
        supermarket.delete_product(delete)
        print("Deleted")

    elif(selection == "4"):

        stock=input("Which product do you want to edit the stock number?")
        amount=int(input("How many/much:"))
        print("Updating...")
        time.sleep(2)
        supermarket.update_stock(stock,amount)
        print("Updated...")

    elif (selection == "5"):

        name = input("Which product do you want to edit the price?")
        price = int(input("How many/much:"))
        print("Updating...")
        time.sleep(2)
        supermarket.update_price(name, price)
        print("Updated...")

    else:
        print("Invalid operation")
