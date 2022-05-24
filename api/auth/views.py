from flask_restx import Namespace,Resource

auth_namespace = Namespace('auth',description="namespace for authentication")

@auth_namespace.route('/signup')
class Signup(Resource):

    def post(self):
        """create a new user"""
        pass

@auth_namespace.route('/login')
class Login(Resource):
    def post(self):
        """login a user"""
        pass

@auth_namespace.route('/user/<int:user_id>/orders/<int:order_id>')
class GetSpecificOrder(Resource):
    def get(self,user_id,order_id):
        """get a specific order"""
        pass