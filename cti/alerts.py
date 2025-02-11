"""
Módulo de alertas, para pegar e atualizar os alertas da aplicação.

:created by:    Mateus Herrera
:created at:    2025-02-07
"""

from os import getenv
from requests import get
from base64 import b64encode
from dotenv import load_dotenv


class Alerts:
    """ Classe de alertas. """

    # ini: attributes

    URL: str = 'http://localhost:8877/api/v1/alert/'

    # end: attributes

    # ini: methods

    @staticmethod
    def get_to_run() -> list:
        """
        Pega os alertas ativos.

        :return:   Alertas ativos.
        """

        load_dotenv()
        user_django = getenv('USER_DJANGO')
        pass_django = getenv('PASS_DJANGO')

        basic_auth = b64encode(
            f'{user_django}:{pass_django}'.encode('utf-8')
        ).decode('utf-8')

        headers = {
            'Authorization': f'Basic {basic_auth}',
        }

        response = get(Alerts.URL + 'run/today/', headers=headers)
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
    def create_post_alerted(data_post: dict):
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
        """

        pass

    # end: methods

    # end: class
    pass
