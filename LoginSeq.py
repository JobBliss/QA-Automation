import time

import LoginToJobbliss
import ManagerLogin
import ContractorLogin
import logging


logging.basicConfig(filename='LoginSeq_Log.txt', level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode='w')

ContractorLogin.jobblissLogin()
time.sleep(5)
ManagerLogin.jobblissLogin()
time.sleep(5)
LoginToJobbliss.jobblissLogin()

print("Login successful for all user types")
