import logging

logging.basicConfig()
logger = logging.getLogger()


class YafaException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class InvalidDate(YafaException):
    def __init__(self, date_str, *args, **kwargs):
        logger.error(__class__.__name__ + " date_str: {}".format(date_str))
        super().__init__(args, kwargs)


class DateNotFound(YafaException):
    def __init__(self, date_str, *args, **kwargs):
        logger.error(__class__.__name__ + " date_str: {}".format(date_str))
        super().__init__(args, kwargs)


class InvalidTradeSignal(YafaException):
    def __init__(self, trade_signal, *args, **kwargs):
        logger.error("Unable to process trade signal: {}".format(trade_signal))
        super().__init__(args, kwargs)
