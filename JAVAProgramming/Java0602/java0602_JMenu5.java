import javax.swing.JCheckBox;
import javax.swing.JCheckBoxMenuItem;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JRadioButtonMenuItem;

public class java0602_JMenu5 extends JFrame {
	public java0602_JMenu5() {
		setTitle("Menu 만들기 예제");
		setSize(300,200);
		
		JMenuBar jmb = new JMenuBar();
		JMenu jm= new JMenu("색상");
		String[] menuTxts = {"빨강", "노랑", "파랑", "닫기"};
		JMenuItem[] menusItems = new JMenu[menuTxts.length];
		for (int i = 0; i<menusItems.length; i++) {
			menusItems[i] = new JMenu(menuTxts[i]);
			jm.add(menusItems[i]);
			}
		
		jmb.add(jm);
		setJMenuBar(jmb);
		setVisible(true);
//		
	}
	
	public static void main(String[] args) {
		new java0602_JMenu5();
	}

}
