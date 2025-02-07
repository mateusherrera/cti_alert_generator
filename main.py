"""
Esse arquivo é o ponto de entrada da aplicação.

:created by:    Mateus Herrera
:created at:    2025-02-07
"""

from cti.alerts import Alerts


if __name__ == '__main__':
    alerts_profiles = Alerts.get_to_run()
    pass
