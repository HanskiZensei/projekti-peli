from sqlalchemy.orm import sessionmaker

from src.database.db import engine
from src.database.models.base import Base


# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Everything else here
print("Haluatko insinööriksi?\n\n")
print("""Valitse numerolla ja paina enter
1. Uusi peli
2. Leaderboard
3. Lisää kysymys
4. Lopeta peli""")

int(input())

# TODO: Pelikoodi tähän
while True:
    # Jotain jotain
    pass

# Close session
session.close()
