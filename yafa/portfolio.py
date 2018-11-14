from abc import ABC, abstractmethod
from typing import Iterable

from yafa.exceptions import DateNotFound, YafaException


class TradeSignalBase(ABC):
    def __init__(self, date_point: str, symbol: str, quantity: float):
        self.quantity = quantity
        self.symbol = symbol
        self.date_point = date_point


class TradeSignal(TradeSignalBase):
    def __init__(self, date_point: str, symbol: str, quantity: float):
        super().__init__(
            date_point=date_point, symbol=symbol, quantity=quantity)


class PortfolioBase(ABC):
    def __init__(self, start_date: str, start_cash: float):
        self._start_cash = start_cash
        self._start_date = start_date

    @property
    def start_date(self) -> str:
        return self._start_date

    @abstractmethod
    def get_cash(self, date_point: str) -> float:
        pass

    @abstractmethod
    def lookup_date(self, date_point: str) -> None:
        pass


class Portfolio(PortfolioBase):
    def __init__(self, start_date, start_cash=0):
        super().__init__(start_date=start_date, start_cash=start_cash)

    def get_cash(self, date_point: str) -> float:
        return self._start_cash

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
