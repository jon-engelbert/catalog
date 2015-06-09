from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Category, Base, MenuItem, User
from project import app
from flask.ext.sqlalchemy import SQLAlchemy
from database_setup import  create_app, create_db


# engine = create_engine('postgres://swyopjstoplhpj:mldH715JMJHFKdZaIpfJuesXiA@ec2-184-73-221-47.compute-1.amazonaws.com:5432/dblg34ae505inc')
# engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
# Base.metadata.bind = engine
 
# DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
# session = DBSession()


app = create_app()
Session = create_db(app)
session = Session()

session.query(MenuItem).delete()
session.query(Category).delete()
session.query(User).delete()
# MenuItem.__table__.drop(self._engine)
# Category.__table__.drop(engine)
# User.__table__.drop(engine)

session.close()

#Create dummy user
User1 = User(name="Tiny Tim", email="tiny_time@little.com", picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

#Menu for UrbanBurger
category1 = Category(user_id=1, name = "Magic The Gathering")

session.add(category1)
session.commit()

card0 = MenuItem(user_id=1, name = "Bob the slayer", description = "Juicy grilled veggie patty with tomato mayo and lettuce", price = "$7.50",  category = category1, imagefile = "")

session.add(card0)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Lady killer", description = "a big hunk", price = "$2.99",  category = category1, imagefile = "")

session.add(menuItem1)
session.commit()




#Menu for Super Stir Fry
category2 = Category(user_id=1, name = "Pokemon")

session.add(category2)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Chicken dance dude", description = "dances you to death", price = "$7.99",  category = category2, imagefile = "")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "killer Duck", description = " watch out for his duck duck goose attack ", price = "$25", category = category2, imagefile = "")

session.add(menuItem2)
session.commit()







print "added menu items!"
