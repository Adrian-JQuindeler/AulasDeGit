public class Salutonmondo! {
	import Java.util.Scanner
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		
		
		System.out.println("Saluton mondo!");
        System.out.println("Digite a frase em esperanto? \n"
        		+ "[1] para bom\n"
        		+ "[2] para ruím\n");
        int resposta = sc.nextInt();
        if (resposta == 1) {
        	System.out.println("que bom que gostou, agradecemos a preferencia");
        }
        else if(resposta == 2){
        	System.out.println("Uma pena, vamos melhorar.");
	}
        else {
        	System.out.println("Número inválido");
        }
        sc.close();
        System.out.println("Volte sempre!!!");
	}

}
