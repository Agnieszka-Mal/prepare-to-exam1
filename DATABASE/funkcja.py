def execute_sql(db, sql_code):
    """
    Run given sql code with psycopg2.

    :param str sql_code: sql code to run
    :param str db: name of db,

    :rtype: list
    :return: data from psycobg2 cursor as a list (can be None) if nothing to fetch.
    """
    # Place exercise 1 solution here.
    try:
        cnx = connect(user=USER, password=PASSWORD, host=HOST, database=db)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql_code)
        results = None
        if cursor.rowcount > 0:
            results = cursor.fetchall()
    except:
        print("There is error in execute_sql")
    else:
        cursor.close()
        cnx.close()
    return results


results = execute_sql("exercises_db", "SELECT * FROM products;")
for res in results:
    print(res)
