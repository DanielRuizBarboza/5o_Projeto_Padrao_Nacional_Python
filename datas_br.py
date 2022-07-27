from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def format_data(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def mes_cadastro(self):
        meses_do_ano = [
            "Janeiro","Fevereiro", "Março",
            "Abril", "Maio", "Junho", "Julho",
            "Agosto", "Setembro", "Outubro",
            "Novembro", "Dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dias_da_semana = [
            "Segunda-Feira", "Terça-Feira", "Quarta-Feira",
            "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"
        ]
        dia_cadastro = self.momento_cadastro.weekday()
        return dias_da_semana[dia_cadastro]

    def tempo_cadastro(self,):
        return datetime.today() - self.momento_cadastro
