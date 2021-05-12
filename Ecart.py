import mysql.connector as sql
import sys
from datetime import datetime

def adminRegistration():
    print("*********************")
    f_name=input("First Name:")
    l_name=input("Last Name:")
    contact=input("Contact No.")
    address=input("Address:")
    email=input("Emailid")
    userid=input("userid(unique)")
    password=input("password:")
    print("*********************")
    val=(f_name,l_name,contact,address,email,userid,password)
    sql="insert into admin_registration values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,val)
    val=(userid,password)
    sql="insert into login values(%s,%s)"
    cur.execute(sql,val)
    conn.commit()
    print("data committed")
    
    

def userRegistration():
    print("*********************")
    f_name=input("First Name:")
    l_name=input("Last Name:")
    contact=input("Contact No.")
    address=input("Address:")
    email=input("Emailid")
    userid=input("userid(unique)")
    password=input("password:")
    print("*********************")
    val=(f_name,l_name,contact,address,email,userid,password)
    sql="insert into user_registration values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,val)
    val=(userid,password)
    sql="insert into login values(%s,%s)"
    cur.execute(sql,val)
    conn.commit()
    print("data committed")
    

def adminPanel():
    print("*********************")
    print("1.Add Item")
    print("2.Delete item")
    print("3.Total sale")
    print("4.Customers Details")
    print("5.Product summary")
    print("6.Logout")
    print("7.for exit")
    print("*********************")
    
                       
def addItem():
    prodid=input("Enter product ID:")
    prodname=input("Enter product name:")
    brand=input("Enter Brand name:")
    category=input("Enter category:")
    price=input("Enter Price:")
    sql="insert into product values(%s,%s,%s,%s,%s)"
    val=(prodid,prodname,brand,category,price)
    cur.execute(sql,val)
    conn.commit()
    print("Item added")
    adminPanel()
def deleteItem():
    prodid=input("Enter productid whose value is to deleted:")
    cur.execute("delete from product where productid=%s",(prodid,))
    conn.commit()
    print("item deleted")
    adminPanel()
def totalSale():
    cur.execute("select * from order_detail")
    row=cur.fetchall()
    for r in row:
        print(r)
def custDetails():
    cur.execute("select * from user_registration")
    row=cur.fetchall()
    for r in row:
        print(r)
def productSummary():
    cur.execute("select * from product")
    row=cur.fetchall()
    for r in row:
        print(r)
def adminDisplay():
    cur.execute("select * from admin_registration")
    row=cur.fetchall()
    for r in row:
        print(r)
def logout():
    login()

    

def adminChoice():
    choice=int(input("Please enter admin choice : "))
    if choice==1:
        addItem()
        print("\n***************************************************\n")
        productSummary()
        print("Item added")
        print("\n***************************************************\n")
        adminChoice()
    elif choice==2:
        deleteItem()
        print("\n***************************************************\n")
        productSummary()
        print("Item deleted")
        print("\n***************************************************\n")
        adminChoice()
    elif choice==3:
        totalSale()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==4:
        custDetails()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==5:
        productSummary()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==6:
        logout()
    elif choice==7:
        sys.exit()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n***************************************************\n")
        adminPanel()
        print("\n***************************************************\n")
        adminChoice()


    


def userPanel():
    print("*********************\n")
    print("1.Items")
    print("2.Profile")
    print("3:My Orders")
    print("4.Place Order")
    print("5.Logout")
    print("6.for exit")
    print("\n*********************")
def item():
    cur.execute("select * from product")
    row=cur.fetchall()
    for r in row:
        print(r)

def profile():
    userid=input("Enter userid")
    cur.execute("select * from user_registration whwere userid=%s",(userid,))
    row=cur.fetchall()
    for r in row:
        print(r)
def order():
    print("choose from our product to order fill your input correctly")
    cur.execute("select * from product")
    row=cur.fetchall()
    for r in row:
        print(r)
    productid=input("Enter correct product id")
    quantity=input("Enter quantity")
    orderid="o"+productid[1:]
    status="ordered"
    userid=input("Enter youe correct userid")
    date=datetime.now()
    val=(orderid,userid,productid,quantity,status,date)
    sql="insert into order_detail values(%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,val)
    conn.commit()
    print("order placed")

def myOrder():
    userid=input("Enter yor userid")
    cur.execute("select * from order_detail where userid=%s",(userid,))
    row=cur.fetchall()
    for r in row:
        print(r)
    

def userChoice():
    choice=int(input("Please enter user choice : "))
    if choice==1:
        item()
        print("\n***************************************************\n")
        userPanel()
        print("\n***************************************************\n")
        userChoice()
    elif choice==2:
        profile()
        print("\n***************************************************\n")
        userPanel()
        print("\n***************************************************\n")
        userChoice()
    elif choice==3:
        myOrder()
        print("\n***************************************************\n")
        userPanel()
        print("\n***************************************************\n")
        userChoice()
    elif choice==4:
        order()
        print("\n***************************************************\n")
        userPanel()
        print("\n***************************************************\n")
        userChoice()
    elif choice==5:
        logout()
    elif choice==6:
        sys.exit()
    else:
        print("Invalid Choice. Please enter valid choice")
            

def login():
    tp=input("Admin/User [A/U] : ")
    if tp=='A' or tp=='a' :
        def admin():
            userid=input("Enter userid")
            password=input("Enter the password : ")
            val=(userid,password)
            sql="select userid from login where  userid=%s and password=%s"
            cur.execute(sql,val)
            row_no=cur.fetchall()
            if len(row_no)==1:
                adminPanel()
                adminChoice()    
            else:
                print("Invalid incredencials")
                admin()
        admin()

    elif tp=='U' or tp=='u':
        def user():
            userid=input("Enter userid")
            password=input("Enter the password : ")
            val=(userid,password)
            sql="select userid from login where  userid=%s and password=%s"
            cur.execute(sql,val)
            row_no=cur.fetchall()
            if len(row_no)==1:
                userPanel()
                userChoice()    
            else:
                print("Invalid incredencials")
                user()
        user()
    else:
        print("Invalid user type. Enter valid user type")

def Ecart():
    print("1.Registation")
    print("2.Login")
    n=input("Enter 1 for registation and 2 for login:")
    if n=="1":
        def registration():
            m=input("Enter 1 for admin registation and 2 for user registration:")
            if m=='1':
                adminRegistration()
            elif m=='2':
                userRegistration()
            else:
                print("wrong choice")
                registration()
        registration()
    elif n=="2":
        login()
    else:
        print("wrong Input")
        Ecart()

try:
    conn=sql.connect(host = "localhost",user="root",passwd="abc123",database = "my_table")
    cur=conn.cursor()
except:
    print("Error in connecting to db")
else:
    print("Database connected")
    Ecart()
finally:
    cur.close()
    conn.close()
    print("connection closed")
    
    


        




