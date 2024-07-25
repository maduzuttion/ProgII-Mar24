package Cadastros;

public class Pessoa {
	private int cdCadastro;
	private char idFisicaJuridica;
	private String dsCpfCnpj;
	private boolean idAtivo;
	private String dsNome;
	private char idEstadoCivil;
	private String dsEmail;

	public Pessoa (){
		System.out.println("Criando pessoa...");
	}

	public int getCdCadastro() {
		return cdCadastro;
	}

	public void setCdCadastro(int cdCadastro) {
		this.cdCadastro = cdCadastro;
	}

	public char getIdFisicaJuridica() {
		return idFisicaJuridica;
	}

	public void setIdFisicaJuridica(char idFisicaJuridica) {
		this.idFisicaJuridica = idFisicaJuridica;
	}

	public String getDsCpfCnpj() {
		return dsCpfCnpj;
	}

	public void setDsCpfCnpj(String dsCpfCnpj) {
		this.dsCpfCnpj = dsCpfCnpj;
	}

	public boolean isIdAtivo() {
		return idAtivo;
	}

	public void setIdAtivo(boolean idAtivo) {
		this.idAtivo = idAtivo;
	}

	public String getDsNome() {
		return dsNome;
	}

	public void setDsNome(String dsNome) {
		this.dsNome = dsNome;
	}

	public char getIdEstadoCivil() {
		return idEstadoCivil;
	}

	public void setIdEstadoCivil(char idEstadoCivil) {
		this.idEstadoCivil = idEstadoCivil;
	}

	public String getDsEmail() {
		return dsEmail;
	}

	public void setDsEmail(String dsEmail) {
		this.dsEmail = dsEmail;
	}
	
}