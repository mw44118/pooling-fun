# vim: set expandtab ts=4 sw=4 filetype=python:

"""
Experiment with pooling.
"""

import multiprocessing
import psycopg2

DSN = 'dbname=matt'


def setup_db():

    conn = psycopg2.connect(DSN)
    cur = conn.cursor()

    cur.execute("""
create table poolfun
(
    id serial primary key,
    right_now timestamp
);
""")
    cur.close()
    conn.commit()


def do_some_queries(conn):
    cur = conn.cursor()
    cur.execute('select 1 + 1;')
    results = cur.fetchall()

def new_connection_each_time():

    conn = psycopg2.connect(DSN)
    do_some_queries(conn)
    conn.commit()

# Write a psycopg2_pool_style function.

def query_in_loop(query_doer):

    """
    Run the query_doer function (whatever it is) a thousand times.
    """

    for i in xrange(100):
        query_doer()


# Write a query_in_separate_process function.
def query_in_separate_process(query_doer):
    """
    Run the query_doer function a thousand times, each in a separate
    process.

    So, each of those thousand processes should be happening in
    parallel.
    """

    for i in xrange(1000):
        p = multiprocessing.Process(target=query_doer)
        p.start()


# Run style functions with threads.
# Run all doers (new connection each time, psycopg2 pool, SQLObject
# pooling, SQL Alchemy pooling, antipool pooling) with all three
# scenarios (query_in_loop, multiprocessing, multithreading).



