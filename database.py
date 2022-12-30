import os

from deta import Deta
from dotenv import load_dotenv

#Load the Environment Variable
load_dotenv(".env")
DATA_KEY = os.getenv("DATA_KEY")
#DATA_KEY = "d0unl8ve_USLEc3M7D2yNz8PbpAEC9GgDwNxit3gw"

#Initialize with Product Key
deta - Deta(DATA_KEY)

#This is how to create/connect a database
db = deta.Base("entries")

def insert_period(variance,skewness,curtosis,entropy):
    """Return the report on successful creation, otherwise raise an error"""
    return db.put({"key":variance, "skewness":skewness,"curtosis":curtosis, "entropy":entropy})


def fetch_all_periods():
    "returns a dict of all period"
    res=db.fetch()
    return res.items


def get_period(period):
    """if not found function will return None"""
    return db.get(period)