import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;

public class java0602_JMenu2 extends JFrame {
	public java0602_JMenu2() {
		setTitle("Menu 만들기 예제");
		setSize(300,200);
		
		JMenuBar jmb = new JMenuBar();
		String[] menuTxts = {"Menu", "OtherMenu"};
		JMenu[] menus = new JMenu[menuTxts.length];
		for (int i = 0; i<menus.length; i++) {
			menus[i] = new JMenu(menuTxts[i]);
			jmb.add(menus[i]);
					
		}
		
		JMenuItem jmi1 = new JMenuItem("sub");
		menus[0].add(jmi1);
		
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
		new java0602_JMenu2();
	}

}
