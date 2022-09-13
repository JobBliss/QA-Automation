# QA-Automation
Automation of some of our test cases

Check out the requirements file to see the dependencies of the files to run.
To generate the requirements.txt file you can always use the following command:

pip3 freeze > requirements.txt

--------------------------------------------------

## Running the scripts

**Scripts contained:**
Uploading Documents Script : - it will login and then move to the documents pane and then uplaod a document as per the test case requirement. 

_py uploadDocument.py_

**The log should show that the document was uploaded successsfully.**

Loginto Jobliss:-
1. As a manager - _py ManagerLogin.py_
2. As a contractor - _py ContractorLogin.py_
3. As a company/admin - _py LoginToJobbliss.py_

**Creating a company account:-**
_CreateCompany.py_

**Invite Manager:**

A Company is the only entity that can invite a Manager:

_py InviteManager.py_

