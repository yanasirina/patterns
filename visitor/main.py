from items import Item
from visitors import EuropeDeliveryVisitor, AsiaDeliveryVisitor, RussiaDeliveryVisitor
import consts


if __name__ == '__main__':
    item_to_europe = Item("Книга", consts.EUROPE)
    item_to_asia = Item("Электроника", consts.ASIA)
    item_to_russia = Item("Одежда", consts.RUSSIA)

    europe_visitor = EuropeDeliveryVisitor()
    asia_visitor = AsiaDeliveryVisitor()
    russia_visitor = RussiaDeliveryVisitor()

    item_to_europe.accept(europe_visitor)
    item_to_asia.accept(asia_visitor)
    item_to_russia.accept(russia_visitor)
