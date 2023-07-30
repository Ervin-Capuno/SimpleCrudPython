# SimpleCrudPython


## Third Party Module
* sqlite
* tabulate

## Installation
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
* The Database class don't have a create table method.
