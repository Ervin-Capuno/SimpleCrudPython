import sqlite3

conn =sqlite3.connect('myData.db')

cursor = conn.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS persons(
    personId INT PRIMARY KEY,
    password VARCHAR(35),
    firstName VARCHAR(35),
    lastName VARCHAR(35),
    birthDay DATE,
    age INT,
    address VARCHAR(35),
    school VARCHAR(35)
)
"""
)


cursor.execute(
"""
CREATE TABLE IF NOT EXISTS vitalSigns(
    vitalSignID INT PRIMARY KEY,
    personId INT,
    weight INT,
    height INT, 
    BMI DOUBLE(5,2),
    FOREIGN KEY(personId) REFERENCES persons(personId)
)
"""
)

conn.commit()
conn.close()
