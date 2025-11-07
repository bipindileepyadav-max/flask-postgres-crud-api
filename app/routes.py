from flask_restx import Namespace, Resource, fields
from flask import request
from model import Customer, Product, Order
from db import db
from settings_config import pagination_per_page, swagger_name, swagger_desc

api = Namespace(swagger_name, description=swagger_desc)

# DB Models
customer_model = api.model('Customer', {
    'id': fields.Integer(readOnly=True),
    'name': fields.String(required=True),
    'email': fields.String(required=True)
})

product_model = api.model('Product', {
    'id': fields.Integer(readOnly=True),
    'name': fields.String(required=True),
    'price': fields.Float(required=True)
})

order_model = api.model('Order', {
    'id': fields.Integer(readOnly=True),
    'customer_id': fields.Integer(required=True),
    'product_id': fields.Integer(required=True),
    'quantity': fields.Integer(required=True)
})


# Pagination utilities
def paginate_query(model):
    """Paginate any SQLAlchemy model"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', pagination_per_page, type=int)
    pagination = model.query.paginate(page=page, per_page=per_page, error_out=False)
    return {
        'total': pagination.total,
        'page': pagination.page,
        'pages': pagination.pages,
        'per_page': pagination.per_page,
        'data': [item for item in pagination.items]
    }


# Customers route
@api.route('/customers')
class Customers(Resource):
    @api.marshal_list_with(customer_model, envelope='data')
    def get(self):
        """Get all customers with pagination"""
        return paginate_query(Customer)['data']

    @api.expect(customer_model)
    @api.marshal_with(customer_model, code=201)
    def post(self):
        data = request.json
        customer = Customer(name=data['name'], email=data['email'])
        db.session.add(customer)
        db.session.commit()
        return customer, 201

# Products route
@api.route('/products')
class Products(Resource):
    @api.marshal_list_with(product_model, envelope='data')
    def get(self):
        """Get all products with pagination"""
        return paginate_query(Product)['data']

    @api.expect(product_model)
    @api.marshal_with(product_model, code=201)
    def post(self):
        data = request.json
        product = Product(name=data['name'], price=data['price'])
        db.session.add(product)
        db.session.commit()
        return product, 201


# Orders route
@api.route('/orders')
class Orders(Resource):
    @api.marshal_list_with(order_model, envelope='data')
    def get(self):
        """Get all orders with pagination"""
        return paginate_query(Order)['data']

    @api.expect(order_model)
    @api.marshal_with(order_model, code=201)
    def post(self):
        data = request.json
        order = Order(customer_id=data['customer_id'], product_id=data['product_id'], quantity=data['quantity'])
        db.session.add(order)
        db.session.commit()
        return order, 201


# Orders details using join custom-logic
@api.route('/orders/details')
class OrderDetails(Resource):
    def get(self):
        """Return paginated order details with JOIN (Customer + Product + Order)"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)

        query = db.session.query(
            Order.id,
            Customer.name.label('customer_name'),
            Product.name.label('product_name'),
            Order.quantity,
            Product.price,
        ).join(Customer, Order.customer_id == Customer.id)\
         .join(Product, Order.product_id == Product.id)

        pagination = query.paginate(page=page, per_page=per_page, error_out=False)

        return {
            'total': pagination.total,
            'page': pagination.page,
            'pages': pagination.pages,
            'per_page': pagination.per_page,
            'data': [
                {
                    'order_id': row.id,
                    'customer': row.customer_name,
                    'product': row.product_name,
                    'quantity': row.quantity,
                    'price': row.price,
                    'total': row.quantity * row.price
                }
                for row in pagination.items
            ]
        }
