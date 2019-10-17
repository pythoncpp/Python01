# import admin.faculty
#
# f_1 = admin.faculty.Faculty('faculty 1', 'subject 1')
# print(f_1)

# import admin.faculty as faculty
#
# f_2 = faculty.Faculty('faculty 2', 'subject 2')
# print(f_2)

# from admin.faculty import Faculty
#
# f_3 = Faculty('faculty 3', 'subject 3')
# print(f_3)


# from admin.faculty import Faculty as MyFaculty
#
# f_3 = MyFaculty('faculty 4', 'subject 4')
# print(f_3)

# import admin.account
# account_1 = admin.account.Account()
# account_1.print_balance()

# import admin.account as MyAccount
# account_2 = MyAccount.Account()
# account_2.print_balance()

# from admin.account import Account
# account_3 = Account()
# account_3.print_balance()

print("this is the first line to get executed")

from admin.account import Account as MyAccount
account_4 = MyAccount()
account_4.print_balance()