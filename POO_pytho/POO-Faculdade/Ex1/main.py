from Pessoa import Pessoa 
from Professor import Professor
from Aluno import Aluno
from Curso import Curso
from Turma import Turma
from Disciplina import Disciplina

Prof1 = Professor ()
Prof2 = Professor ()

Aluno1 = Aluno()
Aluno2 = Aluno()
Aluno3 = Aluno()
Aluno4 = Aluno()

Curso1 = Curso()
Curso2 = Curso()
Curso3 = Curso()

Turma1 = Turma()
Turma2 = Turma()
Turma3 = Turma()

Prof1.set_nome("Carlos Silva")
Prof1.set_idProf(101)
Prof1.set_matriculaProf("MAT12345")

Prof2.set_nome("Ana Souza")
Prof2.set_idProf(202)
Prof2.set_matriculaProf("MAT67890")

Curso1.set_nomeCurso("Engenharia de Software")
Curso1.set_idCurso(1)

Curso2.set_nomeCurso("Ciência da Computação")
Curso2.set_idCurso(2)

Curso3.set_nomeCurso("Matemática")
Curso3.set_idCurso(3)

Aluno1.set_nome("João Pereira")
Aluno1.set_matricula("2023001")
Aluno1.set_cursosAluno([Curso1])

Aluno2.set_nome("Maria Oliveira")
Aluno2.set_matricula("2023002")
Aluno2.set_cursosAluno([Curso2])

Aluno3.set_nome("Pedro Santos")
Aluno3.set_matricula("2023003")
Aluno3.set_cursosAluno([Curso1, Curso2])

Aluno4.set_nome("Ana Costa")
Aluno4.set_matricula("2023004")
Aluno4.set_cursosAluno([Curso3])

Turma1.set_idTurma(501)
Turma1.set_disciplinaTurma("Programação Orientada a Objetos")
Turma1.setProfessorTurma(Prof1)
Turma1.set_alunosTurma([Aluno1, Aluno3])

Turma2.set_idTurma(502)
Turma2.set_disciplinaTurma("Cálculo I")
Turma2.setProfessorTurma(Prof2)
Turma2.set_alunosTurma([Aluno2, Aluno4])

Turma3.set_idTurma(503)
Turma3.set_disciplinaTurma("Lógica de Programação")
Turma3.setProfessorTurma(Prof1)
Turma3.set_alunosTurma([Aluno1, Aluno2, Aluno3])

