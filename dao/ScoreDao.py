import logging
from typing import Union, Any


class ScoreDao:
    def __init__(self, score: int):
        self.__score = score


    @staticmethod
    def _open_database_connection() -> Union[Any, Any]:
        try:
            postgres_connection = psycopg2.connect("dbname='score_si' "
                                                   "user='postgres' "
                                                   "host='localhost' " #on ubuntu change to postgres
                                                   "port='5432' "
                                                   "password='postgres'")
        except(Exception, ConnectionError) as error:
            logging.error('Exception occurred: {}'.format(error))

        return postgres_connection

    def save_score(self):
        score = self.get_record()

        if score < self.__score:
            postgres_connection = self._open_database_connection()

            cursor = postgres_connection.cursor()

            update_query = '''
            UPDATE record SET score = %s WHERE id = 1
            '''

            cursor.execute(update_query)

            cursor.close()
            postgres_connection.close()

    def get_record(self):
        postgres_connection = self._open_database_connection()

        cursor = postgres_connection.cursor()

        query = '''
        SELECT score FROM record WHERE id = 1
        '''

        cursor.execute(query)
        score = cursor.fetchall()

        cursor.close()
        postgres_connection.close()

        return score

