import sqlalchemy as db
from sqlalchemy import Integer, String, MetaData, Numeric, Table, Column, ForeignKey

# Establish a database connection
engine = db.create_engine('postgresql://postdb:postdb616@localhost:5432/btech')
meta = MetaData()

# Create the 'courses' table with 'ID' as the primary key
courses = Table('courses', meta,
    Column("ID", Integer, primary_key=True),
    Column("course_names", String),
    Column("counts", Numeric)
)

# Create the 'loc' table with 'ID' as the primary key and 'c_id' as the foreign key
loc = Table('loc', meta,
    Column("ID", Integer, primary_key=True),
    Column("places", String),
    Column("c_id", Integer, ForeignKey('courses.ID'))
)

# Connect engine objects to the table object
meta.create_all(engine)

# Insert values into the 'courses' table
conn = engine.connect()
conn.execute(courses.insert().values(course_names="cs", counts=84))
conn.execute(courses.insert().values(course_names="eee", counts=34))

# Insert values into the 'loc' table, referencing courses with the 'c_id' foreign key
conn.execute(loc.insert().values(places="ekm", c_id=1))
conn.execute(loc.insert().values(places="ekm", c_id=2))
conn.commit()
# Commit the changes