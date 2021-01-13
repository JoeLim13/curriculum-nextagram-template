from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    username = pw.CharField(unique=True, aka='name')
    password = pw.CharField()
    email = pw.CharField()
    
    def validate(self):
        duplicate_users = User.get_or_none(User.username == self.username)

        if duplicate_users:
            self.errors.append('Username Taken')


