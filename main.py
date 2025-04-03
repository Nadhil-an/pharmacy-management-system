import sqlite3

# ====================Connect Database And Create Table ==================

def database_connection():
    conn = sqlite3.connect('pms.db')
    c=conn.cursor()
        #   table name
    c.execute("""  
              CREATE TABLE IF NOT EXISTS PMSDATA (id INTEGER PRIMARY KEY AUTOINCREMENT,
              Name TEXT,
              Manufacture TEXT,
              Price INTEGER,
              Stock INTEGER,
              Expiry_date TEXT)
              """)
    conn.commit()
    return conn,c

# ========================Add Medicine To Database=======================
def add_medicine(conn,c):
      while True:
          print("1.Start adding")
          print("2. Exit to Main Menu")
          process=input("Add or Exit:")
          if process == "1":
              name = input("Enter the medicine name:")
              manufacture = input("Enter the Manufacture details :")
              price = int(input("Enter the Price:"))
              stock = int(input("Enter the stock :"))
              expiry = input("Enter the Expiry Date: ")
              c.execute('INSERT INTO PMSDATA (Name,Manufacture,Price,Stock,Expiry_date) VALUES (?,?,?,?,?)',(name,manufacture,price,stock,expiry))
              conn.commit()  
              print("Medicine Added Successfully!")
          elif process == "2":
             print("Returning to main menu...")
             break
          else:
            print("Invalid choice. Please enter 1 or 2.")
              

# ==================== Update Medicine Details======================
def update_medicine(conn,c):
    try:
        medicine_id = int(input("Enter the medicine id :"))
    except ValueError:
        print("Invalid input! Medicine ID must be a number.")
        return
    c.execute("SELECT * FROM PMSDATA WHERE id=?",(medicine_id,))
    medicine = c.fetchone()
    if not medicine:
        print("Invalid id")
        return
    print(" Current Medicine Details")
    print("="*50)
    print(f"id |Name | Manufacture | Price | Stock | Expiry  ")
    print("-"*50)
    print(f"{medicine[0]} | {medicine[1]} | {medicine[2]} | {medicine[3]} | {medicine[4]} | {medicine[5]}")

    print("\nWhich detail do you want to update?")
    print("1. Name")
    print("2. Manufacturer")
    print("3. Price")
    print("4. Stock")
    print("5. Expiry Date")
    field_choice = input("Enter your choice: ")

    if field_choice == '1':
        uname = input("Enter new name:")
        c.execute("UPDATE PMSDATA SET Name=? WHERE id=?",(uname,medicine_id))
    elif field_choice == '2':
        umanufacture =input("Enter new manufacture:")
        c.execute("UPDATE PMSDATA SET Manufacture=? WHERE id=?",(umanufacture,medicine_id))
    elif field_choice =='3':
        try:
            uprice = int(input("Enter new price :"))
        except ValueError:
             print("Invalid input! Price must be a number.")
             return
        c.execute("UPDATE PMSDATA SET Price=? WHERE id=?",(uprice,medicine_id))
    elif field_choice == '4':
        try:
            ustock = int(input("Enter new stock:"))
        except ValueError:
            print("Invalid input! Stock must be a number.")
            return
        c.execute("UPDATE PMSDATA SET Stock=? WHERE id=?",(ustock,medicine_id))
    elif field_choice =='5':
        uexpiry = input("Enter new expiry :")
        c.execute("UPDATE PMSDATA SET Expiry_date=? WHERE id=?",(uexpiry,medicine_id))
    else:
        print("Invalid choice")
        return
    
    conn.commit()
    print("Successfully updated")


#  ============  show medicine =============================
def show_medicine(c):
    c.execute("SELECT * FROM PMSDATA")
    medicinedata = c.fetchall()

    if not medicinedata:
        print("Database is empty")
        return
    
    print(" Medicines ")
    print("-"*70)
    print(f"{'ID':<5} | {'Name':<15} | {'Manufacture':<15} | {'Price': <15} | {'Stock' :<15} | {'Expire':<15}")
    print("="*70)
    for data in medicinedata:
        print(f"{data[0]:<5} | {data[1]:<15} | {data[2]:<15} | {data[3]:<15} | {data[4]:<15} | {data[5]:<15}")


# ========================== Search Medicine ==================================
def search_medicine(c):
    print("\n Search Medicine BY:")
    print("="*68)
    print("1.Name")
    print("2.Manufacture")
    print("3.Price")
    print("4.Stock")
    print("5.Expiry Date")
    
    search = (input("Enter you choice :"))
    
    if search == '1':
        sname = input("Enter The Medicine Name:")
        c.execute("SELECT * FROM PMSDATA WHERE Name LIKE ?",('%'+sname+'%',))
    elif search == '2':
        smanufacture = input("Enter The Manufacture Name:")
        c.execute("SELECT * FROM PMSDATA WHERE Manufacture LIKE ?",('%'+smanufacture+'%'))
    elif search == '3':
        try:
            sminprice = int(input("Enter The Mininum Price:"))
            smaxprice = int(input("Enter The Maximum Price:"))
        except ValueError:
            print("Type numbers")
        c.execute("SELECT * FROM PMSDATA WHERE Price BETWEEN ? AND ?",(sminprice,smaxprice)) 
    elif search == '4':
        try:
         sstock = int(input("Enter the stock limit:"))
        except ValueError:
            print("Enter number only")
        c.execute("SELECT * FROM PMSDATA WHERE Stock <=?",(sstock,))
    elif search == '5':
        sexpiry = input("Enter the last expire date:")
        c.execute("SELECT * FROM PMSDATA WHERE Expiry_date <= ?",(sexpiry,))
    else:
        print("Invalid choice")
        return
    
    medicinesearch = c.fetchall()

    if not medicinesearch:
        print("Not found!")
        return
    print(f"ID  Name  |  Manufacture   |  Price |  Stock  | Expiry Date")
    for med in medicinesearch:
        print("-"*67)
        print(f"{med[0]:<5} | {med[1]:<15} | {med[2]:<15} | {med[3]:<15} | {med[4]:<15} | {med[5]:<15}")
    
    print("Search Completed")

# ======================= Drop Medicine Details =========================

def drop_medicine(conn,c):
    show_medicine(c)
    try:
        dropingid = int(input("Enter the id:"))
    except ValueError:
        print("Enter id number")
    
    c.execute("SELECT * FROM PMSDATA WHERE id=?",(dropingid,))
    dropingcol=c.fetchone()

    if not dropingcol:
        print("Id not found")

    c.execute("DELETE FROM PMSDATA WHERE id=?",(dropingid,))
    conn.commit()

    print(f"{dropingid} Deleted")





conn,c = database_connection()

# ====================== Main Interface Of PMS =============================
while True:
    print("===================Pharmacy Managment System================")
    print("1. Show All Medicines")
    print("2. Add New Medicine")
    print("3. Update Medicine Details")
    print("4. Search Medicine")
    print("5. Delete Medicine")
    print("6. Exit")
    print("======================================")
    choice = input("Enter your choice:")

    if choice == "1":
        show_medicine(c) 
    elif choice == "2":
        add_medicine(conn,c)
    elif choice == "3":
        update_medicine(conn,c)
    elif choice == "4":
        search_medicine(c)
    elif choice == "5":
        drop_medicine(conn,c)
    elif choice == "6":
        print("Exit ")
        break
    else:
        print("Sorry !..(Invalid choice)")

