class User:

    def __init__(self,user_id, login, password, email):
        self.user_id: str = user_id
        self.login: str = login
        self.password: str = password
        self.email: str = email

    def check_password(self, password: str) -> bool:
        return self.password == password

    def change_password(self,old_password, password: str) -> bool:
        if old_password == self.password:
            self.password = password
            return True
        else:
            return False