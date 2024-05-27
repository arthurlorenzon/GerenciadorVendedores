import pytest
from models import Salesperson, SalespersonManagement


def test_salesperson_incialization_with_cpf_format_standard():
    salesperson = Salesperson(
        name="João Silva",
        cpf="123.456.789-00",
        birth_date="10/10/2000",
        email="joao@joao.com",
        state="SC"
    )

    assert salesperson.name == "João Silva"
    assert salesperson.cpf == "123.456.789-00"
    assert salesperson.birth_date == "10/10/2000"
    assert salesperson.email == "joao@joao.com"
    assert salesperson.state == "SC"


def test_salesperson_inicialization_with_cpf_format_just_numbers():
    salesperson = Salesperson(
        name="João Silva",
        cpf="12345678900",
        birth_date="10/10/2000",
        email="joao@joao.com",
        state="SC"
    )

    assert salesperson.name == "João Silva"
    assert salesperson.cpf == "12345678900"
    assert salesperson.birth_date == "10/10/2000"
    assert salesperson.email == "joao@joao.com"
    assert salesperson.state == "SC"


def test_invalid_cpf_number_of_digits():
    with pytest.raises(ValueError):
        Salesperson(
            name="João Silva",
            cpf="123.456.789-0",
            birth_date="10/10/2000",
            email="joao@joao.com",
            state="SC"
        )


def test_invalid_cpf_due_values():
    with pytest.raises(ValueError):
        Salesperson(
            name="João Silva",
            cpf="123.456.789-aa",
            birth_date="10/10/2000",
            email="joao@joao.com",
            state="SC"
        )


def test_invalid_email_due_format():
    with pytest.raises(ValueError):
        Salesperson(
            name="João Silva",
            cpf="123.456.789-00",
            birth_date="10/10/2000",
            email="joao@.com",
            state="SC"
        )


def test_invalid_birth_date_due_format():
    with pytest.raises(ValueError):
        Salesperson(
            name="João Silva",
            cpf="123.456.789-00",
            birth_date="10-10-2000",
            email="joao@joao.com",
            state="SC"
        )


def test_invalid_birth_date_due_values():
    with pytest.raises(ValueError):
        Salesperson(
            name="João Silva",
            cpf="123.456.789-00",
            birth_date="32-13-2000",
            email="joao@joao.com",
            state="SC"
        )


def test_calculate_comission():
    salesperson = Salesperson(
        name="João Silva",
        cpf="123.456.789-00",
        birth_date="10/10/2000",
        email="joao@joao.com",
        state="SC"
    )

    comission_online = salesperson.calculate_comission(1000, "Online")
    assert comission_online == 80.0

    comission_standard = salesperson.calculate_comission(1000, "Loja física")
    assert comission_standard == 100.0


def test_add_salesperson():
    management = SalespersonManagement()
    salesperson = Salesperson(
        name="João Silva",
        cpf="123.456.789-00",
        birth_date="10/10/2000",
        email="joao@joao.com",
        state="SC"
    )
    management.add_salesperson(salesperson)
    assert management.get_salesperson(salesperson.cpf) == salesperson


def test_update_salesperson():
    management = SalespersonManagement()
    salesperson = Salesperson(
        name="João Silva",
        cpf="123.456.789-00",
        birth_date="10/10/2000",
        email="joao@joao.com",
        state="SC"
    )
    management.add_salesperson(salesperson)

    management.update_salesperson(
        "123.456.789-00", name="João Modificado", email="joao@modificado.com", birth_date="11/12/2000", state="RS")
    updated_salesperson = management.get_salesperson("123.456.789-00")
    assert updated_salesperson.name == "João Modificado"
    assert updated_salesperson.email == "joao@modificado.com"
    assert updated_salesperson.birth_date == "11/12/2000"
    assert updated_salesperson.state == "RS"


def test_delete_salesperson():
    management = SalespersonManagement()
    salesperson = Salesperson(
        name="João Silva",
        cpf="123.456.789-00",
        birth_date="10/10/2000",
        email="joao@joao.com",
        state="SC"
    )
    management.add_salesperson(salesperson)

    management.delete_salesperson("123.456.789-00")
    assert management.get_salesperson("123.456.789-00") is None
