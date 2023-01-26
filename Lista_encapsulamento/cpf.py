
cpf = 111444777
class Cpf:
    def cpf_eh_Valido(self, documento):
        if len(cpf) != 11:
            return False
            print("cpf inválido")
        else:
            fatia_um = cpf[:3]

