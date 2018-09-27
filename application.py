import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not ("postgresql://tssgowkofctcyh:4b746964b408a6ae79254f334ab1ec2058fab01def7c52d99edc98f0d78636dc@ec2-54-217-235-166.eu-west-1.compute.amazonaws.com:5432/d92uo0gvk9etef"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgresql://tssgowkofctcyh:4b746964b408a6ae79254f334ab1ec2058fab01def7c52d99edc98f0d78636dc@ec2-54-217-235-166.eu-west-1.compute.amazonaws.com:5432/d92uo0gvk9etef")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

if __name__ == "__main__":
    main()