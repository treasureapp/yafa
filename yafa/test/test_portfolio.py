import datetime

import pytest

from yafa.exceptions import DateNotFound, YafaException
from yafa.portfolio import Portfolio, TradeSignal


@pytest.mark.portfolio
def test_portfolio_start_date():
    mock_start_date = datetime.date(2018, 1, 1)
    mock_start_date_str = mock_start_date.isoformat()
    mock_start_cash = 666
    portfolio = Portfolio(
        start_date_str=mock_start_date_str, start_cash=mock_start_cash)
    assert mock_start_date == portfolio.start_date


@pytest.mark.portfolio
def test_portfolio_start_cash():
    mock_start_date = "2018-01-01"
    mock_start_cash = 666
    portfolio = Portfolio(
        start_date_str=mock_start_date, start_cash=mock_start_cash)
    assert mock_start_cash == portfolio.get_cash(mock_start_date)


@pytest.mark.portfolio
def test_date_not_found():
    mock_start_date = "2018-01-01"
    mock_start_cash = 666
    mock_bad_date = "2017-01-01"

    portfolio = Portfolio(
        start_date_str=mock_start_date, start_cash=mock_start_cash)
    with pytest.raises(DateNotFound):
        portfolio.lookup_date(mock_bad_date)
    with pytest.raises(YafaException):
        portfolio.lookup_date(mock_bad_date)


@pytest.mark.portfolio
def test_trade_signal():
    mock_start_date = "2018-01-01"
    mock_start_cash = 666
    mock_bad_date = "2017-01-01"
    trade_signals = [
        TradeSignal(date_str=mock_bad_date, symbol="ABC", quantity=10)
    ]

    portfolio = Portfolio(
        start_date_str=mock_start_date, start_cash=mock_start_cash)
    with pytest.raises(YafaException):
        portfolio.handle_trade_signals(trade_signals=trade_signals)


@pytest.mark.portfolio
def test_valid_trade_signal():
    mock_start_date = "2018-01-01"
    mock_start_cash = 666
    trade_signals = [
        TradeSignal(date_str=mock_start_date, symbol="ABC", quantity=10)
    ]

    portfolio = Portfolio(
        start_date_str=mock_start_date, start_cash=mock_start_cash)
    portfolio.handle_trade_signals(trade_signals=trade_signals)
