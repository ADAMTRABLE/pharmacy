from calendar import c
from flask_restx import Resource,Namespace

order_namespace = Namespace('order',description="Name of the order")

@order_namespace.route('/orders')
class makeOrder(Resource):

    def get(self):
        """get all the orders"""
        pass

    def post(self):
        """post a new order"""
        pass
@order_namespace.route('/orders/<int:order_id>')
class GetUpdateDelete(Resource):

    def get(self,order_id):
        """get a new order by id"""
        pass

    def put(self,order_id):
        """update order by id"""

    def delete(self,order_id):
        """delete a order by id"""
        pass

@order_namespace.route('/users/<int:user_id>/orders')
class UserOrders(Resource):

    def get(self,user_id):
        """get all order by specific user"""

        pass

@order_namespace.route('/orders/status/<int:order_id>')
class UpdateOrderStatus(Resource):
 
    def patch(self,order_id):
           """update order status"""

           pass

     