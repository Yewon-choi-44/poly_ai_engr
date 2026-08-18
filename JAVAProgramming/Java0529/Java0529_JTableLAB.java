import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSlider;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.table.DefaultTableModel;

public class Java0529_JTableLAB extends JFrame {
	JTable jt;
	JButton addbtn = new JButton("추가");
	JButton delbtn = new JButton("취소");
	JTextField[] txts = new JTextField[3];
	String[] colNm = {"사번","이름","근무부서"};
	
	public Java0529_JTableLAB() {
		setTitle("사원정보 테이블");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(750, 600);
		setLayout(new BorderLayout());
		
		JPanel table = new JPanel();
		JPanel input = new JPanel();
		
		Object[][] data = {};
		DefaultTableModel dtm = new DefaultTableModel(data, colNm);
		
		jt = new JTable(dtm) {
			public boolean isCellEditable(int row, int column) {
				return false;
			}
		};

		
		JScrollPane jsp = new JScrollPane(jt);
		jsp.setPreferredSize(new Dimension(750,500));
		table.add(jsp);
		
		JLabel[] lbls = new JLabel[3];
		for(int i=0 ; i<txts.length ; i++) {
			lbls[i] = new JLabel(colNm[i]);
			txts[i] = new JTextField(10);
			input.add(lbls[i]);
			input.add(txts[i]);
			
		}
		
		
		addbtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
//				dtm.addRow(new Object[] {txts[0].getText(), txts[1].getText(), txts[2].getText()});
				Object[] addData = new Object[txts.length];
				for(int i=0; i<txts.length ; i++) {
					addData[i] = txts[i].getText();
				}
				dtm.addRow(addData);
			}
		});
		
		delbtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int selectRow = jt.getSelectedRow();
				
				if(selectRow != -1) {
					dtm.removeRow(selectRow);
				}
			}
		});
		
		
		input.add(addbtn);
		input.add(delbtn);
		add(table, BorderLayout.CENTER); 
		add(input, BorderLayout.NORTH);
		setVisible(true);
		

//		add(new JScrollPane(jt));
	}
	
	public static void main(String[] args) {
		new Java0529_JTableLAB();
		
	}
}
