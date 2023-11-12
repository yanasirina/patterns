import consts


class Item:
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def accept(self, visitor):
        if self.region == consts.EUROPE:
            visitor.visit_europe(self)
        elif self.region == consts.ASIA:
            visitor.visit_asia(self)
        elif self.region == consts.RUSSIA:
            visitor.visit_russia(self)
        else:
            raise Exception('Выбранный регион недоступен')
