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

menuItem2 = MenuItem(user_id=1, name = "Veggie Burger", description = "Juicy grilled veggie patty with tomato mayo and lettuce", price = "$7.50",  category = category1, imagefile = "")

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "French Fries", description = "with garlic and parmesan", price = "$2.99",  category = category1, imagefile = "")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Chicken Burger", description = "Juicy grilled chicken patty with tomato mayo and lettuce", price = "$5.50", category = category1, imagefile = "")

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Chocolate Cake", description = "fresh baked and served with ice cream", price = "$3.99", category = category1, imagefile = "")

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Sirloin Burger", description = "Made with grade A beef", price = "$7.99", category = category1, imagefile = "")

session.add(menuItem4)
session.commit()



#Menu for Super Stir Fry
category2 = Category(user_id=1, name = "Pokemon")

session.add(category2)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Chicken Stir Fry", description = "With your choice of noodles vegetables and sauces", price = "$7.99",  category = category2, imagefile = "")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Peking Duck", description = " A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price = "$25", category = category2, imagefile = "")

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Spicy Tuna Roll", description = "Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ", price = "15",  category = category2, imagefile = "")

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Nepali Momo ", description = "Steamed dumplings made with vegetables, spices and meat. ", price = "12",  category = category2, imagefile = "")

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name = "Beef Noodle Soup", description = "A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.", price = "14",  category = category2, imagefile = "")

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name = "Ramen", description = "a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.", price = "12",  category = category2, imagefile = "")

session.add(menuItem6)
session.commit()





print "added menu items!"
