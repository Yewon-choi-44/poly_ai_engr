import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JCheckBox;
import javax.swing.JCheckBoxMenuItem;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JRadioButtonMenuItem;

public class java0602_JMenu4 extends JFrame {
	public java0602_JMenu4() {
		setTitle("Menu 만들기 예제");
		setSize(300,200);
		
		JMenuBar jmb = new JMenuBar();
		JMenu jm= new JMenu("색상");
		String[] menuTxts = {"빨강", "노랑", "파랑", "닫기"};
		JMenuItem[] menusItems = new JMenu[menuTxts.length];
		for (int i = 0; i<menusItems.length; i++) {
			int idx = i;
			menusItems[i] = new JMenu(menuTxts[i]);
			menusItems[i].addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					if(menusItems[idx].getText() == "닫기") {
						dispose();
					} else {
						
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
		new java0602_JMenu4();
	}

}
