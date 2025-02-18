"""
Módulo de alertas, para pegar e atualizar os alertas da aplicação.

:created by:    Mateus Herrera
:created at:    2025-02-07
"""

from os import getenv
from base64 import b64encode
from requests import get, post
from dotenv import load_dotenv


class Alerts:
    """ Classe de alertas. """

    # ini: attributes

    URL: str = 'http://localhost:8877/api/v1/alert/'

    # end: attributes

    # ini: methods

    @staticmethod
    def get_header() -> dict:
        """
        Pega a autenticação para acessar os alertas.

        :return:   Cabeçalho (com autenticação).
        """

        load_dotenv()
        user_django = getenv('USER_DJANGO')
        pass_django = getenv('PASS_DJANGO')

        basic_auth = b64encode(
            f'{user_django}:{pass_django}'.encode('utf-8')
        ).decode('utf-8')

        return {
            'Authorization': f'Basic {basic_auth}',
        }

    @staticmethod
    def get_to_run() -> list:
        """
        Pega os alertas ativos.

        :return:   Alertas ativos.
        """

        headers = Alerts.get_header()

        response = get(Alerts.URL + 'run/today/', headers=headers)
        return response.json()['data'] if response.json()['data'] else response.json()['error']

    @staticmethod
    def update_run_date(alert_id: int) -> dict:
        """
        Atualiza a data de execução de um alerta.

        :param alert_id:        ID do alerta.
        :return:                Alerta atualizado.
        """

        headers = Alerts.get_header()

        response = get(Alerts.URL + f'{alert_id}/update/run/', headers=headers)
        return response.json()['data'] if response.json()['data'] else response.json()['error']

    @staticmethod
    def create_post_alerted(data_post: dict) -> dict:
        """
        Cria um post alertado.
            Data example:
                {
                    'id_post': int,
                    'title': str,
                    'description': str,
                    'alert_id': int,
                    'forum': str,
                    'keywords': list,
                    'relevance': int,
                    'date': str
                }

        :param data_post:       Dados do post alertado.
        :return:                Post alertado criado.
        """

        headers = Alerts.get_header()

        response = post(Alerts.URL + 'post_alerted/', data=data_post, headers=headers)
        return response.json()['data'] if response.json()['data'] else response.json()['error']

    # end: methods

    # end: class
    pass
