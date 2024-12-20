from flask_admin.contrib.sqla import ModelView
from models import *
AViews = list()


class RouteModelView(ModelView):
    form_columns = ['departure_point', 'destination_point',
                    'datetime', 'distance', 'cost', 'driver_id']
    column_list = ['id', 'departure_point', 'destination_point',
                   'datetime', 'distance', 'cost', 'driver.full_name']
    column_labels = {'id': 'Номер', 'departure_point': 'Откуда', 'destination_point': 'Куда',
                     'datetime': 'Время', 'distance': 'Расстояние', 'cost': 'Стоимость', 'driver.full_name': 'Водитель'}
    column_searchable_list = ['id', 'departure_point', 'destination_point']
    column_filters = ['datetime', 'distance', 'cost']


class ProductModelView(ModelView):
    form_columns = ['product_name', 'category', 'price_per_unit',
                    'stock_quantity', 'supplier_id']
    column_list = ['product_name', 'category', 'price_per_unit',
                   'stock_quantity', 'supplier.company_name']
    column_labels = {'product_name': 'Название', 'category': 'Категория',
                     'price_per_unit': 'Цена', 'stock_quantity': 'Количество',
                     'supplier.company_name': 'Поставщик'}
    column_searchable_list = ['product_name']
    column_filters = ['price_per_unit', 'stock_quantity', 'category']


class OrderReportModelView(ModelView):
    form_columns = ['order_id', 'accountant_id']
    column_list = ['order_id', 'accountant.full_name',
                   'revenue', 'expenses', 'profit']
    column_labels = {'order_id': 'Заказ', 'accountant.full_name': 'Бухгалтер',
                     'revenue': 'Выручка', 'expenses': 'Расходы', 'profit': 'Прибыль'}
    column_searchable_list = ['order_id']

    # Этот метод вызывается перед сохранением модели в базу данных.
    def on_model_change(self, form, model, is_created):
        if is_created or form.order_id.data:
            model.calculate_profit()
        super().on_model_change(form, model, is_created)


class OrderModelView(ModelView):
    form_columns = ['order_date', 'route_id', 'client_id', 'status']
    column_list = ['id', 'order_date', 'route.departure_point', 'route.destination_point',
                   'client.client_name', 'status']
    column_labels = {'id': 'Номер', 'order_date': 'Дата заказа', 'route.departure_point': 'Откуда', 'route.destination_point': 'Куда',
                     'client.client_name': 'Клиент', 'status': 'Статус'}
    column_searchable_list = ['id']
    column_filters = ['order_date', 'status']


class SuborderModelView(ModelView):
    form_columns = ['order_id', 'product_id', 'quantity']
    column_list = ['order_id', 'product.product_name', 'quantity']
    column_labels = {'order_id': 'Номер заказа',
                     'product.product_name': 'Продукт', 'quantity': 'Количество'}
    column_searchable_list = ['order_id']


class ClientModelView(ModelView):
    form_columns = ['client_name', 'contact_info']
    column_list = ['client_name', 'contact_info']
    column_labels = {'client_name': 'Клиент',
                     'contact_info': 'Контактная информация'}
    column_searchable_list = ['client_name']


class SupplierModelView(ModelView):
    form_columns = ['company_name', 'contact_info']
    column_list = ['company_name', 'contact_info']
    column_labels = {'company_name': 'Поставщик',
                     'contact_info': 'Контактная информация'}
    column_searchable_list = ['company_name']


class AccountantModelView(ModelView):
    form_columns = ['full_name']
    column_list = ['full_name']
    column_labels = {'full_name': 'ФИО'}
    column_searchable_list = ['full_name']


class DriverModelView(ModelView):
    form_columns = ['full_name', 'license_number']
    column_list = ['full_name', 'license_number']
    column_labels = {'full_name': 'ФИО', 'license_number': 'Лицензия'}
    column_searchable_list = ['full_name', 'license_number']


AViews.append(ClientModelView(Client, db.session, name='Клиенты'))
AViews.append(SupplierModelView(Supplier, db.session, name='Поставщики'))
AViews.append(AccountantModelView(Accountant, db.session, name='Бухгалтеры'))
AViews.append(DriverModelView(Driver, db.session, name='Водители'))
AViews.append(RouteModelView(Route, db.session, name='Маршруты'))
AViews.append(ProductModelView(Product, db.session, name='Товары'))
AViews.append(OrderReportModelView(OrderReport, db.session, name='Отчеты'))
AViews.append(SuborderModelView(Suborder, db.session, name='Подзаказы'))
AViews.append(OrderModelView(Order, db.session, name='Заказы'))
