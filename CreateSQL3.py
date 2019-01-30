import sqlite3
conn = sqlite3.connect("Flights_Service.db")
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE Customer(
  cust_id INTEGER PRIMARY KEY,
  c_first_name TEXT NOT NULL,
  c_last_name TEXT NOT NULL,
  address TEXT NOT NULL,
  city TEXT NOT NULL,
  postal_code INTEGER,
  email TEXT NOT NULL,
  phone INTEGER NOT NULL)''')

  # Create table
c.execute('''CREATE TABLE Airplane(
  airplane_id INTEGER PRIMARY KEY,
  manufacturer TEXT NOT NULL,
  max_seats INTEGER NOT NULL,
  type TEXT NOT NULL
)
''')

# Create table
c.execute('''CREATE TABLE Seat(
  seat_number TEXT PRIMARY KEY,
  airplane_id reference INTEGER NOT NULL,
  FOREIGN KEY(airplane_id) REFERENCES Airplane(airplane_id)
)
''')

# Create table
c.execute('''CREATE TABLE Airport(
  airport_id INTEGER PRIMARY KEY,
  airport_name TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL
)
''')

# Create table
c.execute('''CREATE TABLE Customer_Seat(
  cust_id reference INTEGER NOT NULL,
  seat_number reference TEXT NOT NULL,
  FOREIGN KEY(seat_number) REFERENCES Seat(seat_number),
  FOREIGN KEY(cust_id) REFERENCES Customer(cust_id)
)
''')

# Create table
c.execute('''CREATE TABLE Airplane_Customer(
  airplane_id reference INTEGER NOT NULL,
  cust_id reference INTEGER NOT NULL,
  FOREIGN KEY(airplane_id) REFERENCES Airplane(airplane_id),
  FOREIGN KEY(cust_id) REFERENCES Customer(cust_id)
)
''')

# Create table
c.execute('''CREATE TABLE Airplane_Airport(
  scheduled_dep_time DATETIME,
  scheduled_arr_time DATETIME,
 airplane_id reference INTEGER NOT NULL,
 airport_id reference INTEGER NOT NULL,
  FOREIGN KEY(airplane_id) REFERENCES Airplane(airplane_id),
  FOREIGN KEY(airport_id) REFERENCES Airport(airport_id)
)
''')


# Insert a row of data
c.execute("INSERT INTO Customer VALUES (1,'Dolorita','Brumen','76347 Hauk Terrace','Liangdang Chengguanzhen','41234','dbrumen0@addthis.com','1756675012'),(2,'Zelma','Ridgeway','9 Oakridge Court','Nixi','43533','zridgeway1@freewebs.com','8649368785'),(3,'Joli','Moreinis','84297 Hoffman Plaza','Łaziska,Górne','43-173','jmoreinis2@dyndns.org','4304404875'),(4,'Giovanna','Herity','407 Alpine Way','Wucheng','43201','gherity3@google.pl','5138226457'),(5,'Boone','Vedyasov','08284 Miller Circle','Vakhsh','91902','bvedyasov4@nba.com','8189504854'),(6,'Felic','McCorley','55885 Portage Road','Baleal','2520-005','fmccorley5@cpanel.net','3881191092'),(7,'Juliette','Nichols','09 Killdeer Pass','Los Andes','526529','jnichols6@tuttocitta.it','1293561900'),(8,'Griff','Castagnier','59 Calypso Center','Kostarea Satu','43201','gcastagnier7@cbslocal.com','826265873'),(9,'Kimberlee','Southorn','05 International Road','Svirsk','665420','ksouthorn8@hostgator.com','4172758091'),(10,'Desirae','Gusticke','32704 Brentwood Center','Brusyanka','403567','dgusticke9@sina.com.cn','30462542908')")

c.execute("INSERT INTO Airplane VALUES(1, 'Airbus', 525, 'A380'),(2, 'Airbus', 520, 'A380'),(3, 'Airbus', 185, 'A320'),(4, 'Boeing', 300, '787'),(5, 'Boeing', 290, '787'),(6, 'Boeing', 416, '747'),(7, 'Airbus', 180, 'A320'),(8, 'Boeing', 400, '747') ,(9, 'Embraer', 100, '190'),(10, 'Embraer', 100, '190')")

c.execute("INSERT INTO Seat VALUES('1A',8),('1B',7),('1C',8),('1D',3),('1E',3),('1F',2),('2A',1),('2B',8),('2C',6),('2D',4)")

c.execute("INSERT INTO Customer_Seat VALUES(10,'1C'),(3,'2D'),(8,'2C'),(3,'1A'),(5,'1D'),(5,'1E'),(8,'1F'),(1,'2A'),(10,'2B'),(4,'1B')")


c.execute("INSERT INTO Airplane_Customer VALUES(8,1),(3,3),(7,2),(1,4),(9,5),(10,6),(1,7),(2,8),(6,9),(2,10)")


c.execute("INSERT INTO Airport VALUES(1,'Aberdeen Regional Airport','Aberdeen','South Dakota'),(2,'Floyd Bennett Memorial Airport','Glens Falls','New York'),(3,'Columbus Municipal Airport','Columbus','Ohio'),(4,'Gaylord Regional Airport','Gaylord','Michican'),(5,'Grand Canyon National Park Airport','Grand Canyon','Arizona'),(6,'Hobby Airport','Houston','Texas'),(7,'Key West International Airport','Key West','Florida'),(8,'Orcas Island Airport','Eastsound','Washington')")


c.execute("INSERT INTO  Airplane_Airport VALUES('2019-01-25 10:00:00','2019-01-25 12:00:00',1,1),('2019-01-25 08:00:00','2019-01-25 12:00:00',2,8),('2019-01-25 07:00:00','2019-01-25 12:00:00',3,6),('2019-01-25 10:00:00','2019-01-25 12:00:00',3,5),('2019-01-25 10:00:00','2019-01-25 12:00:00',4,4),('2019-01-25 10:00:00','2019-01-25 12:00:00',5,6),('2019-01-25 10:00:00','2019-01-25 12:00:00',6,7),('2019-01-25 10:00:00','2019-01-25 12:00:00',7,3),('2019-01-25 10:00:00','2019-01-25 12:00:00',8,2),('2019-01-25 10:00:00','2019-01-25 12:00:00',9,8),('2019-01-25 10:00:00','2019-01-25 12:00:00',10,6)")


conn.commit()
conn.close()
