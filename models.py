import pandas as pd
import re
from datetime import datetime


class Salesperson:
    def __init__(self, name, cpf, birth_date, email, state):
        self.name = name

        if self.validade_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF inválido")

        if self.validate_birth_date(birth_date):
            self.birth_date = birth_date
        else:
            raise ValueError("Data de nascimento inválida")

        if self.validate_email(email):
            self.email = email
        else:
            raise ValueError("E-mail inválido")

        self.state = state
        self.sales = []

    def format_cpf(self, cpf):
        cpf_digits = ''.join(filter(str.isdigit, cpf))
        formatted_cpf = '{}.{}.{}-{}'. format(
            cpf_digits[:3], cpf_digits[3:6], cpf_digits[6:9], cpf_digits[9:])
        return formatted_cpf

    def validade_cpf(self, cpf):
        cpf_digits = ''.join(filter(str.isdigit, cpf))
        return len(cpf_digits) == 11

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_birth_date(self, birth_date):
        try:
            datetime.strptime(birth_date, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def add_sale(self, value, channel):
        comission = self.calculate_comission(value, channel)
        sale = {'valor': value, 'canal': channel, 'comissao': comission}
        self.sales.append(sale)

    def calculate_comission(self, value, channel):
        standard_comission = 0.1 * value

        if channel == 'Online':
            comission = standard_comission * 0.8
        else:
            comission = standard_comission

        return comission


class SalespersonManagement:
    def __init__(self):
        self.salespersons = {}

    def add_salesperson(self, salesperson):
        self.salespersons[salesperson.cpf] = salesperson

    def get_salesperson(self, cpf):
        return self.salespersons.get(cpf)

    def update_salesperson(self, cpf, **kwargs):
        if cpf in self.salespersons:
            salesperson = self.salespersons[cpf]
            for key, value in kwargs.items():
                if hasattr(salesperson, key):
                    setattr(salesperson, key, value)

    def delete_salesperson(self, cpf):
        if cpf in self.salespersons:
            del self.salespersons[cpf]
