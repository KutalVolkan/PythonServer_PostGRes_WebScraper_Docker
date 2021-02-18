# Project Description
Components: 
- PostGres DB, 
- Webscraper which scrapes the first page from ```https://www.athome.de/en/``` and provides the data to the Python-Server
- Python-Server which processes the data and creates, updates, reads and delete relations in PostGres DB.

The two docker-container (PostGres DB and Python-Server) communicate via the ```docker-compose.yml``` file. Use ```docker-compose up --build``` to run the application. 
The Pyhton-Server will process the data which is in Folder```apartment_data```, upload it into the DB. Afterwards it will read the DB Apartment Relation, and print the records on terminal.

## Showing Records In PostGres DB Using GitBash
Open a new Terminal and run ```docker ps``` to list all containers in particular to see if container pgdb exists. Afterwards run ```winpty docker exec -it pgdb bash```. 
You should come into root mode and run ```winpty docker exec -it pgdb bash```. To list all relations run ```\d```. 
You should see an apartments table, afterwards run ```\c``` to connect to database "postgres" as user "postgres". To list all apartments you uploaded just run ```Select* From apartments;``` and you will see something like this: 
![](images/db_records.png)
