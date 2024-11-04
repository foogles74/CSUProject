from db.DBConnect import Base, DBConnect


def init_db():
    connector = DBConnect()
    Base.metadata.create_all(bind=connector.engine)

def main():
    init_db()

print("Подключение к db")
main()
print("db")