from sqlmodel import Session

from db.dao.user import create_user, get_all_users
from db.database import init_db, engine
from db.models.user import User


if __name__ == "__main__":

    print("Подключение к db")
    init_db()
    print("db")

    with Session(engine) as session:
        users = get_all_users(session)

    for user in users:
        # print(f'id: {user.id} - {user.email}')
        print(user)