from app import ma

class CommentSchema(ma.Schema):
    class Meta:
        fields = ("comment_id", "user_id", "lens_id", "comment")
    
comments_schema = CommentSchema(many=True)
comment_schema = CommentSchema()