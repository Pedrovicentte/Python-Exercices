from rich import print, inspect
from aluno import Aluno
from funcionario import Funcionario
from professor import Professor

def main():
    a1 = Aluno("José", 17, "Informática", "T01")
    a1.fazer_aniversário()
    a1.fazer_matricula()

    p1 = Professor("Samuel", 45, "Matématica", "Doutor")
    p1.dar_aula()

    f1 = Funcionario("Claudia", 29, "Secretária", "Financeiro")
    a1.fazer_aniversário()
    f1.bater_ponto()

    a1.estudar()
    p1.estudar()
    f1.estudar()
if __name__ == "__main__":
    main()