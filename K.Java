package comoprogramarjava.com;

public class Salutonmondo! {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		
		
		String frase = "Saluton mondo!";
        System.out.println("Digite a frase: " + frase);
        String frase2;
        frase2 = sc.nextLine();
        if (frase2 == frase) {
        	System.out.println("Você escreveu corretamente, parabéns!!!");
        }
        else {
        	System.out.println("Não era bem isso que você deveria escrever, tente novamente.");
	}
	}

}
