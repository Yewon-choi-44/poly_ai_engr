import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JCheckBox;
import javax.swing.JCheckBoxMenuItem;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JRadioButtonMenuItem;

public class java0602_JMenu7 extends JFrame {
	public java0602_JMenu7() {
		setTitle("Menu 만들기 예제");
		setSize(300,200);
		
		JMenuBar jmb = new JMenuBar();
		JMenu jm= new JMenu("색상");
		String[] menuTxts = {"Load", "Hide", "Reshow", "Exit"};
		
		ImageIcon Img3 = new ImageIcon("images/image3.jpg"); 
		JLabel imgLbl = new JLabel(Img3);
		
		
		JMenuItem[] menusItems = new JMenuItem[menuTxts.length];
		for (int i = 0; i<menusItems.length; i++) {
			int idx = i;
			menusItems[i] = new JMenuItem(menuTxts[i]);
			menusItems[i].addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					if(menusItems[idx].getText() == "Load") {
						imgLbl.setIcon(Img3);
					} else if(menusItems[idx].getText() == "Hide") {
						imgLbl.setVisible(false);
					} else if(menusItems[idx].getText() == "Reshow") {
						imgLbl.setVisible(true);
					} else if(menusItems[idx].getText() == "Exit") {
						dispose();
					}
				}
			});
			jm.add(menusItems[i]);
			}
		
		add(imgLbl);
		jmb.add(jm);
		setJMenuBar(jmb);
		setVisible(true);
//		
	}
	
	public static void main(String[] args) {
		new java0602_JMenu7();
	}

}
