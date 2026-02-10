from .connector import connect as mySqlite_connection
from sqlite3 import IntegrityError, DatabaseError, ProgrammingError

class Repository:
    
    def __init__(self):
        self._TABLENAME = None
    
    def _create_if_notExist(self):
        
        try:
            connection = mySqlite_connection()
            sql = self._create_table_sql()
            connection.execute(sql)
            connection.commit()
            connection.close()

        except ProgrammingError as e:
            print("Connection is closed:", e)

        except IntegrityError as e:
            print("Integrity error occurred:", e)
            if connection: connection.rollback()

        except DatabaseError as e:
            print("Database error occurred:", e)
            if connection: connection.rollback()
        
        except Exception as e:
            print("Unexpected error:", e)
            if connection: connection.rollback()

        finally:
            connection.close()
    def _create_table_sql(self):
        return f"""
                CREATE TABLE IF NOT EXISTS {self._TABLENAME} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME NOT NULL,
                    count REAL NOT NULL
                )
            """
    def _insert_recode_sql(self):
        return f"""
                INSERT INTO {self._TABLENAME} (timestamp, count)
                VALUES (?, ?)
            """
    def _get_last_recode_sql(self):
        return f"""
                SELECT id, timestamp, count
                FROM {self._TABLENAME}
                ORDER BY id DESC
                LIMIT 1
            """
    def _get_by_id_recode_sql(self):
        return f"""
            SELECT id, timestamp, count
            FROM {self._TABLENAME}
            WHERE id = ?
        """
    
    def _update_by_id_recode_sql(self):
        return f"""
            UPDATE {self._TABLENAME}
            SET count = ?
            WHERE id = ?
        """
    
    def _delete_by_id_recode_sql(self):
        return f"""
            DELETE FROM {self._TABLENAME}
            WHERE id = ?
        """
    def _get_many_by_timestamp_recode_sql(self):
        return f"""
            SELECT id, timestamp, count
            FROM {self._TABLENAME}
            WHERE timestamp BETWEEN ? AND ?
            ORDER BY timestamp ASC
        """
    
    def _get_all_recode_sql(self):
        return f"""
            SELECT id, timestamp, count
            FROM {self._TABLENAME}
            ORDER BY id ASC
        """
    
    def insert(self, records):
        """
        records: list of tuples -> (timestamp, count)
        """
        if not records:
            return
        
        connection = None
        try:
            connection = mySqlite_connection()

            sql = self._insert_recode_sql()

            connection.executemany(sql, records)
            connection.commit()

        except ProgrammingError as e:
            print("Programming error:", e)

        except IntegrityError as e:
            print("Integrity error:", e)
            if connection:
                connection.rollback()

        except DatabaseError as e:
            print("Database error:", e)
            if connection:
                connection.rollback()

        except Exception as e:
            print("Unexpected error:", e)
            if connection:
                connection.rollback()

        finally:
            if connection:
                connection.close()

    def get_last(self):
        """
        Returns the last record as a dict:
        {id, timestamp, count}
        """
        connection = None
        try:
            connection = mySqlite_connection()
            cursor = connection.cursor()

            sql = self._get_last_recode_sql()
            cursor.execute(sql)

            row = cursor.fetchone()

            if row is None:
                return None

            return {
                "id": row[0],
                "timestamp": row[1],
                "count": row[2]
            }

        except ProgrammingError as e:
            print("Programming error:", e)

        except DatabaseError as e:
            print("Database error:", e)

        except Exception as e:
            print("Unexpected error:", e)

        finally:
            if connection:
                connection.close()

def get_by_id(self, record_id: int):
    """
    Returns a record by id:
    {id, timestamp, count} or None if not found
    """
    connection = None
    try:
        connection = mySqlite_connection()
        cursor = connection.cursor()

        sql = self._get_by_id_recode_sql()
        cursor.execute(sql, (record_id,))

        row = cursor.fetchone()

        if row is None:
            return None

        return {
            "id": row[0],
            "timestamp": row[1],
            "count": row[2]
        }

    except ProgrammingError as e:
        print("Programming error:", e)

    except DatabaseError as e:
        print("Database error:", e)

    except Exception as e:
        print("Unexpected error:", e)

    finally:
        if connection:
            connection.close()

def update_by_id(self, record_id: int, ph_value: float) -> bool:
    """
    Updates pH value for a given record ID
    Returns True if updated, False if record not found
    """
    connection = None
    try:
        connection = mySqlite_connection()
        cursor = connection.cursor()
        
        sql = self._update_by_id_recode_sql()
        cursor.execute(sql, (count_value, record_id))

        connection.commit()

        return cursor.rowcount > 0

    except ProgrammingError as e:
        print("Programming error:", e)

    except DatabaseError as e:
        print("Database error:", e)
        if connection:
            connection.rollback()

    except Exception as e:
        print("Unexpected error:", e)
        if connection:
            connection.rollback()

    finally:
        if connection:
            connection.close()

    return False

def delete_by_id(self, record_id: int) -> bool:
    """
    Deletes a record by ID
    Returns True if deleted, False if record not found
    """
    connection = None
    try:
        connection = mySqlite_connection()
        cursor = connection.cursor()
        sql = self._delete_by_id_recode_sql()
        cursor.execute(sql, (record_id,))

        connection.commit()

        return cursor.rowcount > 0

    except ProgrammingError as e:
        print("Programming error:", e)

    except DatabaseError as e:
        print("Database error:", e)
        if connection:
            connection.rollback()

    except Exception as e:
        print("Unexpected error:", e)
        if connection:
            connection.rollback()

    finally:
        if connection:
            connection.close()

    return False

def get_many_by_timestamp(self, start_timestamp: str, end_timestamp: str):
    """
    Fetch records between start_timestamp and end_timestamp.
    
    Args:
        start_timestamp (str): 'YYYY-MM-DD HH:MM:SS'
        end_timestamp (str): 'YYYY-MM-DD HH:MM:SS'
    
    Returns:
        List of dicts: [{'id':..., 'timestamp':..., 'count':...}, ...]
    """
    connection = None
    try:
        connection = mySqlite_connection()
        cursor = connection.cursor()

        sql = self._get_many_by_timestamp_recode_sql()
        cursor.execute(self, (start_timestamp, end_timestamp))

        rows = cursor.fetchall()

        # Convert to list of dicts
        return [
            {"id": row["id"], "timestamp": row["timestamp"], "count": row["count"]}
            for row in rows
        ]

    except ProgrammingError as e:
        print("Programming error:", e)

    except DatabaseError as e:
        print("Database error:", e)

    except Exception as e:
        print("Unexpected error:", e)

    finally:
        if connection:
            connection.close()

    return []

def get_all(self):
    """
    Fetch all records from the table.
    
    Returns:
        List of dicts: [{'id':..., 'timestamp':..., 'count':...}, ...]
    """
    connection = None
    try:
        connection = mySqlite_connection()
        cursor = connection.cursor()
        sql = self._get_all_recode_sql()
        cursor.execute(sql)

        rows = cursor.fetchall()

        # Convert to list of dicts
        return [
            {"id": row["id"], "timestamp": row["timestamp"], "count": row["count"]}
            for row in rows
        ]

    except ProgrammingError as e:
        print("Programming error:", e)

    except DatabaseError as e:
        print("Database error:", e)

    except Exception as e:
        print("Unexpected error:", e)

    finally:
        if connection:
            connection.close()

    return []

        
