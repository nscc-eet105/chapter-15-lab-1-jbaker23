from dataclasses import dataclass
#my name is Jacob Baker and this is Chapter 15 Lab 1 being revised on July 18
@dataclass
class Employee:
    _Employee__name: str
    _Employee__hours_worked: float
    _Employee__hourly_rate: float

    @property
    def name(self):
        return self._Employee__name

    @property
    def hours_worked(self):
        return self._Employee__hours_worked

    @property
    def hourly_rate(self):
        return self._Employee__hourly_rate

    def calc_pay(self):
        return self.hours_worked * self.hourly_rate


@dataclass
class Salesperson(Employee):
    _Salesperson__weekly_sales: float
    _Salesperson__commission_percentage: float

    @property
    def weekly_sales(self):
        return self._Salesperson__weekly_sales

    @property
    def commission_percentage(self):
        return self._Salesperson__commission_percentage

    def calc_pay(self):
        base = super().calc_pay()
        commission = self.weekly_sales * self.commission_percentage
        return base + commission
