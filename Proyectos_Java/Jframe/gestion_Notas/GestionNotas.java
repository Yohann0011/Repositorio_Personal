package gestion_Notas;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.util.HashMap;

public class GestionNotas extends JFrame {
    private JTextField txtCalificacion;
    private JComboBox<String> comboTrabajos;
    private JTextField txtPorcentaje;
    private JTable tablaCalificaciones;
    private DefaultTableModel modeloTabla;
    private HashMap<String, Double> tiposTrabajo;

    public GestionNotas() {
        setTitle("Gestión de Notas");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        // Inicializar componentes
        tiposTrabajo = new HashMap<>();
        inicializarTiposTrabajo();

        JPanel panelSuperior = new JPanel(new GridLayout(2, 1));
        JPanel panelIngreso = new JPanel();
        JPanel panelBotones = new JPanel();

        txtCalificacion = new JTextField(5);
        comboTrabajos = new JComboBox<>(tiposTrabajo.keySet().toArray(new String[0]));
        txtPorcentaje = new JTextField(5);
        txtPorcentaje.setEditable(false);

        // Actualizar el porcentaje al seleccionar en el combo
        comboTrabajos.addActionListener(e -> {
            String tipoSeleccionado = (String) comboTrabajos.getSelectedItem();
            txtPorcentaje.setText(String.valueOf(tiposTrabajo.get(tipoSeleccionado)));
        });

        JButton btnAgregar = new JButton("Agregar");
        JButton btnEditar = new JButton("Editar Porcentaje");
        JButton btnCalcular = new JButton("Calcular Promedio");

        // Modelo de la tabla
        modeloTabla = new DefaultTableModel(new String[]{"Calificación", "Trabajo", "Porcentaje"}, 0);
        tablaCalificaciones = new JTable(modeloTabla);

        // Agregar calificación
        btnAgregar.addActionListener(e -> agregarCalificacion());

        // Editar porcentaje
        btnEditar.addActionListener(e -> editarPorcentaje());

        // Calcular promedio
        btnCalcular.addActionListener(e -> calcularPromedio());

        // Ensamblar panel superior
        panelIngreso.add(new JLabel("Calificación:"));
        panelIngreso.add(txtCalificacion);
        panelIngreso.add(new JLabel("Trabajo:"));
        panelIngreso.add(comboTrabajos);
        panelIngreso.add(new JLabel("Porcentaje:"));
        panelIngreso.add(txtPorcentaje);

        panelBotones.add(btnAgregar);
        panelBotones.add(btnEditar);
        panelBotones.add(btnCalcular);

        panelSuperior.add(panelIngreso);
        panelSuperior.add(panelBotones);

        // Agregar componentes al JFrame
        add(panelSuperior, BorderLayout.NORTH);
        add(new JScrollPane(tablaCalificaciones), BorderLayout.CENTER);
    }

    private void inicializarTiposTrabajo() {
        tiposTrabajo.put("Parcial", 20.0);
        tiposTrabajo.put("Laboratorios", 15.0);
        tiposTrabajo.put("Talleres", 10.0);
        // Actualizar combo box
        if (comboTrabajos != null) {
            comboTrabajos.setModel(new DefaultComboBoxModel<>(tiposTrabajo.keySet().toArray(new String[0])));
        }
    }

    private void agregarCalificacion() {
        try {
            double calificacion = Double.parseDouble(txtCalificacion.getText());
            String trabajo = (String) comboTrabajos.getSelectedItem();
            double porcentaje = tiposTrabajo.get(trabajo);

            // Agregar a la tabla
            modeloTabla.addRow(new Object[]{calificacion, trabajo, porcentaje});
            txtCalificacion.setText("");
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Ingrese una calificación válida", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void editarPorcentaje() {
        String trabajo = (String) comboTrabajos.getSelectedItem();
        String nuevoPorcentajeStr = JOptionPane.showInputDialog(this, 
                "Ingrese el nuevo porcentaje para " + trabajo, 
                tiposTrabajo.get(trabajo));
        try {
            double nuevoPorcentaje = Double.parseDouble(nuevoPorcentajeStr);
            tiposTrabajo.put(trabajo, nuevoPorcentaje);
            txtPorcentaje.setText(String.valueOf(nuevoPorcentaje));
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Ingrese un porcentaje válido", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void calcularPromedio() {
        double sumaPonderada = 0;
        double sumaPesos = 0;

        for (int i = 0; i < modeloTabla.getRowCount(); i++) {
            double calificacion = (double) modeloTabla.getValueAt(i, 0);
            double porcentaje = (double) modeloTabla.getValueAt(i, 2);

            sumaPonderada += calificacion * (porcentaje / 100);
            sumaPesos += porcentaje;
        }

        if (sumaPesos == 100) {
            JOptionPane.showMessageDialog(this, "El promedio ponderado es: " + sumaPonderada);
        } else {
            JOptionPane.showMessageDialog(this, 
                    "La suma de los porcentajes no es 100%. Revise los porcentajes.", 
                    "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new GestionNotas().setVisible(true));
    }
}
