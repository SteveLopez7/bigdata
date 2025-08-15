import os
from database import con, cursor
#CREATE
def create_user ():
    os.system('clear')
    new_data = '''
    INSERT INTO users (firstname, lastname, ide_number, email) 
    VALUES ('Stev','Lope','1235','steve1@gmail.com'); '''

    con.execute(new_data)
    con.commit()
    print(':::User has been created sucessfully:::')

create_user()        

#READ
