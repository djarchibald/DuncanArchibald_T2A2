from flask import Blueprint
from model.comment import Comment
from schema.comments_schema import comment_schema, comments_schema

comment = Blueprint('comment', __name__, url_prefix="/comments")

@comment.get("/")
def get_comments():
    comments = Comment.query.all()
    return comments_schema.dump(comments) 