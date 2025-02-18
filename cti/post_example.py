"""
Módulo para buscar posts de exemplo.

:created by:    Mateus Herrera
:created at:    2025-02-18
"""

class PostExample:
    """ Classe para buscar posts de exemplo. """

    # ini: attributes

    posts: list = [
        {
            'title': 'Massive Data Leak Exposes Thousands of CPF Numbers',
            'description': 'A recent breach in a financial institution led to the leak of thousands of CPF numbers and other sensitive data.',
            'relevance': 0.9,
            'source': 'twitter',
            'collect_date': '2025-02-11',
            'classification_date': '2025-02-11'
        },
        {
            'title': 'Hackers Target Government Database',
            'description': 'A hacker group has claimed responsibility for an attack on a national government database, exposing confidential citizen records.',
            'relevance': 0.85,
            'source': 'reddit',
            'collect_date': '2025-02-11',
            'classification_date': '2025-02-11'
        },
        {
            'title': 'How to Improve Your Password Security',
            'description': 'A cybersecurity expert shares best practices for creating and managing strong passwords.',
            'relevance': 0.3,
            'source': 'medium',
            'collect_date': '2025-02-11',
            'classification_date': '2025-02-11'
        },
        {
            'title': 'New Banking Malware Spreads via Phishing Emails',
            'description': 'Cybercriminals are distributing a new type of banking malware using fake email attachments.',
            'relevance': 0.75,
            'source': 'twitter',
            'collect_date': '2025-02-11',
            'classification_date': '2025-02-11'
        },
        {
            'title': 'Tech Company Suffers Security Breach',
            'description': 'A well-known tech company confirmed a security breach but claims no sensitive user data was compromised.',
            'relevance': 0.6,
            'source': 'reddit',
            'collect_date': '2025-02-11',
            'classification_date': '2025-02-11'
        },
        {
            'title': 'CPF Database Sold on Dark Web',
            'description': 'A database containing CPF numbers and personal details is reportedly being sold on underground forums.',
            'relevance': 0.92,
            'source': 'twitter',
            'collect_date': '2025-02-11',
            'classification_date': '2025-02-11'
        },
        {
            'title': 'Ransomware Attack Hits Major Hospital Network',
            'description': 'A ransomware attack has crippled operations at several hospitals, demanding millions in cryptocurrency.',
            'relevance': 0.88,
            'source': 'reddit',
            'collect_date': '2025-02-11',
            'classification_date': '2025-02-11'
        },
        {
            'title': 'Best VPNs for 2025',
            'description': 'A cybersecurity blog reviews the top VPN services for privacy and security in 2025.',
            'relevance': 0.2,
            'source': 'blog',
            'collect_date': '2025-02-11',
            'classification_date': '2025-02-11'
        },
        {
            'title': 'New Phishing Scam Targets Bank Customers',
            'description': 'Scammers are sending fake bank alerts to trick customers into revealing their login credentials.',
            'relevance': 0.7,
            'source': 'twitter',
            'collect_date': '2025-02-11',
            'classification_date': '2025-02-11'
        },
        {
            'title': 'Leaked Credentials Lead to Unauthorized Bank Transfers',
            'description': 'Cybercriminals have used leaked login details to make unauthorized transactions from user accounts.',
            'relevance': 0.8,
            'source': 'reddit',
            'collect_date': '2025-02-11',
            'classification_date': '2025-02-11'
        },
    ]

    # end: attributes

    # ini: methods

    @staticmethod
    def get_posts():
        """ Retorna a lista de posts de exemplo. """

        return PostExample.posts

    # end: methods

    # end: class
    pass
