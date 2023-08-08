public class Motocicleta {

    String modelo;
    String marca;
    int nroChassi;
    String nroPlaca;
    String cor;
    int nroCilindradas;


    private String licenciar() {
        int tamanho = nroPlaca.length();
        String valor = nroPlaca.substring(tamanho - 1);
        int valorInt = Integer.parseInt(valor);
        switch (valorInt) {
            case 1:
                System.out.println("abril");
                break;
            case 2:
                System.out.println("maio");
                break;
            case 3:
                System.out.println("junho");
                break;
            case 4:
                System.out.println("julho");
                break;
            case 5:
                System.out.println("agosto");
                break;
            case 6:
                System.out.println("setembro");
                break;
            case 7:
                System.out.println("outubro");
                break;
            case 8:
                System.out.println("novembro");
                break;
            case 9:
                System.out.println("dezembro");
                break;
        }
        return marca;
    }
}

