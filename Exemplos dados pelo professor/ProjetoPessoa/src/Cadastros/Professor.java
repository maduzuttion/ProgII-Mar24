package Cadastros;

public class Professor extends Pessoa{
	
	private double vlHora;
	private double qdHora;	

	public Professor (){
		System.out.println("Criando professor...");
	}

	public double getVlHora() {
		return vlHora;
	}

	public void setVlHora(double vlHora) {
		this.vlHora = vlHora;
	}

	public double getQdHora() {
		return qdHora;
	}

	public void setQdHora(double qdHora) {
		this.qdHora = qdHora;
	}
	
}