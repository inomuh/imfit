""" Database connection functions. """

import psycopg2


def connect(dbname, user, password):
    """ Connect function. """
    try:
        print("Connecting to database...")
        connection = psycopg2.connect("host='localhost' dbname='imfit_database' user='postgres' password='admin'")
        print("Connection to the database has been established.")
        return connection
    except(Exception, psycopg2.Error) as errorMsg:
        print("A database-related error occured: ", errorMsg)
        return None


def disconnect(connection):
    """ Disconnect function. """
    if connection:
        connection.close()
        print("\nPostgreSQL connection is closed\n")
