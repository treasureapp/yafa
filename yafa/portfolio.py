import datetime
from abc import ABC, abstractmethod
from typing import Iterable

from yafa.exceptions import DateNotFound, YafaException
from yafa.util import parse_date_str


class TradeSignalBase(ABC):
    date_point: datetime.date

    def __init__(self, date_str: str, symbol: str, quantity: float):
        self.quantity = quantity
        self.symbol = symbol
        self.date_point = parse_date_str(date_str)


class TradeSignal(TradeSignalBase):
    def __init__(self, date_str: str, symbol: str, quantity: float):
        super().__init__(
            date_str=date_str, symbol=symbol, quantity=quantity)


class PortfolioBase(ABC):
    _start_date: datetime.date

    def __init__(self, start_date_str: str, start_cash: float):
        self._start_cash = start_cash
        self._start_date = parse_date_str(start_date_str)

    @property
    def start_date(self) -> datetime.date:
        return self._start_date

    @abstractmethod
    def get_cash(self, date_str: str) -> float:
        pass

    @abstractmethod
    def lookup_date(self, date_point: str) -> None:
        pass

    @abstractmethod
    def handle_trade_signal(self, trade_signal: TradeSignal):
        pass

    @abstractmethod
    def handle_trade_signals(self, trade_signals: Iterable[TradeSignal]):
        pass


class Portfolio(PortfolioBase):

    def __init__(self, start_date_str, start_cash=0):
        super().__init__(start_date_str=start_date_str, start_cash=start_cash)

    def get_cash(self, date_str: str) -> float:
        date_point = parse_date_str(date_str)
        if date_point == self.start_date:
            return self._start_cash
        else:
            raise NotImplementedError

    def lookup_date(self, date_point: str) -> None:
        raise DateNotFound(date_str=date_point)

    def is_valid_trade_signal(self, trade_signal: TradeSignal):
        return trade_signal.date_point >= self.start_date

    def handle_trade_signals(self, trade_signals: Iterable[TradeSignal]):
        if not all(
                map(
                    lambda trade_signal: self.is_valid_trade_signal(trade_signal),
                    trade_signals)):
            raise YafaException

    def handle_trade_signal(self, trade_signal: TradeSignal):
        pass
