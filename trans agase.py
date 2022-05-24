# Транспортное агентство
# Разработайте программу, имитирующую работу трансагентства.
# Трансагентство имеет сеть филиалов в нескольких городах.
# Транспортировка грузов осуществляется между этими городами тремя видами транспорта: автомобильным, железнодорожным и воздушным.
# Любой вид транспортировки имеет """стоимость единицы веса на и единицу пути скорость доставки."""
# Воздушный транспорт можно использовать только между крупными городами, этот вид самый скоростной и самый дорогой.
# Кроме того, воздушный транспорт зависит от погоды. Доставить груз воздушным путем можно только при условии хорошей
# погоды одновременно в городах отправки и назначения. Хорошая или плохая погода задается случайным образом.
# Железнодорожный транспорт можно использовать между крупными и средними городами, этот вид самый дешевый.
# Автомобильный транспорт можно использовать между любыми городами.
# Заказчики через случайные промежутки времени обращаются
# в один из филиалов трансагентства с заказом на перевозку определенной массы груза и возможным пожеланием о скорости/цене доставки.
# Трансагентство организует отправку грузов одним из видов транспорта с учетом пожеланий клиента.
# Оплату трансагенство получает только после успешной доставки груза.
# Между некоторыми городами для железнодорожного и/или автомобильного транспорта имеются скоростные магистрали,
# на которых скорость соответствующего вида транспорта увеличивается с заданным коэффициентом.
# При перевозке грузов могут происходить аварии, при этом вероятность аварии на автотранспорте больше,
# чем на железнодорожном транспорте, а авиатранспорт имеет аварийность очень низкую. На скоростных магистралях вероятность аварии меньше, чем на обычных дорогах.
# При аварии трансагентство возвращает заказчику двойную стоимость перевозки.
# Процесс имитации может быть остановлен пользователем программы для просмотра параметров объектов:
import random


class TransAgencies:
    def __init__(self, unit_weight, unit_path, delivery_speed, deliv_price, weather):
        self.unit_weight = unit_weight  # единица веса
        self.unit_path = unit_path  # единица пути
        self.delivery_speed = delivery_speed  # скорость доставки
        self.deliv_price = deliv_price  # цена доставки
        self.weather = weather  # погода

    def __int__(self):
        return int(self.unit_weight * self.unit_path * self.delivery_speed)


class Air(TransAgencies):
    def __init__(self, unit_path, unit_weight, delivery_speed, deliv_price, weather):
        super().__init__(unit_path, unit_weight, delivery_speed, deliv_price, weather)

    def __str__(self):
        return f"способ доставки: {self.__class__.__name__}, скорость достовки:{self.delivery_speed},cтоимость доставки:{self.deliv_price}, что - то:{self.unit_weight * self.unit_path * self.delivery_speed}, погодные условия:{self.weather}"

    @staticmethod
    def random():
        pool = [
            {
                "nit_weight": "1.67",  # random.randint()
                "unit_path = unit_path": "1.34",  # random.randint()
                "delivery_speed": "15",  # random.randint()
                "deliv_price": "10 000 руб",
                "city": "Moscva: 15 000 000",
                "weather": random.choice("Солнечно, дождливо, ураган, метель, пыльные бури", )

            }
        ]
        return TransAgencies.random(Air, pool)


class Auto(TransAgencies):
    def __init__(self, unit_path, unit_weight, delivery_speed, deliv_price, weather):
        super().__init__(unit_path, unit_weight, delivery_speed, deliv_price, weather)


class Train(TransAgencies):
    def __init__(self, unit_path, unit_weight, delivery_speed, deliv_price, weather):
        super().__init__(unit_path, unit_weight, delivery_speed, deliv_price, weather)

# "Санкт-Петербург": "5 000 000",
# "Новосибирск": "1 500 000",
# "Нижний Новгород": "1 200 000"
