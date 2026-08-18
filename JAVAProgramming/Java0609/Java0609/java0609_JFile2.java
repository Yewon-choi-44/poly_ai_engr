import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.filechooser.FileNameExtensionFilter;

public class java0609_JFile2 extends JFrame{
	JTextArea tf = new JTextArea(5, 20);
	public java0609_JFile2() {
		setTitle("File 예제");
		setSize(350, 200);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new BorderLayout());
		tf.setFont(new Font("맑은 고딕", Font.PLAIN, 20)); //글자 너므 작으면 이거.
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
		
		saveItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JFileChooser chooser = new JFileChooser();
				FileNameExtensionFilter filter = new FileNameExtensionFilter("텍스트 파일(*.txt)", "txt");
				chooser.setFileFilter(filter);
				int ret = chooser.showSaveDialog(null);
				if (ret != JFileChooser.APPROVE_OPTION) {
					return;
				}
				File file = chooser.getSelectedFile();
				if(!file.getName().endsWith(".txt")) {
					file = new File(file.getAbsolutePath() + ".txt");
				}
				try {
					BufferedWriter bw = new BufferedWriter(new FileWriter(file));
					String cont = tf.getText();
					bw.write(cont);
					bw.close();
					JOptionPane.showMessageDialog(null, "파일이 정상적으로 저장되었습니다.");

				} catch(IOException io) {
					JOptionPane.showMessageDialog(null, "파일 저장 중 오류가 발생하였습니다.");
				}
			}
		});
		
		openItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JFileChooser chooser = new JFileChooser();
				FileNameExtensionFilter filter = new FileNameExtensionFilter("텍스트 파일(*.txt)","txt");
				chooser.setFileFilter(filter);
				int ret = chooser.showOpenDialog(null);
				if (ret != JFileChooser.APPROVE_OPTION) {
					return;
				}
				File file = chooser.getSelectedFile();
				try {
					tf.setText("");
					BufferedReader br = new BufferedReader(new FileReader(file));
					String line = "";
					while ((line = br.readLine()) != null) {
						tf.append(line + "\n");
					}
					br.close();
				} catch(IOException io) {
					JOptionPane.showMessageDialog(null, "파일을 읽어오는 중 오류가 발생하였습니다.");
				}
			}
		});
		
		fileMenu.add(saveItem);
		fileMenu.add(openItem);
		jmb.add(fileMenu);
		setJMenuBar(jmb);
	}
	
	public static void main(String[] args) {
		new java0609_JFile2();
	}
}
