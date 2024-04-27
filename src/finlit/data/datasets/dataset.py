"""
Base class for all datasets.
"""

from abc import ABC, abstractmethod
from typing import Any

from finlit.data.ledger import Ledger
from pandas import DataFrame
from pgloader.utils import START_MONTH, START_YEAR
from sqlalchemy.engine import Engine


class Dataset(ABC):
    """
    Base class for all datasets.
    """

    def __init__(  # noqa: PLR0913
        self,
        ledger: Ledger,
        engine: Engine,
        table_name: str,
        first_available_year: int = START_YEAR,
        first_available_month: int = START_MONTH,
    ) -> None:
        """
        Initialize the table object.
        """
        super().__init__()
        self.engine = engine
        self.table_name = table_name
        self.ledger = ledger
        self.first_available_year = first_available_year
        self.first_available_month = first_available_month

    @abstractmethod
    def build(self, **kwargs: dict[str, Any]) -> DataFrame:
        """
        Build the table in the database.
        """