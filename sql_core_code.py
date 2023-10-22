import sqlalchemy as db
from sqlalchemy import Integer, String, MetaData, Numeric, Table, Column, ForeignKey

# Establish a database connection
engine = db.create_engine('postgresql://postdb:postdb616@localhost:5432/btech')
meta = MetaData()

# Create the 'courses' table with 'ID' as the primary key
courses = Table('courses', meta,
    Column("ID", Integer, primary_key=True),
    Column("course_names", String),
    Column("Count", Numeric)
)

# Create the 'loc' table with 'ID' as the primary key and 'c_id' as the foreign key
loc = Table('loc', meta,
    Column("ID", Integer, primary_key=True),
    Column("places", String),
    Column("c_id", Integer, ForeignKey('courses.ID'))  # Establish a foreign key relationship
)

# Connect engine objects to the table object
meta.create_all(engine)

# Insert values into the 'courses' table
ins1 = courses.insert().values(course_names='eee', Count=120)
ins2 = courses.insert().values(course_names='ec', Count=40)
ins3 = courses.insert().values(course_names='mech', Count=90)

# Insert values into the 'loc' table, referencing courses with the 'c_id' foreign key
ins4 = loc.insert().values(places='ekm', c_id=1)
ins5 = loc.insert().values(places='kottayam', c_id=2)
ins6 = loc.insert().values(places='aluva', c_id=3)
ins7 = loc.insert().values(places='kochi', c_id=4)

# Connect to the database and execute the insert statements
conn = engine.connect()
conn.execute(ins1)
conn.execute(ins2)
conn.execute(ins3)
conn.execute(ins4)
conn.execute(ins5)
conn.execute(ins6)
conn.execute(ins7)

# Commit the changes
conn.close()
