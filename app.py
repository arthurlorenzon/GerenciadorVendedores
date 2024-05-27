from flask import Flask, request, jsonify, send_file
from models import Salesperson, SalespersonManagement
import pandas as pd

app = Flask(__name__)
management = SalespersonManagement()


@app.route('/vendedor', methods=['POST'])
def add_salesperson():
    data = request.json
    salesperson = Salesperson(
        data['name'], data['cpf'], data['birth_date'], data['email'], data['state'])
    management.add_salesperson(salesperson)
    return jsonify({'message': 'Vendedor adicionado com sucesso!'}), 201


@app.route('/vendedor/<cpf>', methods=['GET'])
def get_salesperson(cpf):
    salesperson = management.get_salesperson(cpf)
    if salesperson:
        return jsonify({
            'Nome do Vendedor': salesperson.name,
            'cpf': salesperson.cpf,
            'Data de nascimento': salesperson.birth_date,
            'E-mail': salesperson.email,
            'Estado (UF)': salesperson.state,
            'Vendas': salesperson.sales
        })
    return jsonify({'message': 'Vendedor não encontrado'}), 404


@app.route('/vendedor/<cpf>', methods=['PUT'])
def update_salesperson(cpf):
    data = request.json
    management.update_salesperson(cpf, **data)
    return jsonify({'message': 'Vendedor atualizado com sucesso!'})


@app.route('/vendedor/<cpf>', methods=['DELETE'])
def delete_salesperson(cpf):
    management.delete_salesperson(cpf)
    return jsonify({'message': 'Vendedor removido com sucesso!'})


@app.route('/exportar', methods=['GET'])
def export_excel():
    file_name = 'api_vendedores.xlsx'
    management.export_excel(file_name)
    return send_file(file_name, as_attachment=True)


@app.route('/estatisticas', methods=['GET'])
def calculate_statistics():
    sale_statistics = []
    for salesperson in management.salespersons.value():
        for sale in salesperson.sales:
            sale_statistics.append({
                'Nome do Vendedor': salesperson.name,
                'Estado': salesperson.state,
                'Valor': sale['valor'],
                'Canal': sale['canal']
            })
    df_sales = pd.DataFrame(sale_statistics)

    volume_per_channel = df_sales.groupby('Canal')['Valor'].sum().reset_index()
    average_per_channel = df_sales.groupby(['Canal', 'Nome do Vendedor'])[
        'Valor'].mean().reset_index()
    volume_per_state = df_sales.groupby('Estado')['Valor'].sum().reset_index()
    average_per_state = df_sales.groupby(['Estado', 'Nome do Vendedor'])[
        'Valor'].mean().reset_index()

    return jsonify({
        'Volume por Canal': volume_per_channel.to_dict(orient='records'),
        'Média por Canal': average_per_channel.to_dict(orient='records'),
        "Volume por Estado": volume_per_state.to_dict(orient='records'),
        "Média por Estado": volume_per_state.to_dict(orient='records')
    })


if __name__ == '__main__':
    app.run(debug=True)
