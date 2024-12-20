from flask_sqlalchemy import SQLAlchemy

# Инициализация базы данных
db = SQLAlchemy()


# Модель для бухгалтеров
class Accountant(db.Model):
    __tablename__ = 'accountants'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)

    reports = db.relationship('OrderReport', backref='accountant', lazy=True)


# Модель для водителей
class Driver(db.Model):
    __tablename__ = 'drivers'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(50), nullable=False)

    routes = db.relationship('Route', backref='driver', lazy=True)


# Модель для маршрутов
class Route(db.Model):
    __tablename__ = 'routes'

    id = db.Column(db.Integer, primary_key=True)
    departure_point = db.Column(db.String(100), nullable=False)
    destination_point = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey(
        'drivers.id'), nullable=False)

    orders = db.relationship('Order', backref='route', lazy=True)


# Модель для поставщиков
class Supplier(db.Model):
    __tablename__ = 'suppliers'

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)

    products = db.relationship('Product', backref='supplier', lazy=True)


# Модель для клиентов
class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)

    orders = db.relationship('Order', backref='client', lazy=True)


# Модель для заказов
class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey(
        'routes.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey(
        'clients.id'), nullable=False)

    status = db.Column(db.Boolean, nullable=False)

    suborders = db.relationship('Suborder', backref='order', lazy=True)
    reports = db.relationship('OrderReport', backref='order', lazy=True)


# Модель для товаров
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey(
        'suppliers.id'), nullable=False)

    suborders = db.relationship('Suborder', backref='product', lazy=True)


# Модель для подзаказов
class Suborder(db.Model):
    __tablename__ = 'suborders'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(
        'orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


# Модель для отчетов по заказу
class OrderReport(db.Model):
    __tablename__ = 'order_reports'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(
        'orders.id'), nullable=False)
    accountant_id = db.Column(db.Integer, db.ForeignKey(
        'accountants.id'), nullable=False)
    revenue = db.Column(db.Float, nullable=True, default=0.0)
    expenses = db.Column(db.Float, nullable=True, default=0.0)
    profit = db.Column(db.Float, nullable=True, default=0.0)

    def calculate_profit(self):
        self.revenue = sum(
            suborder.quantity * suborder.product.price_per_unit for suborder in self.order.suborders)
        self.expenses = self.order.route.cost

        self.profit = self.revenue - self.expenses
