from matplotlib import pyplot as plt

class GraphicFunction:
    @staticmethod
    def draw_orders_cities(orders):
        plt.bar(orders.keys(), [len(value) for value in orders.values()], width=0.5, color='red')
        plt.xlabel('Города')
        plt.ylabel('Количество заказов')
        plt.title('Статистика заказов')
        plt.savefig('./main/static/main/img/order_sities_stat.jpg')
        plt.clf()

    @staticmethod
    def draw_incomes_stats(months, sales, incomes):
        plt.plot(months, sales, marker='o', markersize=5, linestyle='-')
        plt.xlabel('Месяц')
        plt.ylabel('Продажи')
        plt.title('Количество продажи по месяцам')
        plt.savefig('./main/static/main/img/month_amount_stat.jpg')
        plt.clf()
        plt.bar(months, incomes)
        plt.xlabel('Месяц')
        plt.ylabel('Сумма продаж')
        plt.title('Сумма продаж по месяцам')
        plt.savefig('./main/static/main/img/month_incomes_stat.jpg')
        plt.clf()