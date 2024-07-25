package Cadastros;

public class Aluno extends Pessoa{
	private int  cdCurso;
	private char idAtivo;	

	public Aluno (){
		System.out.println("Criando aluno...");
	}

	public int getCdCurso() {
		return cdCurso;
	}

	public void setCdCurso(int cdCurso) {
		this.cdCurso = cdCurso;
	}

	public char getIdAtivo() {
		return idAtivo;
	}

	public void setIdAtivo(char idAtivo) {
		this.idAtivo = idAtivo;
	}

	
}
