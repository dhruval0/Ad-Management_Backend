from server.utils.database import Base, engine
from server.models.user import Item


Base.metadata.create_all(engine)
