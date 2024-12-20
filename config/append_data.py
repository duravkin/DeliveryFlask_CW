from datetime import datetime, timedelta
# from app import db
from run import app
from models import db, Accountant, Driver, Route, Supplier, Client, Order, Product, Suborder, OrderReport


def populate_database():
    with app.app_context():
        # Удаление существующих данных и создание таблиц заново
        db.drop_all()
        db.create_all()

        # Заполнение данных для бухгалтеров
        accountants = [
            Accountant(full_name="Иванов Иван"),
            Accountant(full_name="Петрова Анна"),
            Accountant(full_name="Смирнов Дмитрий"),
            Accountant(full_name="Козлова Мария"),
            Accountant(full_name="Федоров Александр")
        ]
        db.session.add_all(accountants)

        # Заполнение данных для водителей
        drivers = [
            Driver(full_name="Сидоров Алексей", license_number="ABC12345"),
            Driver(full_name="Кузнецов Михаил", license_number="XYZ67890"),
            Driver(full_name="Орлов Павел", license_number="LMN34567"),
            Driver(full_name="Васильев Виктор", license_number="JKL89012"),
            Driver(full_name="Горбунов Сергей", license_number="QWE56789")
        ]
        db.session.add_all(drivers)

        # Заполнение данных для маршрутов
        routes = [
            Route(departure_point="Москва", destination_point="Санкт-Петербург",
                  datetime=datetime.now(), distance=700.5, cost=12000.0, driver=drivers[0]),
            Route(departure_point="Казань", destination_point="Екатеринбург", datetime=datetime.now(
            ) + timedelta(days=1), distance=900.0, cost=15000.0, driver=drivers[1]),
            Route(departure_point="Нижний Новгород", destination_point="Самара", datetime=datetime.now(
            ) + timedelta(days=2), distance=500.0, cost=10000.0, driver=drivers[2]),
            Route(departure_point="Уфа", destination_point="Пермь", datetime=datetime.now(
            ) + timedelta(days=3), distance=300.0, cost=8000.0, driver=drivers[3]),
            Route(departure_point="Краснодар", destination_point="Волгоград", datetime=datetime.now(
            ) + timedelta(days=4), distance=400.0, cost=9000.0, driver=drivers[4])
        ]
        db.session.add_all(routes)

        # Заполнение данных для поставщиков
        suppliers = [
            Supplier(company_name="ООО 'Поставщик 1'",
                     contact_info="info@supplier1.ru"),
            Supplier(company_name="ООО 'Поставщик 2'",
                     contact_info="info@supplier2.ru"),
            Supplier(company_name="ООО 'Поставщик 3'",
                     contact_info="info@supplier3.ru"),
            Supplier(company_name="ООО 'Поставщик 4'",
                     contact_info="info@supplier4.ru"),
            Supplier(company_name="ООО 'Поставщик 5'",
                     contact_info="info@supplier5.ru")
        ]
        db.session.add_all(suppliers)

        # Заполнение данных для товаров
        products = [
            Product(product_name="Телевизор", category="Электроника",
                    price_per_unit=30000.0, stock_quantity=50, supplier=suppliers[0]),
            Product(product_name="Холодильник", category="Бытовая техника",
                    price_per_unit=40000.0, stock_quantity=30, supplier=suppliers[1]),
            Product(product_name="Смартфон", category="Электроника",
                    price_per_unit=20000.0, stock_quantity=100, supplier=suppliers[2]),
            Product(product_name="Микроволновка", category="Бытовая техника",
                    price_per_unit=7000.0, stock_quantity=20, supplier=suppliers[3]),
            Product(product_name="Стиральная машина", category="Бытовая техника",
                    price_per_unit=25000.0, stock_quantity=15, supplier=suppliers[4])
        ]
        db.session.add_all(products)

        # Заполнение данных для клиентов
        clients = [
            Client(client_name="ООО 'Клиент 1'",
                   contact_info="client1@example.com"),
            Client(client_name="ООО 'Клиент 2'",
                   contact_info="client2@example.com"),
            Client(client_name="ИП 'Клиент 3'",
                   contact_info="client3@example.com"),
            Client(client_name="ООО 'Клиент 4'",
                   contact_info="client4@example.com"),
            Client(client_name="ИП 'Клиент 5'",
                   contact_info="client5@example.com")
        ]
        db.session.add_all(clients)

        # Заполнение данных для заказов
        orders = [
            Order(order_date=datetime.now(),
                  route=routes[0], client=clients[0], status=True),
            Order(order_date=datetime.now() + timedelta(days=1),
                  route=routes[1], client=clients[1], status=False),
            Order(order_date=datetime.now() + timedelta(days=2),
                  route=routes[2], client=clients[2], status=True),
            Order(order_date=datetime.now() + timedelta(days=3),
                  route=routes[3], client=clients[3], status=False),
            Order(order_date=datetime.now() + timedelta(days=4),
                  route=routes[4], client=clients[4], status=True)
        ]
        db.session.add_all(orders)

        # Заполнение данных для подзаказов
        suborders = [
            Suborder(order=orders[0], product=products[0], quantity=2),
            Suborder(order=orders[1], product=products[1], quantity=1),
            Suborder(order=orders[2], product=products[2], quantity=3),
            Suborder(order=orders[3], product=products[3], quantity=1),
            Suborder(order=orders[4], product=products[4], quantity=2)
        ]
        db.session.add_all(suborders)

        # Заполнение данных для отчетов по заказу
        reports = [
            OrderReport(order=orders[0], accountant=accountants[0],
                        revenue=60000.0, expenses=40000.0, profit=20000.0),
            OrderReport(order=orders[1], accountant=accountants[1],
                        revenue=40000.0, expenses=25000.0, profit=15000.0),
            OrderReport(order=orders[2], accountant=accountants[2],
                        revenue=60000.0, expenses=30000.0, profit=30000.0),
            OrderReport(order=orders[3], accountant=accountants[3],
                        revenue=20000.0, expenses=10000.0, profit=10000.0),
            OrderReport(order=orders[4], accountant=accountants[4],
                        revenue=50000.0, expenses=35000.0, profit=15000.0)
        ]
        db.session.add_all(reports)

        # Сохранение изменений в базе данных
        db.session.commit()
        print("Данные успешно добавлены в базу.")


if __name__ == "__main__":
    populate_database()
