## Instruções de uso

1. Clone o repositório:
```
git clone https://github.com/arthurlorenzon/GerenciadorVendedores.git
```
2. Instale a biblioteca pandas:
```
pip install pandas
```
3. Importe as classes utilizadas no seu arquivo de teste:
```
from models import Salesperson, SalespersonManagement
```
4. Crie uma instância para gerencias os vendedores. Exemplo:
```
 management = SalespersonManagement()
```
5. Crie instâncias de vendedores utilizando os seguintes parâmentros: Nome, CPF (Formato padrão ou apenas números), Data de Nascimento (dd/mm/aaaa), Estado (UF). Exemplo:
```
salesperson1 = Salesperson("João", "111.111.111-11", "01/01/1990", "joao@joao.com", "SC")
salesperson2 = Salesperson("Maria", "22222222222", "02/02/1991", "maria@email.com", "PR")
```
6. Adicione os vendedores à instância do gerenciador. Exemplo:
```
management.add_salesperson(salesperson1)
management.add_salesperson(salesperson2)
```
7. Formate o cpf dos vendedores. Exemplo:
```
for cpf, vendedor in management.salespersons.items():
    vendedor.cpf = vendedor.format_cpf(vendedor.cpf)
```
8. Adicione vendas aos vendedores. Exemplo:
```
management.add_sale("111.111.111-11", 800, "Loja física")
management.add_sale("22222222222", 1000, "Loja física")
```
9. Exporte os dados para um arquivo excel. Exemplo:
```
manager.export_excel("nome_do_arquivo.xlsx")
```
10. Para receber as estatísticas de venda na tela, execute a função calculate_statistics(). Exemplo:
```
manager.calculate_statistics()
```
11. Utilizando o restante das funções:  
11.1. update_salesperson(cpf, **kwargs): Recebe como parâmetro o CPF do vendedor e os dados que serão alterados junto ao seu novo valor. Exemplo:
```
management.update_salesperson("111.111.111-11", name="João Modificado", email="joao@modificado.com", birth_date="11/12/2000", state="RS")
```
11.2. get_salesperson(cpf): Recebe como parâmetro o CPF e lê os dados do vendedor. Exemplo:
```
management.get_salesperson("111.111.111-11")
```
11.3. delete_salesperson(cpf): Recebe como parâmetro o CPF do vendedor e remove todos os seus dados. Exemplo:
```
management.delete_salesperson("111.111.111-11")
```
