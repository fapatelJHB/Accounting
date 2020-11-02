from __init__ import *
from user.authentication import authenticate_user
from transactions.journal import receive_income , pay_expense
# import banking.reconciliation as bank
import banking
# import banking.ubsa.reconciliation as ubsa
import sys
# import banking.online.reconciliation as online

amount = 100

# def receive_income(amount):
#    print("[Journal] Received R{}".format(amount))

# def pay_expense(amount):
#     print("[Journal] Paid R{}".format(amount))


if __name__ == "__main__":
    if (len(sys.argv)>0):
        for i in sys.argv[1:]:
            print (i)
    
    authenticate_user()
    receive_income(amount)
    pay_expense(amount)
    # bank.do_reconciliation()
    banking.do_reconciliation()
    # ubsa.do_reconciliation()
    # online.do_reconciliation()