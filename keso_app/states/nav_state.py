import reflex as rx
from . import routes

class NavState(rx.State):

    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_production(self):
        return rx.redirect(routes.PRODUCTION_ROUTE)

    def to_cattle(self):
        return rx.redirect(routes.CATTLE_ROUTE)
    
    def to_transactions(self):
        return rx.redirect(routes.TRANSACTIONS_ROUTE)
    
    def to_system_logs(self):
        return rx.redirect(routes.SYSTEM_LOGS_ROUTE)
    
    def to_settings(self):
        return rx.redirect(routes.SETTINGS_ROUTE)
    
    def to_help(self):
        return rx.redirect(routes.HELP_ROUTE)