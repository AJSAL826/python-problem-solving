import sqlalchemy as db
from sqlalchemy import Integer, String, Numeric, MetaData, Table, Column, ForeignKey

engine = db.create_engine('')
meta = MetaData()

courses = Table('courses', meta,
    Column("ID", Integer, primary_key=True),
    Column("course_names", String),
    Column("Count", Numeric)
)

loc = Table('loc', meta,
    Column("ID", Integer, primary_key=True),
    Column("places", String),
    Column("c_id", Integer, ForeignKey('courses.ID'))
)

meta.create_all(engine)
conn = engine.connect()
import sqlalchemy as db
from sqlalchemy import Integer, String, Numeric, MetaData, Table, Column, ForeignKey

engine = db.create_engine('')
meta = MetaData()

courses = Table('courses', meta,
    Column("ID", Integer, primary_key=True),
    Column("course_names", String),
    Column("Count", Numeric)
)

loc = Table('loc', meta,
    Column("ID", Integer, primary_key=True),
    Column("places", String),
    Column("c_id", Integer, ForeignKey('courses.ID'))
)

meta.create_all(engine)
conn = engine.connect()

# Insert data into the 'courses' table with matching IDs
conn.execute(courses.insert().values(course_names='cs', Count=120))
conn.execute(courses.insert().values(course_names='eee', Count=30))

# Insert data into the 'loc' table with corresponding 'c_id' values
conn.execute(loc.insert().values(places="ekm", c_id=1))
conn.execute(loc.insert().values(places="ekm", c_id=2))

# Commit the changes
conn.commit()

# Commit the changes
conn.commit()
