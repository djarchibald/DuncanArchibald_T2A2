from app import ma
from marshmallow import fields

class CommentSchema(ma.Schema):
    class Meta:
        fields = ("comment_id", "user_id", "lens_id", "comment")

    user = fields.Nested("UserSchema")
    lens = fields.Nested("LensSchema")
    
comments_schema = CommentSchema(many=True)
comment_schema = CommentSchema()