from app import ma
# from marshmallow import fields

class LensSchema(ma.Schema):
    class Meta:
        fields = ("lens_id", "model", "manufacturer", "mount", "max_aperture", "user")

    user = ma.Nested("UserSchema")

#multiple lenses schema to handle list of lenses
lenses_schema = LensSchema(many=True)    
#single lens schema to handle lens object 
lens_schema = LensSchema()