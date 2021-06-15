from mysql.models import User


class MySQLBuilder:

    def __init__(self, client):
        self.client = client
        self.User = User.__table__

    def get_users(self):
        users = self.client.session.query(self.User).all()
        return [item.username for item in users]

    def add_user(self, username, password, email, access=1, active=0):
        row = User(
            username=username,
            password=password,
            email=email,
            access=access,
            active=active
        )
        self.client.session.add(row)
        self.client.session.commit()
        return row

    def get_user_by_name(self, username):
        row = self.client.session.query(self.User).filter_by(username=username).first()
        return row

    def block_user(self, username):
        self.client.session.query(self.User).filter_by(username=username).update({User.access: 0})
        self.client.session.commit()

    def unblock_user(self, username):
        row = self.client.session.query(self.User).filter_by(username=username)
        row.access = 1
        self.client.session.commit()

    def is_active(self, username):
        row = self.get_user_by_name(username)
        return row.active == 1
