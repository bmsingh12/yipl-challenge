# yipl-intern-petroleum-report
This repository contains the source code for the YIPL intern coding challenge.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
* Python : version 3
* Pandas Library
* MySql: 8.0

### Installation

```
$ git clone https://github.com/<username>/yipl-challenge.git
$ cd yipl_challenge
```

### Creating Virtual Environment
To create a virtual environment, go to your project's directory and run virtualenv.

#### On macOS and Linux:
```
python3 -m virtualenv venv
```
#### On windows:
```
py -m virtualenv venv
```
Note : The second argument is the location to create the virtualenv. Generally, you can just create this in your project and call it venv. [ virtualenv will create a virtual Python installation in the venv folder.]

### Activating Virtual Environment
Before you can start installing or using packages in your virtualenv, you'll need to activate it.

#### On macOS and Linux:
```
source venv/bin/activate
```
#### On windows:
```
.\venv\Scripts\activate
```

### Confirming virtualenv by checking location
#### On macOS and Linux:
```
which python
```
Output : .../venv/bin/python

#### On windows:
```
where python
```
Output : .../venv/bin/python.exe

### Installing required packages with pip
For installing mysql connector:
```
pip3 install mysql-connector-python
```
For installing pandas library:
```
pip install pandas
```
### Creating the MySQL table 
Run the following query to create the sql table:
```
create table yipl.challenge (
    year bigint,
    petroleumProduct varchar(30),
    sale bigint
)
```
In the driver code, set the respective fields:
* host
* user
* password
* database name
##### Example for local environment:
* host=localhost
* user=root
* password=password
* database= yipl

### Running the App
Get inside the project directory and enter the following command line code at terminal for Linux/MacOS or command prompt for Windows.
```
python report.py
```
