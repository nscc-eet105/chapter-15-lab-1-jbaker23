from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    hours_worked: float
    hourly_rate: float

    def calc_pay(self):
        return self.hours_worked * self.hourly_rate


@dataclass
class Salesperson(Employee):
    weekly_sales: float
    commission_percentage: float

    def calc_pay(self):
        base = super().calc_pay()
        commission = self.weekly_sales * self.commission_percentage
        return base + commission
