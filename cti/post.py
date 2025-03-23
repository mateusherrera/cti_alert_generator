"""
Módulo para buscar posts.

:created by:    Mateus Herrera
:created at:    2025-03-22
"""

from utils.database_connections.db_connection import DBConnection


class Post:
    """ Classe para buscar posts. """

    # ini: methods

    @staticmethod
    def get_posts(ini_date: str, end_date: str) -> list[dict]:
        """
        Método para buscar posts no banco de dados.

        :param ini_date: Data inicial para busca dos posts.
        :param end_date: Data final para busca dos posts.
        :return: Lista com os posts encontrados.
        """
        
        pass

    # end: methods

    # end: class
    pass
