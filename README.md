# Project Description
Components: 
- PostGres DB, 
- Webscraper which scrapes the first page from ```https://www.athome.de/en/``` and provides the data to the Python-Server
- Python-Server which processes the data and creates, updates, reads and delete relations in PostGres DB.

The two docker-container (PostGres DB and Python-Server) communicate via the ```docker-compose.yml``` file. Use ```docker-compose up --build``` to run the application. 
The Pyhton-Server will process the data which is in Folder```apartment_data```, upload it into the DB. Afterwards it will read the DB Apartment Relation, and print the records on terminal.
