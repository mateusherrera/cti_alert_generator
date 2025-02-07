"""
Módulo de alertas, para pegar e atualizar os alertas da aplicação.

:created by:    Mateus Herrera
:created at:    2025-02-07
"""

from requests import post, put


class Alerts:
    """ Classe de alertas. """

    # ini: attributes

    URL: str = 'http://localhost:8877/api/v1/alerts/'

    # end: attributes

    # ini: methods

    @staticmethod
    def get_to_run() -> list:
        """
        Pega os alertas ativos.

        :return:   Alertas ativos.
        """

        response = post(Alerts.URL + 'run/today/active/')
        if response.status_code != 200:
            return []
        return response.json()
    
    @staticmethod
    def update_run_date(alert_id: int):
        """
        Atualiza a data de execução de um alerta.

        :param alert_id:        ID do alerta.
        """

        pass

    @staticmethod
    def create_post_alerted(id_post: int, title: str, description: str, alert_id: int, forum: str, keywords: list, relevance: int, date: str):
        """
        Cria um post alertado.

        :param id_post:         ID do post.
        :param title:           Título do post.
        :param description:     Descrição do post.
        :param alert_id:        ID do alerta.
        :param forum:           Fórum do post.
        :param keywords:        Palavras-chave encontradas no post.
        :param relevance:       Relevância do post.
        :param date:            Data do post.
        """

        pass

    # end: methods

    # end: class
    pass
