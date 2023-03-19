from app import ma
# from marshmallow import fields

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "verified", "name", "email", "phone", "lenses")
    
    lenses = ma.List(ma.Nested("LensSchema", exclude=["user"]))
#multiple users schema
users_schema = UserSchema(many=True)
#single user schema
user_schema = UserSchema() 