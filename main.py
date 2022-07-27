from cpf_cnpj import Documento
from telefonesbr import TelefonesBr
from datas_br import DatasBr
from acesso_cep import Busca_Endereco
import requests


cep = "01001000"
telefone = "5595987831895"
cnpj = "35379838000112"
cpf = "71017332045"

objeto = Documento.cria_documento(cpf)
telefone_objeto = TelefonesBr(telefone)
cadastro = DatasBr()
objeto_cep = Busca_Endereco(cep)
r = requests.get("https://viacep.com.br/ws/01001000/json/").text

print(objeto)
print(telefone_objeto)
print(cadastro)
print(objeto_cep)

# Extrai informações do CEP via API
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)


