from PySimpleGUI import PySimpleGUI as sg
from calendar import monthrange
from datetime import date

# Layout
sg.theme('Default1')
layout = [
    [sg.Combo(['Salário p/hora', 'Salário p/dia', 'Salário p/mês', 'Salário p/ano'], default_value='Salário p/hora', key='combo', size=(15, 1)),
     sg.Input(key='salario', size=(15, 1)), ],
    [sg.Text('Carga horária', size=(15, 1)), sg.In(key='horas', size=(15, 1))],
    [sg.Checkbox('Converter para hora', key='boxhora', ), sg.Checkbox('Converter para dia', key='boxdia')],
    [sg.Checkbox('Converter para mês', key='boxmes'), sg.Check('Converter para ano', key='boxano')],
    [sg.Button('Calcular', key='calcular'), sg.Output(20, 5)]
]
# Janela
janela = sg.Window('Conversor de salário', layout)

# Valores


# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'calcular':
        if valores['horas'] != '':
            qnt_dias_mes = monthrange(date.today().year, date.today().month)[1]
            horas_de_trabalho = float(valores['horas'])
            if valores['combo'] == 'Salário p/hora':
                if valores['salario'] != '' and valores['horas'] != '':
                    salario_hora = float(valores['salario'])
                    if valores['boxhora']:
                        print(f'{salario_hora:.2f} R$ por hora')
                    if valores['boxdia']:
                        print(f'{salario_hora * horas_de_trabalho:.2f} R$ por dia')
                    if valores['boxmes']:
                        print(f'{(salario_hora * horas_de_trabalho) * qnt_dias_mes:.2f} R$ por mês')
                    if valores['boxano']:
                        print(f'{((salario_hora * horas_de_trabalho) * qnt_dias_mes) * 12:.2f} R$ por ano')
            if valores['combo'] == 'Salário p/dia':
                if valores['salario'] != '' and valores['horas'] != '':
                    salario_dia = float(valores['salario'])
                    if valores['boxhora']:
                        print(f'{salario_dia / horas_de_trabalho:.2f} RS por hora')
                    if valores['boxdia']:
                        print(f'{salario_dia:.2f} R$ por dia')
                    if valores['boxmes']:
                        print(f'{salario_dia * qnt_dias_mes:.2f} R$ por mês')
                    if valores['boxano']:
                        print(f'{(salario_dia * qnt_dias_mes) * 12:.2f} R$ por ano')
            if valores['combo'] == 'Salário p/mês':
                if valores['salario'] != '' and valores['horas'] != '':
                    salario_mensal = float(valores['salario'])
                    if valores['boxhora']:
                        print(f'{(salario_mensal / qnt_dias_mes) / horas_de_trabalho:.2f} R$ por hora')
                    if valores['boxdia']:
                        print(f'{salario_mensal / qnt_dias_mes:.2f} R$ por dia')
                    if valores['boxmes']:
                        print(f'{salario_mensal:.2f} R$ por mês')
                    if valores['boxano']:
                        print(f'{salario_mensal * 12:.2f} R$ por ano')
            if valores['combo'] == 'Salário p/ano':
                if valores['salario'] != '' and valores['horas'] != '':
                    salario_ano = float(valores['salario'])
                    if valores['boxhora']:
                        print(f'{((salario_ano / 12) / qnt_dias_mes) / horas_de_trabalho:.2f} R$ por hora')
                    if valores['boxdia']:
                        print(f'{(salario_ano / 12) / qnt_dias_mes:.2f} R$ por dia')
                    if valores['boxmes']:
                        print(f'{salario_ano / 12:.2f} R$ por mês')
                    if valores['boxano']:
                        print(f'{salario_ano} R$ por ano')
        else:
            print('Digite os campos corretamente')
