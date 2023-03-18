from flask import Blueprint, jsonify, request
from model.comment import Comment
from schema.comments_schema import comment_schema, comments_schema
from app import db

comment = Blueprint('comment', __name__, url_prefix="/comments")

@comment.get("/")
def get_comments():
    comments = Comment.query.all()
    return comments_schema.dump(comments) 

@comment.get("/<int:id>")
def get_comment(id):
    comment = Comment.query.get(id)
    
    if not comment:
        return {"message": "I can't find that comment"}
    
    return comment_schema.dump(comment)

@comment.post("/")
def create_comment():
    try:
        comment_fields = comment_schema.load(request.json)

        comment = Comment(**comment_fields)
           
        db.session.add(comment)
        db.session.commit()
    except:
        return {"message": "Hmm. I can't seem to post that comment. Check the information is correct." }
    
    return comment_schema.dump(comment)