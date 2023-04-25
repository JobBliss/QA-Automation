import time
import logging
import CreateCompany
import LoginToJobbliss
import emailLogin
import CompanyProfileCreationPackage

logging.basicConfig(filename='mainLog.txt', level=logging.DEBUG, format="%(asctime)s %(message)s", filemode='w')
CreateCompany.jobblissCreateCompany()
print('Company Created Successfully!')
time.sleep(10)
emailLogin.emailLogin()
print('Email Checked Successfully!')
time.sleep(10)
LoginToJobbliss.jobblissLogin()
print('Company Logged In Successfully!')
time.sleep(10)
CompanyProfileCreationPackage.jobblissCompleteCompanySetup()
print('Company Package Successfully!')

#Trigger The other Workflows.
