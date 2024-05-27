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

    def add_sale(self, cpf, valor, channel):
        if cpf in self.salespersons:
            salesperson = self.salespersons[cpf]
            salesperson.add_sale(valor, channel)

    def export_excel(self, file_name):
        salesperson_data = {
            'Nome do Vendedor': [],
            'CPF': [],
            'Data de Nascimento': [],
            'E-mail': [],
            'Estado (UF)': []
        }

        sales_data = {
            'Nome do Vendedor': [],
            'CPF': [],
            'Estado (UF)': [],
            'Valor da Venda': [],
            'Canal da Venda': [],
            'Comissão': []
        }

        payments_data = {
            'Nome do Vendedor': [],
            'Comissão': []
        }

        for salesperson in self.salespersons.values():
            salesperson_data['Nome do Vendedor'].append(salesperson.name)
            salesperson_data['CPF'].append(salesperson.cpf)
            salesperson_data['Data de Nascimento'].append(
                salesperson.birth_date)
            salesperson_data['E-mail'].append(salesperson.email)
            salesperson_data['Estado (UF)'].append(salesperson.state)

            total_comission = 0

            for sale in salesperson.sales:
                sales_data['Nome do Vendedor'].append(salesperson.name)
                sales_data['CPF'].append(salesperson.cpf)
                sales_data['Estado (UF)'].append(salesperson.state)
                sales_data['Valor da Venda'].append(sale['valor'])
                sales_data['Canal da Venda'].append(sale['canal'])
                sales_data['Comissão'].append(sale['comissao'])

                total_comission += sale['comissao']

            if total_comission >= 1000:
                total_comission *= 0.9

            payments_data['Nome do Vendedor'].append(salesperson.name)
            payments_data['Comissão'].append(total_comission)

        with pd.ExcelWriter(file_name) as writer:
            df_salespersons = pd.DataFrame(salesperson_data)
            df_sales = pd.DataFrame(sales_data)
            df_payments = pd.DataFrame(payments_data)
            df_salespersons.to_excel(writer, index=False,
                                     sheet_name='Vendedores')
            df_sales.to_excel(writer, index=False, sheet_name='Vendas')
            df_payments.to_excel(writer, index=False,
                                 sheet_name='Pagamentos')

    def calculate_statistics(self):
        sale_statistics = []

        for salesperson in self.salespersons.values():
            for sale in salesperson.sales:
                sale_statistics.append({
                    'Nome do Vendedor': salesperson.name,
                    'Estado': salesperson.state,
                    'Valor': sale['valor'],
                    'Canal': sale['canal']
                })

        df_sales = pd.DataFrame(sale_statistics)

        volume_per_channel = df_sales.groupby(
            'Canal')['Valor'].sum().reset_index()
        average_per_channel = df_sales.groupby(['Canal', 'Nome do Vendedor'])[
            'Valor'].mean().reset_index()
        volume_per_state = df_sales.groupby(
            'Estado')['Valor'].sum().reset_index()
        average_per_state = df_sales.groupby(['Estado', 'Nome do Vendedor'])[
            'Valor'].mean().reset_index()

        print("Volume de vendas por canal:")
        print(volume_per_channel)
        print("\nMédia de vendas por canal:")
        print(average_per_channel)
        print("\nVolume de vendas por estado:")
        print(volume_per_state)
        print("\nMédia de vendas por estado:")
        print(average_per_state)
