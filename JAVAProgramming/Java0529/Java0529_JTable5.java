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

public class Java0529_JTable5 extends JFrame {
	JTable jt;
	JButton edit = new JButton("수정");
	JButton cancel = new JButton("취소");
	JTextField[] txts = new JTextField[4];
	String[] colNm = {"사번","이름","근무부서", "나이"};
	
	public Java0529_JTable5() {
		setTitle("사원정보 테이블");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(750, 200);
		setLayout(new BorderLayout());
		
		JPanel table = new JPanel();
		JPanel input = new JPanel(new BorderLayout());
		JPanel txtsp = new JPanel(new GridLayout(4, 2, 5, 5));
		JPanel btnp = new JPanel(new GridLayout(1, 2));
		
		
		Object[][] data = {{"260001", "박길동", "총무부"},{"260002","이순신","관리부"},{"260003", "임꺽정", "보건복지관리부", "불혹의 장미"}, {"260004", "아버지", "부", "신형만과 동갑"}};
		DefaultTableModel dtm = new DefaultTableModel(data, colNm);
		
		jt = new JTable(dtm) {
			public boolean isCellEditable(int row, int column) {
				return false;
			}
		};
		
		jt.getSelectionModel().addListSelectionListener(new ListSelectionListener() {
			@Override
			public void valueChanged(ListSelectionEvent e) {
				for(int i=0 ; i < txts.length ; i++) {
					txts[i].setText(jt.getValueAt(jt.getSelectedRow(), i).toString());
				}
			}
		});
	
//		table.add(new JScrollPane(jt));
		JScrollPane jsp = new JScrollPane(jt);
		jsp.setPreferredSize(new Dimension(500,200));
		table.add(jsp);
		
		JLabel[] lbls = new JLabel[4];
		for(int i=0 ; i<txts.length ; i++) {
			lbls[i] = new JLabel(colNm[i]);
			txts[i] = new JTextField(10);
			txtsp.add(lbls[i]);
			txtsp.add(txts[i]);
			
		}
		
		
		edit.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				for(int i=0; i<txts.length; i++) {
					String updateValue = txts[i].getText();
					jt.setValueAt(updateValue, jt.getSelectedRow(), i);
				}
			}
		});
		
		cancel.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				for(int i=0; i<txts.length; i++) {
					dispose();
				}
			}
			
		});
		
		
		btnp.add(edit);
		btnp.add(cancel);
		input.add(txtsp, BorderLayout.NORTH); 
		input.add(btnp, BorderLayout.SOUTH); 
		add(table, BorderLayout.CENTER); 
		add(input, BorderLayout.EAST);
		setVisible(true);
		

//		add(new JScrollPane(jt));
	}
	
	public static void main(String[] args) {
		new Java0529_JTable5();
		
	}
}
