package gestion_Notas;

import java.util.ArrayList;
import java.util.Scanner;
import java.io.IOException;

public class Software {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);
        // contar la cantidad de notas
        int tn = 0,c = 0;
        String n;
        double promedio = 0, suma = 0;

        ArrayList<String> notas = new ArrayList<>();
        
        do{
        
        // Limpiar consola
        try {
            if (System.getProperty("os.name").contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                new ProcessBuilder("clear").inheritIO().start().waitFor();
            }
        } catch (IOException | InterruptedException ex) {
            System.out.println("Error al limpiar la consola: " + ex.getMessage());
        }    


        // agregar notas al digitar
        System.out.println("Ingrese una calificacion o presione e para terminar el proceso"); // label
        n = teclado.next(); // input

        // Evitar agregar la e
        if(!n.equals("e")){
        notas.add(n);
        c=c++;
        }

        }while(!n.equals("e"));
        
        // Obtenemos la cantidad de notas ingresadas
        tn = notas.size();
        // Recorrer el arraylist y sumar las notas obtenidas
        for(int i = 0; i < tn ;i ++){
            suma += Double.parseDouble(notas.get(i));
        }

        // sacar el promedio
        promedio = suma/tn;
        System.out.println(promedio);
    }
}
