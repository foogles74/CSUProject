from sqlmodel import Session
from torch.utils.hipify.hipify_python import value

from models.qwen.qwem_model import generate_text
from db.models.transaction import Transaction
from db.models.user import User
from db.dao.transactionDAO import get_all_transactions,create_transaction,get_history_transactions
from db.dao.userDAO import get_all_users,create_user
from db.database import init_db, engine


if __name__ == "__main__":
    generate_text("Что такое ИИ?")

    # user_admin = User(login = "admin",email="admin@admin", password="123qwe",balance=999999)
    # user_test = User(login="test", email="test@admin", password="123qwe", balance=0)
    #
    # print("Подключение к db")
    # try :
    #     init_db()
    #     print("База Подключена")
    # except Exception as e:
    #     print("Ошибка Подключения к БД по причине: "+str(e))
    #     exit(1)
    #
    # new_transactions = Transaction(user_id=1,value = 1)
    # new_test_transactions1 = Transaction(user_id=2, value=10)
    # new_test_transactions2 = Transaction(user_id=2, value=10)
    #
    # with Session(engine) as session:
    #     users = get_all_users(session)
    #     create_user(user_admin,session)
    #     create_user(user_test, session)
    #     transaction = get_all_transactions(session)
    #     create_transaction(new_transactions,session)
    #
    #     create_transaction(new_test_transactions1, session)
    #     create_transaction(new_test_transactions2, session)
    #
    #     userTransactions = get_history_transactions(2,session)
    #
    #
    # for user in userTransactions:
    #     print(user)

