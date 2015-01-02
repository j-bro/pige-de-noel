"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb

class FromTo(ndb.Model):
    """
    Representation of a participant who will gift to another
    Structured Property of an Exchange Property
    """
    from_user = ndb.StringProperty() # id of "FROM" participant
    to_user = ndb.StringProperty() # id of "TO" participant
    
class GiftList(ndb.Model):
    """
    Gift lists for each participant in the exchange
    """
    user_id = ndb.StringProperty(required=True)
    list = ndb.TextProperty(required=True, default='')
    
class Exchange(ndb.Model):
    """
    An exchange in which a group participates
    Structured Property of a Group Model
    """
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)
    active = ndb.BooleanProperty(required=True, default=False)
    price_cap = ndb.IntegerProperty(required=True)
    draw = ndb.StructuredProperty(FromTo, repreated=True)
    lists = ndb.StructuredProperty(List, repeated=True)

class Group(ndb.Model):
    """Group of users"""
    name = ndb.StringProperty(required=True)
    administrator = ndb.StringProperty(required=True) # id of group administrator
    participants = ndb.StringProperty(repeated=True) # id of participants
    exchanges = ndb.StructuredProperty(Exchange, repeated=True)
    
class User(ndb.Model):
    """App user"""
    user_id = ndb.StringProperty(required=True) # user_id from Google login User object
    name = ndb.StringProperty(required=True)
    first_login = ndb.DateTimeProperty(auto_now_add=True)
    last_login = ndb.DateTimeProperty(auto_now=True)
    