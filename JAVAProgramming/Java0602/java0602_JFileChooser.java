import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.filechooser.FileNameExtensionFilter;

public class java0602_JFileChooser extends JFrame{
	JLabel displaylbl = new JLabel("메뉴로 Open", JLabel.CENTER);
//	JFileChooser chooser;
	public java0602_JFileChooser() {
		setTitle("Menu Jfile");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setSize(350, 200);
		
		JMenuBar jmb = new JMenuBar();
		JMenu file = new JMenu("File");
		JMenuItem open = new JMenuItem("Open");
		JMenuItem cancel = new JMenuItem("Cancel");
		
		open.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				JFileChooser filechooser = new JFileChooser();
				FileNameExtensionFilter filter = new FileNameExtensionFilter("JPG 파일", "jpg");
				filechooser.setFileFilter(filter);
				int selectedfile = filechooser.showOpenDialog(null);
				if(selectedfile != JFileChooser.APPROVE_OPTION) {
					JOptionPane.showMessageDialog(null, "파일을 선택하지 않았습니다.", "경고", JOptionPane.WARNING_MESSAGE);
					return;
				}
				String filepath = filechooser.getSelectedFile().getPath();
				displaylbl.setText(null);
				displaylbl.setIcon(new ImageIcon(filepath));
			}
		});
		
		cancel.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				displaylbl.setText("메뉴로 오픈");
				displaylbl.setIcon(null);
				setSize(350, 200);
			}
		});
	
		
		add(displaylbl);
		file.add(open);
		file.add(cancel);
		jmb.add(file);
		setJMenuBar(jmb);
		setVisible(true);

	}
	
	public static void main(String[] args) {
		new java0602_JFileChooser();
	}

}
