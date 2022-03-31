from server.utils.database import Base, engine
# from server.models.ads import Item


Base.metadata.create_all(engine)
