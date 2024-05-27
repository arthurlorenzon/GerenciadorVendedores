from models import SalespersonManagement, Salesperson


def main():
    # Criar uma instância da classe SalespersonManagement
    management = SalespersonManagement()

    # Cria instâncias da classe Salesperson
    salesperson1 = Salesperson("João", "111.111.111-11",
                               "01/01/1990", "joao@joao.com", "SC")

    salesperson2 = Salesperson("Maria", "222.222.222-22",
                               "02/02/1991", "maria@email.com", "PR")

    salesperson3 = Salesperson("José", "333.333.333-33",
                               "03/03/1991", "jose@jose.com", "SP")

    salesperson4 = Salesperson("Júlia", "444.444.444-44", "04/04/1994",
                               "julia@julia.com", "RS")

    salesperson5 = Salesperson("Marcos", "55555555555", "04/04/1994",
                               "marcos@marcos.com", "SC")

    # Adiciona os vendedores à instância da classe SalespersonManagement
    management.add_salesperson(salesperson1)
    management.add_salesperson(salesperson2)
    management.add_salesperson(salesperson3)
    management.add_salesperson(salesperson4)
    management.add_salesperson(salesperson5)

    # Adiciona vendas realizadas pelos vendedores
    management.add_sale("111.111.111-11", 800, "Loja física")
    management.add_sale("222.222.222-22", 1000, "Loja física")
    management.add_sale("333.333.333-33", 1200, "Online")
    management.add_sale("444.444.444-44", 500, "Online")
    management.add_sale("111.111.111-11", 1000, "Online")
    management.add_sale("333.333.333-33", 600, "Loja física")
    management.add_sale("222.222.222-22", 1500, "Online")
    management.add_sale("444.444.444-44", 20000, "Online")
    management.add_sale("55555555555", 20000, "Online")

    # Formata o CPF de todos os vendedores incluídos no gerenciamento
    for cpf, vendedor in management.salespersons.items():
        vendedor.cpf = vendedor.format_cpf(vendedor.cpf)

    # Exporta os dados dos vendedores para um arquivo Excel
    management.export_excel('vendedores.xlsx')

    # Calcula e exibe estatísticas de venda na tela
    management.calculate_statistics()


if __name__ == "__main__":
    main()
