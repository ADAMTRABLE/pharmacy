from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import serializer
from marshmallow import Schema,fields

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://postgres:adam@localhost/recipes'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)



class Recipe(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    description = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class RecipeSchema(Schema):
    id =fields.Integer()
    name =fields.String()
    description =fields.String()

@app.route('/recipes',methods=['GET'])
def get_all_recipes():
    recipes =Recipe.get_all()
    serializer =RecipeSchema(many=True)
    data = serializer.dump(recipes)
    return jsonify(data)

@app.route('/create',methods=['POST'])
def insert_recipes():
    data =request.get_json()
    new=Recipe(name = data.get('name'),
    description=data.get('description'))
    new.save()
    serializer =RecipeSchema(many=True)
    return jsonify(data),201

if __name__ =='__main__':
    app.run(debug=True)