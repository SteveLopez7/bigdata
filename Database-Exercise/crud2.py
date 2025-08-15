import os
from database import con, cursor
#CREATE
def create_user ():
    os.system('clear')
    fname = input('Enter you firstname: ')
    lname = input('Enter your lastname: ')
    ide_num = input ('Enter your ident_number: ') 
    email = input ('Enter your email: ')

    new_data = f''' INSERT INTO users (firstname, lastname, ide_number, email) 
    VALUES ('{fname}','{lname}','{ide_num}','{email}')'''

    con.execute(new_data)
    con.commit()
    print(':::User has been created sucessfully:::')

# create_user()

#Read

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
    print(data)
list_users()    

