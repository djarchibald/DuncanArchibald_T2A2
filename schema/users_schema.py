from app import ma
from marshmallow import fields

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "verified", "name", "email", "phone")
#multiple users schema
users_schema = UserSchema(many=True)
#single user schema
user_schema = UserSchema() 