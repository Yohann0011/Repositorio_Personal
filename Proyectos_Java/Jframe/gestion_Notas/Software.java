package gestion_Notas;

import java.awt.Color;

//librería de interfaz swing.JFrame
import javax.swing.JFrame;
import javax.swing.JPanel;

//Realizar herencia de la clase Jframe con = extends JFrame
public class Software extends JFrame{

    //Clase Principal
    public static void main(String[] args) {
        //Instanciamos la Ventana
        Software v1 = new Software();
        //Hacemos visible la ventana
        v1.setVisible(true);
    }

    //constructor - ventana
    public Software(){
        //Establecemos el tamaño de la ventana tamaño de la ventana
        this.setSize(640, 480);
        //finalizar el proceso al clicar en cerrar
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        // Titulo de ventana
        this.setTitle("Gestión de Notas");
        //Posición de la ventana - Centrar la ventana
        this.setLocationRelativeTo(this);
        //Llamar a Elementos
        elementos();
    }

    private void elementos(){
        JPanel fondo = new JPanel();
        //Establecer color de Fondo
        fondo.setBackground(Color.DARK_GRAY);
        //Agregar el panel
        this.getContentPane().add(fondo);
        
    }
}

