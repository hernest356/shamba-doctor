import mysql.connector


def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="347882356",
        database="shamba_doctor"
    )

    return connection


def get_crop(crop_name):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT *
        FROM crops
        WHERE LOWER(crop_name) = LOWER(%s)
    """

    cursor.execute(query, (crop_name,))
    crop = cursor.fetchone()

    cursor.close()
    connection.close()

    return crop