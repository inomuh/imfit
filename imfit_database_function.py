""" IM-FIT Database Functions """
from concurrent.futures import process
import psycopg2

global process_id
global time

# Returns system id
def get_systemid(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT process_id FROM imfit_table WHERE time = %s" ,(time,))
        myidtuple = cursor.fetchone()
        myid = myidtuple[0]
        cursor.close()
        return myid
    except(Exception, psycopg2.Error) as errorMsg:
        print("A database-related error occured: ", errorMsg)
        return []

def set_process_id(connection, time):
    global process_id
    process_id = get_systemid(connection, time)
    return process_id

# Insert user's source code into database. Gets systemname paramater to find the which user is using
def insert_time(connection, time):
    """Source codes are added to the database by that function."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO imfit_table(time) VALUES(%s)",
            (time,),
        )
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)

# Insert user's source code into database. Gets systemname paramater to find the which user is using
def insert_sourcecode(connection, file_name, source_code):
    """Source codes are added to the database by that function."""
    try:
        process_id
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO imfit_table(file_name,source_code,process_id) SELECT %s, %s, %s
            WHERE NOT EXISTS (SELECT 1 FROM imfit_table WHERE process_id = %s)
            """,
            (process_id, file_name, source_code, process_id),
        )
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)


# Insert line into database
def insert_code_snippets(connection, code_snippets):
    """Code snippets are added to the database by that function."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO imfit_table(code_snippets) VALUES(%s)", (code_snippets,)
        )
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)


# Insert line into database
def insert_possible_code_lines(connection, possible_code_lines):
    """Possible code lines are added to the database by that function."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO imfit_table(possible_code_lines) VALUES(%s)",
            (possible_code_lines,),
        )
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)


# Insert line into database
def insert_fault_names(connection, fault_names):
    """Fault names are added to the database by that function."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO imfit_table(fault_names) VALUES(%s)", (fault_names,)
        )
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)


# Insert line into database
def insert_mutation_list(connection, mutation_list):
    """Mutation list is added to the database by that function."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO imfit_table(mutation_list) VALUES(%s)", (mutation_list,)
        )
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)


# Insert line into database
def insert_fiplan_name(connection, fiplan_name):
    """FI Plan Name is added to the database by that function."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO imfit_table(fiplan_name) VALUES(%s)", (fiplan_name,)
        )
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)


# Insert line into database
def insert_fiplan_content(connection, fiplan_content):
    """FI Plan Content is added to the database by that function."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO imfit_table(fiplan_content) VALUES(%s)", (fiplan_content,)
        )
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)


# Insert line into database
def insert_mutation_info(connection, mutation_list, fiplan_name, fiplan_content):
    """FI Plan Content is added to the database by that function."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO imfit_table(mutation_list, fiplan_name ,fiplan_content) VALUES(%s,%s,%s)",
            (mutation_list, fiplan_name, fiplan_content),
        )
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)


def insert_execution_info(
    connection, held_mutant_list, killed_mutants, equivalent_mutants, survived_mutants
):
    """Information of mutants is added to the database by that function."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO imfit_table(held_mutant_list, killed_mutants, equivalent_mutants, survived_mutants) VALUES( %s, %s, %s, %s)",
            (held_mutant_list, killed_mutants, equivalent_mutants, survived_mutants),
        )
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)


def insert_metrics(connection, metrics):
    """Used metrics are added to the database by that function."""
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO imfit_table(metrics) VALUES(%s)", (metrics,))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)


def add_all_data(connection, file_name, source_code, code_snippets, possible_code_lines, fault_names, mutation_list, fiplan_name, fiplan_content, held_mutant_list, metrics, killed_mutants, equivalent_mutants, survived_mutants):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO imfit_table(file_name, source_code, code_snippets, possible_code_lines, fault_names, mutation_list, fiplan_name, fiplan_content, held_mutant_list, metrics, killed_mutants, equivalent_mutants, survived_mutants) VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)", (file_name, source_code, code_snippets, possible_code_lines, fault_names, mutation_list, fiplan_name, fiplan_content, held_mutant_list, metrics, killed_mutants, equivalent_mutants, survived_mutants,))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error_message:
        print("A database-related error occured: ", error_message)