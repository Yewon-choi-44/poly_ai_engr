import javax.swing.JCheckBox;
import javax.swing.JCheckBoxMenuItem;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JRadioButtonMenuItem;

public class java0602_JMenu3 extends JFrame {
	public java0602_JMenu3() {
		setTitle("Menu 만들기 예제");
		setSize(300,200);
		
		JMenuBar jmb = new JMenuBar();
		String[] menuTxts = {"Menu", "OtherMenu"};
		JMenu[] menus = new JMenu[menuTxts.length];
		for (int i = 0; i<menus.length; i++) {
			menus[i] = new JMenu(menuTxts[i]);
			if(i == 1) {
				menus[0].add(menus[i]);
			} else {
				jmb.add(menus[i]);
		}
			}
		
		JMenuItem jmi1 = new JMenuItem("sub1");
		JMenuItem jmi2 = new JMenuItem("sub2");
		menus[1].add(jmi1);
		menus[1].add(jmi2);
		
		JCheckBoxMenuItem jcmi = new JCheckBoxMenuItem("CheckBox");
		JRadioButtonMenuItem jrmi = new JRadioButtonMenuItem("RadioButton");
		menus[2].add(jcmi);
		menus[2].add(jrmi);
		
		setJMenuBar(jmb);
		setVisible(true);
//		
//		String[] itemTxts = {"Load", "Hide", "Reshow", "Exit"};
//		JMenuItem[] menuItems = new JMenuItem[itemTxts.length];
//		for (int i = 0; i<menus.length; i++) {
//			menuItems[i] = new JMenuItem(menuTxts[i]);
//			menus[0].add(menuItems[i]);
//			if(i==2) {
//				menus[0].addSeparator();
//			}
//		}
		
//		JMenu screeM = new JMenu("Screen"); 
//		JMenu editM = new JMenu("Edit"); 
//		JMenu sourceM = new JMenu("Source"); 
//		JMenu projectM = new JMenu("Project"); 
//		JMenu runM = new JMenu("Run"); 
//		
	}
	
	public static void main(String[] args) {
		new java0602_JMenu3();
	}

}
