from db.db import get_connection, get_connection_db_server


def migrate_data_base():
    try:
        connection = get_connection_db_server()
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM pg_database WHERE datname='inventory'")
            exists = cursor.fetchone()
            if not exists:
                cursor.execute("CREATE DATABASE inventory")
            connection.close()
    except Exception as ex:
        raise Exception(ex)


def migrate_create_table():
    try:
        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS inventory
                (
                    id character(36) COLLATE pg_catalog."default" NOT NULL,
                    name character varying(50) COLLATE pg_catalog."default",
                    sellin smallint,
                    quality smallint,
                    type character varying(255) COLLATE pg_catalog."default",
                    CONSTRAINT inventory_pkey PRIMARY KEY (id)
                )
                """
            )
            connection.commit()

        connection.close()

    except Exception as ex:
        raise Exception(ex)


migrate_data_base()
migrate_create_table()

