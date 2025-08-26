import os
from database import con, cursor

#----------------------------------------------
# CREATE USER
#----------------------------------------------
def create_user():
    os.system('clear')
    fname = input('Enter your firstname: ')
    lname = input('Enter your lastname: ')
    ide_num = input('Enter your ident_number: ')
    email = input('Enter your email: ')

    # (TALLER - Punto 1: Verificar si existe usuario con ide_number o email)
    check_query = f'''SELECT * FROM users 
                      WHERE ide_number = '{ide_num}' OR email = '{email}' '''
    cursor.execute(check_query)
    existing = cursor.fetchone()
    if existing:
        print("::: User with this ident_number or email already exists :::")
        return

    new_data = f''' INSERT INTO users (firstname, lastname, ide_number, email) 
    VALUES ('{fname}','{lname}','{ide_num}','{email}')'''

    con.execute(new_data)
    con.commit()
    print('::: User has been created successfully :::')


#----------------------------------------------
# LIST USERS
#----------------------------------------------
def list_users():
    os.system('clear')
    users_data_query = ''' 
            select 
                id,
                firstname,
                lastname,
                ide_number,
                email,
                case when status = 1 then 'Active' else 'Inactive' end as status 
            from
                users    
    '''
    cursor.execute(users_data_query)
    data = cursor.fetchall()

    # (TALLER - Punto 2: Mostrar usuarios en formato tabla)
    print("\n{:<5} {:<12} {:<12} {:<12} {:<25} {:<10}".format(
        "ID", "Firstname", "Lastname", "ID_Number", "Email", "Status"))
    print("-"*80)
    for row in data:
        print("{:<5} {:<12} {:<12} {:<12} {:<25} {:<10}".format(*row))


#----------------------------------------------
# LIST ACTIVE USERS (TALLER - Punto 3)
#----------------------------------------------
def list_active_users():
    cursor.execute("SELECT id, firstname, lastname, ide_number, email FROM users WHERE status = 1")
    data = cursor.fetchall()
    print("\n::: Active Users :::")
    for row in data:
        print(row)


#----------------------------------------------
# LIST INACTIVE USERS (TALLER - Punto 4)
#----------------------------------------------
def list_inactive_users():
    cursor.execute("SELECT id, firstname, lastname, ide_number, email FROM users WHERE status = 0")
    data = cursor.fetchall()
    print("\n::: Inactive Users :::")
    for row in data:
        print(row)


#----------------------------------------------
# UPDATE USER (TALLER - Punto 5)
#----------------------------------------------
def update_user():
    user_id = input("Enter user ID to update: ")
    new_email = input("Enter new email: ")
    new_status = input("Enter new status (1=Active, 0=Inactive): ")

    query = f"UPDATE users SET email='{new_email}', status={new_status} WHERE id={user_id}"
    con.execute(query)
    con.commit()
    print("::: User updated successfully :::")


#----------------------------------------------
# DELETE USER (TALLER - Punto 6)
#----------------------------------------------
def delete_user():
    user_id = input("Enter user ID to delete: ")
    query = f"DELETE FROM users WHERE id={user_id}"
    con.execute(query)
    con.commit()
    print("::: User deleted successfully :::")


#----------------------------------------------
# SEARCH USER (TALLER - Punto 7)
#----------------------------------------------
def search_user():
    ide_num = input("Enter ident_number to search: ")
    cursor.execute(f"SELECT * FROM users WHERE ide_number = '{ide_num}'")
    data = cursor.fetchone()
    if data:
        print("::: User found :::")
        print(data)
    else:
        print("::: User not found :::")


#----------------------------------------------
# MAIN MENU (TALLER - Punto 1 al 8)
#----------------------------------------------
def main_menu():
    while True:
        print("\nMain Menu:")
        print("[1]. Create new user")
        print("[2]. List all users")
        print("[3]. List active users")
        print("[4]. List inactive users")
        print("[5]. Update user")
        print("[6]. Delete user")
        print("[7]. Search user")
        print("[8]. Exit")

        try:
            opt = int(input("Press any option: "))
        except ValueError:
            print("::: Invalid input, only numbers allowed :::")
            continue

        # (TALLER - Validar opciones 1 a 8)
        if opt < 1 or opt > 8:
            print("::: Error, please choose between 1 and 8 :::")
            continue

        if opt == 1:
            create_user()
        elif opt == 2:
            list_users()
        elif opt == 3:
            list_active_users()
        elif opt == 4:
            list_inactive_users()
        elif opt == 5:
            update_user()
        elif opt == 6:
            delete_user()
        elif opt == 7:
            search_user()
        elif opt == 8:
            print("::: Exiting program :::")
            break


#----------------------------------------------
# Ejecutar menú principal
#----------------------------------------------
if __name__ == "__main__":
    main_menu()
