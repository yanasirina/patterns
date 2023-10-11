from factory_method import factories, consts


if __name__ == '__main__':
    """Закажем разные версии MyPhone в разных странах"""
    japanese_factory = factories.JapanFactory()
    russian_factory = factories.RussiaFactory()
    uae_factory = factories.UAEFactory()

    japanese_factory.order_phone(phone_type=consts.MY_PHONE_MINI)
    russian_factory.order_phone(phone_type=consts.MY_PHONE_STANDARD)
    uae_factory.order_phone(phone_type=consts.MY_PHONE_MAX)
