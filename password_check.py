def password_entry():
    pass_req = 3
    password_good = False
    while password_good == False:
        pass_stren = 0
        print('Password must be 8 characters and include 3 of the following: ')
        print('A number, lowercase letter, uppercase letter, a special character.')
        pass_at = (input('Please enter a password: '))
        if any(a.isupper() for a in pass_at):
            print('TEST UPPER')
            pass_stren += 1
        if any(a.islower() for a in pass_at):
            print('test lower')
            pass_stren += 1
        if any(a.isdigit() for a in pass_at):
            print('test 123')
            pass_stren += 1
        if any(not a.isalnum() for a in pass_at):
            print('test @^$*')
            pass_stren += 1
        if pass_stren >= pass_req and len(pass_at) >= 8:
            password_good = True
            print('Password strength:', pass_stren, '\nPassword accepted! \n')
        else:
            print('Password strength:', pass_stren, '\nPassword is too weak. \n')

   
        
        


    




password_entry()

        
