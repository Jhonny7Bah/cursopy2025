from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

valor_emprestado = 1_000_000
#pagamento em 5 anos
data_do_emprestimo = datetime(2020, 12, 20)
print(data_do_emprestimo)
data_final_do_emprestimo = data_do_emprestimo + relativedelta(years=5)
pagamento_mensal = valor_emprestado / 60 #60 é a quantidade de meses que tem em 5 anos.

#iteração para cada mês
for mes in range(1,61):
      data_mensal = data_do_emprestimo + relativedelta(months=mes)
      print(f'''Parcela {mes}: 
            Valor: R${pagamento_mensal:,.2f}
            Data de Vencimento: {data_mensal.strftime('%d/%m/%Y')}
      {'-'*100}
            ''')