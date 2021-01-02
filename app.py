import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(engine, reflect=True)

#Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create our session (link) from Python to the DB
session = Session(engine)

#Flask Setup
app = Flask(__name__)


#Flask Routes
@app.route("/")
def welcome():
    test = (f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>" 
        f"/api/v1.0/temp/start/end")
    return (test)

#Find precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year"""
    # Calculate the date 1 year ago from last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query for the date and precipitation for the last year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    # Dict with date as the key and prcp as the value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
