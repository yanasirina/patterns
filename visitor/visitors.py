class DeliveryVisitor:
    """Абстрактная транспортная компания"""
    def visit_europe(self, europe):
        pass

    def visit_asia(self, asia):
        pass

    def visit_russia(self, russia):
        pass


class EuropeDeliveryVisitor(DeliveryVisitor):
    """Транспортная компания для Европы"""
    def visit_europe(self, item):
        print(f"Доставка товара {item.name} в Европу через транспортную компанию для Европы")

    def visit_asia(self, item):
        print(f"Доставка товара {item.name} в Азию не поддерживается")

    def visit_russia(self, item):
        print(f"Доставка товара {item.name} в Россию не поддерживается")


class AsiaDeliveryVisitor(DeliveryVisitor):
    """Транспортная компания для Азии"""
    def visit_europe(self, item):
        print(f"Доставка товара {item.name} в Европу не поддерживается")

    def visit_asia(self, item):
        print(f"Доставка товара {item.name} в Азию через транспортную компанию для Азии")

    def visit_russia(self, item):
        print(f"Доставка товара {item.name} в Россию не поддерживается")


class RussiaDeliveryVisitor(DeliveryVisitor):
    """Транспортная компания для России"""
    def visit_europe(self, item):
        print(f"Доставка товара {item.name} в Европу не поддерживается")

    def visit_asia(self, item):
        print(f"Доставка товара {item.name} в Азию не поддерживается")

    def visit_russia(self, item):
        print(f"Доставка товара {item.name} в Россию через транспортную компанию для России")
