from .PylitDomain import PylitDomain

def setup(app):
    app.add_domain(PylitDomain)

