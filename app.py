# Import the dependencies.
import os
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, func, and_

from flask import Flask, jsonify, request, g


#################################################
# Database Setup
#################################################
# sqlpath = os.path.abspath("C:/Users/Jessi/Desktop/Data Analytics Bootcamp/Challenges/Challenge_10/sqlalchemy-challenge/SurfsUp/Resources/hawaii.sqlite")
# engine = create_engine(f"sqlite:///{sqlpath}")  

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(autoload_with=engine)

# # Save references to each table
# measurements = Base.classes.measurement
# stations = Base.classes.station

# # Create our session (link) from Python to the DB
# # session = Session(engine)
# SessionClass = sessionmaker(bind=engine)
# session = SessionClass()

# def get_date_ranges():
#     most_recent_date = session.query(func.max(measurements.date)).scalar()
#     most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d')  # Convert to datetime
#     one_year_earlier_date = most_recent_date - dt.timedelta(days=365)
#     return most_recent_date, one_year_earlier_date


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Before each request, set the session to the global 'g' object (help from chatgpt)
@app.before_request
def before_request():
    g.session = session

# After each request, close the session
@app.teardown_request
def teardown_request(exception=None):
    if hasattr(g, 'session'):
        g.session.close()


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>     Shows precipitation readings for the last 12 months recorded for all stations.<br/><br/>"
        f"/api/v1.0/stations<br/>     Shows Station names and id numbers.<br/><br/>"  
        f"/api/v1.0/tobs<br/>     Shows temperature readings for the last 12 months recorded for the station with the most observations - Waihee Station.<br/><br/>"
        f"/api/v1.0/DATE<br/>     Shows the minimum temperature, maximum temperature, and average temperature at Waihee Station from selected date to 8/23/17. <br/> Replace 'DATE' with your own date in the format year-month-day.  For example, /api/v1.0/2010-1-16.<br/><br/>"
        f"/api/v1.0/DATE/DATE<br/>     Shows the minimum temperature, maximum temperature, and average temperature at Waihee Station from first selected date through second selected date. <br/>Replace each 'DATE' with your own start and end dates in the format year-month-day.  For example, /api/v1.0/2011-9-1/2012-8-7."
    )

#################################################
# About the survey page
#################################################

@app.route("/about")
def about():
    most_recent_date, one_year_earlier_date = get_date_ranges()

    recent_year_data = g.session.query(measurements.date, measurements.prcp).\
        filter(and_(measurements.date >= one_year_earlier_date,
                    measurements.date <= most_recent_date)).all()

    all_precipitations = []
    for date, prcp in recent_year_data:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["precipitation"] = prcp
        all_precipitations.append(precipitation_dict)

    return jsonify(all_precipitations)

#################################################
# Survey Page
#################################################

@app.route("/survey")
def survey():

    # Query all stations
    station_query = g.session.query(stations).all()

    # Create a list of dictionaries for all stations
    all_stations = []
    for station in station_query:
        station_dict = {}
        station_dict["station"] = station.station
        station_dict["name"] = station.name
        all_stations.append(station_dict)

    return jsonify(all_stations)

#################################################
# Results Page
#################################################

@app.route("/results")
def results():
    
    return 


#################################################
# Another Page?
#################################################

@app.route("/api/v1.0/<start>")
def temp_stats1(start):
    
    return 

#################################################
# Another Page?
#################################################

@app.route("/api/v1.0/<start>/<end>")
def temp_stats2(start,end):
    
    return jsonify(most_active_station_temps)



if __name__ == '__main__':
    app.run(debug=True)
