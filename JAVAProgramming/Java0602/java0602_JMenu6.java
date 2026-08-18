import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JCheckBox;
import javax.swing.JCheckBoxMenuItem;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JRadioButtonMenuItem;

public class java0602_JMenu6 extends JFrame {
	public java0602_JMenu6() {
		setTitle("Menu 만들기 예제");
		setSize(300,200);
		
		JMenuBar jmb = new JMenuBar();
		JMenu jm= new JMenu("색상");
		String[] menuTxts = {"빨강", "노랑", "파랑", "닫기"};
		Color[] colors = { Color.RED, Color.YELLOW, Color.BLUE};
		JMenuItem[] menusItems = new JMenuItem[menuTxts.length];
		for (int i = 0; i<menusItems.length; i++) {
			int idx = i;
			menusItems[i] = new JMenuItem(menuTxts[i]);
			menusItems[i].addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					if(menusItems[idx].getText() == "닫기") {
						dispose();
					} 
					else if(menusItems[idx].getText() == "빨강") {
						getContentPane().setBackground(Color.RED);
					}
					else if(menusItems[idx].getText() == "노랑") {
						getContentPane().setBackground(Color.YELLOW);
					}
					else if(menusItems[idx].getText() == "파랑") {
						getContentPane().setBackground(Color.BLUE);
					}
					else {
						getContentPane().setBackground(Color.RED);
					}
				}
			});
			jm.add(menusItems[i]);
			}
		
		jmb.add(jm);
		setJMenuBar(jmb);
		setVisible(true);
//		
	}
	
	public static void main(String[] args) {
		new java0602_JMenu6();
	}

}
