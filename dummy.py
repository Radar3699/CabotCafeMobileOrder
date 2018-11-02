import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///drinks.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

### Adding

user = User("chai_love_lucy")
session.add(user)

user = User("thin_mint")
session.add(user)

user = User("cookie")
session.add(user)


### Removing
"""
drink = session.query(User).get(1)
session.delete(drink)
"""



# commit the record the database
session.commit()

session.commit()



