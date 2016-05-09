"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year<1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded>1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.discontinued!=None, Brand.founded==1903).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter((Brand.discontinued==None) | (Brand.founded<1950)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name!='Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    print (db.session.query(Model.name, Model.brand_name, Brand.headquarters)
           .filter(Model.year==year).all())



def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # I think I'm meant to only list the Brand.name once for all the models of that 
    # brand but I'm not sure how to do this with only one query.
    print (db.session.query(Brand.name, Model.name).group_by(Brand.name, Model.name).all())


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# I don't think this returns anything? 

# Doesn't it need a .all() or .first() or .one() to actually return something since it doesn't use the .get() method?

# If it has a .first or .one or .all, I think it returns a tuple of objects.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association is a table that purely exists to separate two tables that have a many to many relationship so that there are two one(original tables) to many(association table) relationships.

# Looks like T1 -one to many- AssocT -many to one- T2

# Columns to exist in the association table are 1. FromT1FromT2_id = primary key, 2. Foreign key that is primary key of T1, and 3. Foreign key that is primary key of T2 

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Takes mystr and returns a list of objects that are brands
    that contains or is equal to mystr."""

    return Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()

def get_models_between(start_year, end_year):
    """Takes a start_year and end_year and returns a list of model objects
    that are between start_year(inclusive) and end_year(exclusive)."""

    return Model.query.filter(Model.year.in_(range(start_year, end_year))).all()

