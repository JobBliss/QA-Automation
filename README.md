# QA Automation Command Center

*We are Velocity Inc. , we use Automation Command Center.*


## Installation

clone:
```
$ git 
$ cd qaCommandCenter
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
init database then run:
```
$ flask initdb
$ flask run

Aleternatively:
$ python -m flask initdb
$ python -m flask run
* Running on http://127.0.0.1:5000/
```

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
