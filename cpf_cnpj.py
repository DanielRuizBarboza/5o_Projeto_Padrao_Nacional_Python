from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos incorreta")


class DocCpf:
    def __init__(self, documento):
        if self.valida_cpf(documento):
            self.__cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def valida_cpf(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.__cpf)

    def __str__(self):
        return self.format_cpf()


class DocCnpj:
    def __init__(self, documento):
        if self.valida_cnpj(documento):
            self.__cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!")

    def valida_cnpj(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.__cnpj)

    def __str__(self):
        return self.format_cnpj()
