"""
Esse arquivo é o ponto de entrada da aplicação.

:created by:    Mateus Herrera
:created at:    2025-02-07
"""

from cti.alerts         import Alerts
from datetime           import datetime
from pandas             import DataFrame
from cti.post_example   import PostExample


def save_alert_to_file(filename: str, alert_data: dict, df_posts_relevants: DataFrame):
    """
    Essa função salva os alertas em um arquivo de texto. FUNÇÃO DE TESTE.

    :param filename:            Nome do arquivo de texto.
    :param alert_data:          Dicionário com os dados do alerta.
    :param df_posts_relevants:  DataFrame com os posts relevantes.
    """

    with open(filename, 'a') as file:
        if file.tell() != 0:
            file.write('\n\n')

        file.write(f'Alerta: {alert_data.get("id", None)}\n')
        file.write(f'Forums: {alert_data.get("forums", None)}\n')
        file.write(f'Keywords: {alert_data.get("keywords", None)}\n')
        file.write(f'Is Relevant: {alert_data.get("is_relevant", None)}\n')
        file.write(f'Generated alerts: {len(df_posts_relevants)}\n\n')

        for _, post in df_posts_relevants.iterrows():
            file.write(f'\tTitle: {post["title"]}\n')
            file.write(f'\tDescription: {post["description"]}\n')
            file.write(f'\tForum: {post["source"]}\n')
            file.write(f'\tRelevance: {post["relevance"]}\n')


if __name__ == '__main__':
    posts = PostExample.get_posts()
    df_posts = DataFrame(posts)

    alerts_profiles = Alerts.get_to_run()
    alerts_data = alerts_profiles.get('data', None)

    # Para testes
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'posts_alerted_{now}.txt'

    if alerts_data and posts:
        for alert_data in alerts_data:
            emails          = alert_data.get('emails', None)

            forums          = alert_data.get('forums', None)
            keywords        = alert_data.get('keywords', None)
            is_relevant     = alert_data.get('is_relevant', None)

            last_run        = alert_data.get('last_run', None)
            run             = alert_data.get('run', None)

            df_posts_relevants = df_posts[
                (df_posts['classification_date'] >= last_run) &
                (df_posts['classification_date'] <= run) &
                (df_posts['relevance'] >= is_relevant) &
                df_posts['source'].str.upper().isin([forum.upper() for forum in forums])
            ].copy()

            if df_posts_relevants.empty:
                Alerts.update_run_date(alert_data['id'])
                continue

            df_posts_relevants['keywords_found'] = df_posts_relevants.apply(
                lambda row: ';'
                    .join([kw for kw in keywords if kw.lower() in (row['title'] + row['description']).lower()]),
                axis=1
            )

            df_posts_relevants = df_posts_relevants[
                df_posts_relevants['title'].str.contains('|'.join(keywords), case=False, na=False) |
                df_posts_relevants['description'].str.contains('|'.join(keywords), case=False, na=False)
            ]

            if df_posts_relevants.empty:
                Alerts.update_run_date(alert_data['id'])
                continue

            # save_alert_to_file(filename, alert_data, df_posts_relevants)

            posts_alerted = [
                {
                    'id_post'           :   row['id'],
                    'title'             :   row['title'],
                    'description'       :   row['description'],
                    'alert'             :   alert_data['id'],
                    'forum'             :   row['source'],
                    'keywords_found'    :   row['keywords_found'].split(';'),
                    'relevance'         :   row['relevance'],
                    'date'              :   row['classification_date'],
                }
                for _, row in df_posts_relevants.iterrows()
            ]

            for post_alerted in posts_alerted:
                Alerts.create_post_alerted(post_alerted)
            Alerts.update_run_date(alert_data['id'])

    pass
