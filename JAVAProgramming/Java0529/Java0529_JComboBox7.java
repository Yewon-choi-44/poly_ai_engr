import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;
import javax.swing.JSlider;
import javax.swing.JTable;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.table.DefaultTableModel;

public class Java0529_JComboBox7 extends JFrame {
	JTable jt;
	public Java0529_JComboBox7() {
		setTitle("사원정보 테이블");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(600, 200);
		
		JTable jt;
		String[] colNm = {"사번", "이름", "근무부서"};
		Object[][] data = {{"260001", "박길동", "총무부"},{"260002","이순신","관리부"}};
		DefaultTableModel dtm = new DefaultTableModel(data, colNm);
		
		jt = new JTable(dtm) {
			public boolean isCellEditable(int row, int column) {
				return false;
			}
		};
			
		
		// 테이블 만들 때 정말 많이 쓰이는 메서드들임 알아둬야 함.
		dtm.addColumn("나이", new Object[] {30, "비밀"});
		dtm.addRow(new Object[] {"260004", "임꺽정", "홍보부", "많음"});
		dtm.insertRow(2,  new Object[] {"260003", "임길동", "총무부", "불혹의 장미"});
		dtm.removeRow(0);
		dtm.setRowCount(0);
		
		jt.getSelectionModel().addListSelectionListener(new ListSelectionListener() {
			@Override
			public void valueChanged(ListSelectionEvent e) {
				JTable jt = (JTable) e.getSource();
				System.out.println("행 " + jt.getSelectedRow());
				System.out.println("열 " + jt.getSelectedColumn());
				System.out.println("값 " + jt.getValueAt(jt.getSelectedRow(), jt.getSelectedColumn()));
			}
		});
	
		add(new JScrollPane(jt));
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new Java0529_JComboBox7();
		
	}
}
