"""
dummy.py
Tests database record entry and removal

Created by Duncan Stothers in 2018 at Harvard University for Cabot Cafe
Licensed under MIT License
"""

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///drinks.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

### Adding (uncomment to add to database)
"""
user = User("chai_love_lucy")
session.add(user)

user = User("thin_mint")
session.add(user)

user = User("cookie")
session.add(user)
"""

### Removing (uncomment to get and remove from database)
"""
drink = session.query(User).get(1)
session.delete(drink)
"""

### Commit the record the database
session.commit()




