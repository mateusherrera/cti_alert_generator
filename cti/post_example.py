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
            'id': 1,
            'title': 'Massive Data Leak Exposes Thousands of CPF Numbers',
            'description': 'A recent breach in a financial institution led to the leak of thousands of CPF numbers and other sensitive data.',
            'relevance': 0.9,
            'source': 'twitter',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 2,
            'title': 'Hackers Target Government Database',
            'description': 'A hacker group has claimed responsibility for an attack on a national government database, exposing confidential citizen records.',
            'relevance': 0.85,
            'source': 'reddit',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 3,
            'title': 'How to Improve Your Password Security',
            'description': 'A cybersecurity expert shares best practices for creating and managing strong passwords.',
            'relevance': 0.3,
            'source': 'twitter',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 4,
            'title': 'New Banking Malware Spreads via Phishing Emails',
            'description': 'Cybercriminals are distributing a new type of banking malware using fake email attachments.',
            'relevance': 0.75,
            'source': 'twitter',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 5,
            'title': 'Tech Company Suffers Security Breach',
            'description': 'A well-known tech company confirmed a security breach but claims no sensitive user data was compromised.',
            'relevance': 0.6,
            'source': 'reddit',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 6,
            'title': 'CPF Database Sold on Dark Web',
            'description': 'A database containing CPF numbers and personal details is reportedly being sold on underground forums.',
            'relevance': 0.92,
            'source': 'twitter',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 7,
            'title': 'Ransomware Attack Hits Major Hospital Network',
            'description': 'A ransomware attack has crippled operations at several hospitals, demanding millions in cryptocurrency.',
            'relevance': 0.88,
            'source': 'reddit',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 8,
            'title': 'Best VPNs for 2025',
            'description': 'A cybersecurity blog reviews the top VPN services for privacy and security in 2025.',
            'relevance': 0.2,
            'source': 'reddit',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 9,
            'title': 'New Phishing Scam Targets Bank Customers',
            'description': 'Scammers are sending fake bank alerts to trick customers into revealing their login credentials.',
            'relevance': 0.7,
            'source': 'twitter',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 10,
            'title': 'Leaked Credentials Lead to Unauthorized Bank Transfers',
            'description': 'Cybercriminals have used leaked login details to make unauthorized transactions from user accounts.',
            'relevance': 0.8,
            'source': 'reddit',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 11,
            'title': 'Massive DDoS Attack Disrupts Banking Services',
            'description': 'A coordinated DDoS attack has caused major disruptions to online banking services.',
            'relevance': 0.85,
            'source': 'twitter',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 12,
            'title': 'New Malware Variant Exploits Unpatched Systems',
            'description': 'A recently discovered malware variant is targeting outdated systems with known vulnerabilities.',
            'relevance': 0.78,
            'source': 'reddit',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 13,
            'title': 'Hackers Leak Sensitive Data from Government Agency',
            'description': 'A hacker group has published sensitive data obtained from a government agency.',
            'relevance': 0.2,
            'source': 'reddit',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 14,
            'title': 'Mirai Botnet Resurfaces with New Capabilities',
            'description': 'The infamous Mirai botnet has returned, now capable of launching more powerful DDoS attacks.',
            'relevance': 0.9,
            'source': 'twitter',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 15,
            'title': 'CPF Leak on Dark Web Raises Concerns',
            'description': 'A CPF data leak has been found on underground forums, raising security concerns.',
            'relevance': 0.91,
            'source': 'twitter',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 16,
            'title': 'New Phishing Scam Targets Social Media Users',
            'description': 'A phishing campaign is spreading on social media, stealing users’ credentials.',
            'relevance': 0.5,
            'source': 'twitter',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 17,
            'title': 'Exploit Found in Popular VPN Service',
            'description': 'Security researchers have discovered a critical exploit in a widely used VPN service.',
            'relevance': 0.8,
            'source': 'reddit',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 18,
            'title': 'Major Hacking Forum Shut Down by Authorities',
            'description': 'Law enforcement has taken down a popular hacking forum used for illegal activities.',
            'relevance': 0.5,
            'source': 'reddit',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 19,
            'title': 'Cybersecurity Firm Discovers New Ransomware Campaign',
            'description': 'A cybersecurity company has identified a large-scale ransomware operation targeting enterprises.',
            'relevance': 0.89,
            'source': 'reddit',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        },
        {
            'id': 20,
            'title': 'Data Leak Exposes Millions of Email Passwords',
            'description': 'A massive data leak has revealed millions of email credentials, raising concerns over account security.',
            'relevance': 0.93,
            'source': 'twitter',
            'collect_date': '2025-03-23',
            'classification_date': '2025-03-23'
        }
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
