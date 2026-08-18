import java.awt.BorderLayout;

import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

public class java0609_JFile extends JFrame{
	JTextArea tf = new JTextArea(5, 20);
	public java0609_JFile() {
		setTitle("File 예제");
		setSize(350, 200);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new BorderLayout());
		createMenu();
//		add(tf, BorderLayout.CENTER);
		add(new JScrollPane(tf), BorderLayout.CENTER); // 이거 있으면 스크롤도 생긴다함 참고
		setVisible(true);
	}
	
	private void createMenu() {
		JMenuBar jmb = new JMenuBar();
		JMenu fileMenu = new JMenu("File");
		JMenuItem saveItem = new JMenuItem("Save");
		JMenuItem openItem = new JMenuItem("Open");
		fileMenu.add(saveItem);
		fileMenu.add(openItem);
		jmb.add(fileMenu);
		setJMenuBar(jmb);
	}
	
	public static void main(String[] args) {
		new java0609_JFile();
	}

}
