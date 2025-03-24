"""
Módulo para buscar posts.

:created by:    Mateus Herrera
:created at:    2025-03-22
"""

from utils.database_connections.db_connection import DBConnection
from pandas import read_sql


class Post:
    """ Classe para buscar posts. """

    # ini: methods

    @staticmethod
    def get_posts(ini_date: str, end_date: str, sources: list) -> dict:
        """
        Método para buscar posts no banco de dados.

        :param ini_date: Data inicial para busca dos posts.
        :param end_date: Data final para busca dos posts.
        :param sources: Lista com as fontes dos posts.
        :return: Lista com os posts encontrados.
        """

        if not isinstance(sources, list):
            sources = [sources]

        db_connection = DBConnection()
        posts = list()

        for source in sources:
            table = f'posts.{source.lower()}_classified_posts'
            query = f"""
            SELECT *
            FROM {table}
            WHERE
                classification_date BETWEEN \'{ini_date}\' AND \'{end_date}\'
            """

            with db_connection.get_connection() as conn:
                df_posts = read_sql(query, conn)
            
            posts += [
                {
                    'id': post['id'],
                    'title': post['title'],
                    'description': post['description'],
                    'relevance': post['relevance'],
                    'source': source,
                    'collect_date': post['collect_date'],
                    'classification_date': post['classification_date'],
                } for _, post in df_posts.iterrows()
            ]

        return posts


    # end: methods

    # end: class
    pass
