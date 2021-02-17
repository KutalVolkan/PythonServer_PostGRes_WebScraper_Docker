#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from os import listdir
import json   

    
 # declare connection instance
db_name = 'postgres'
db_user = 'postgres'
db_pass = 'postgres'
db_host = 'pgdb'
db_port = '5432'

db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string, echo=True)
Base = declarative_base()


class Apartment(Base):
    __tablename__ = 'apartments'

    id_nr = Column(Integer, primary_key=True)
    sales_price = Column(String)
    livable_surface = Column(String)
    number_of_rooms = Column(String)
    location = Column(String)


# examines the schema that we implicitly created by declaring the Apartment class, and sends a CREATE TABLE command to our database.
Session = sessionmaker(db)  
session = Session()
Base.metadata.create_all(db)

# adding into apartment table 
def create_apartment_table(id_nr, sales_price, livable_surface, number_of_rooms, location):
    apartment = Apartment(id_nr = id_nr, sales_price = sales_price, livable_surface = livable_surface, number_of_rooms = number_of_rooms, location = location)
    session.add(apartment)
    session.commit()


# read
def read_apartmens():
    apartments = session.query(Apartment)  
    for apartment in apartments:
        print(f'id_nr: {apartment.id_nr}')
        print(f'sales price: {apartment.sales_price}')
        print(f'livable_surface: {apartment.livable_surface}')
        print(f'number_of_rooms: {apartment.number_of_rooms}')
        print(f'location: {apartment.location}')
        print("-------------------------")

# Update
def update_apartment(id_nr, new_sales_price):
    # Fetch apartments with id_nr
    apartment = session.query(Apartment).filter_by(id_nr= id_nr).all()
    apartment[0].sales_price = new_sales_price  
    session.commit()

# Delete
def delete_apartment(id_nr):
    # Fetch apartments with id_nr
    apartment = session.query(Apartment).filter_by(id_nr= id_nr).all()
    session.delete(apartment[0])
    session.commit()  


def delete_all_apartments():
    # Fetch apartments with id_nr
    apartments = session.query(Apartment)
    for apartment in apartments:
        session.delete(apartment)
        session.commit()  


def creating_records():
    id_nr = 0
    for apartment_no in json_files:
        with open(f'{path}/{apartment_no}') as f:
            data = json.loads(f.read()) 
            sales_price = data['Sale_price']
            livable_surface = data['Livable_surface']
            number_of_rooms = data['Number_of_rooms']
            location = data['Location']
            create_apartment_table(id_nr, sales_price, livable_surface, number_of_rooms, location)
            id_nr = id_nr + 1


# test for update and delete
def some_tests():
    read_apartmens()
    update_apartment(0, 200)
    read_apartmens()
    delete_apartment(0)
    read_apartmens()

# finding json files in givin path 
def find_json_filenames(path_to_dir, suffix=".json" ):
    filenames = listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]

if __name__ == '__main__':
    print('Application started')
    path = "./apartment_data/"
    json_files = find_json_filenames(path)
    
    
    # creating records with scraped data
    creating_records()
    # reading from db and printing into terminal
    read_apartmens()
    print("Application finished")

