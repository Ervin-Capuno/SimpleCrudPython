# VitalSignApp
> A simple Vital sign command line app.
> A simple CRUD System.

## Third Party Module
* sqlite
* tabulate

## Installation
- If Docker installed in a local computer:
1. open your command prompt/terminal.
2. type the command below:
    ```
        Docker run 
    ```

- If Docker is not installed in a local computer:
1. open the command prompt/terminal

2. locate your project directory assuming that the project directory is projectDirectory locate it and type:
    * Windows
        1. Creating a venv file:
            ```
            python -m venv C:\path\projectDirectory\venv
            ```

        2. Activating the virtual environment:
           ```
            C:\projectDirectory\venv\Scripts\activate
           ```
    * Linux
        1. Creating a venv file:
            ```
            python3 -m venv projectDirectory/venv
            ```
        2. Activating the virtual environment: 
           ```
           source projectDirectory/venv/bin/activate
           ```
            
    * MacOS
        1. Creating a venv file
             ```
             python3 -m venv projectDirectory/venv
             ```
        2. Activating the virtual environment:
           ```
           source projectDirectory/venv/bin/activate
           ```
3. Install the required module from the requuirements.txt type:
   ```
   pip3 install -r requirements.txt
   ```


## Scope
* The Database class have a methods of:
    * insert_data
    * show_tables
    * read_specific_data
    * read_data_all
    * sanitized_input
    * del_data
    * search_dta
    * __str__
    * __repr__


## Limitations
* This Database class is certain only in two tables which vitalSigns table and persons table, if you want to create another database for your program modify the Database class the create tables 
