from dataclasses import dataclass


@dataclass
class HistoryItem:
    good_id: int
    count: int
    price: int


@dataclass
class User:
    login: str
    password: str  # TODO hash
    is_admin: bool
    authorized: bool
    basket: dict
    total_price: int
    history: list[HistoryItem]  # list of history item


@dataclass
class Good:
    name: str
    price: int
    count: int
    # specifications: dict spec_name and value


@dataclass
class ShoppingBasketItem:
    count: int
    price: int
