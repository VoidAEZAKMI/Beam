import os

profile = os.getenv("DJANGO_PROFILE", "local")
if profile == "prod":
    from .prod import *
else:
    from .local import *
