import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JCheckBoxMenuItem;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JRadioButtonMenuItem;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JToolBar;

public class java0602_JTooBar extends JFrame {
	public java0602_JTooBar() {
		setTitle("툴바");
		setSize(500,320);
		
		JToolBar filJToolBar = new JToolBar();
		filJToolBar.setFloatable(false);
//		filJToolBar.setFloatable(true); // true로 바꾸면 텨나옴
		filJToolBar.setOrientation(JToolBar.HORIZONTAL);
//		filJToolBar.setOrientation(JToolBar.VERTICAL); // VERTICAL로 바꾸면 세로됨
		JTextArea textarea = new JTextArea("여기에 내용이 표시됩니다.");
		String[][] btnData = {{"new.png", "새 파일", "새 파일 선택"},
				{"open.png", "파일 열기", "파일 열기 선택"},
				{"save.png", "파일 저장", "파일 저장 선택"}};
				
		for(int i=0; i<btnData.length ; i++) {
			String imgPath = btnData[i][0];
			String toolTip = btnData[i][1];
			String actionText = btnData[i][2];
			
			JButton btn = new JButton(new ImageIcon("ToolBar/"+imgPath));
			btn.setToolTipText(toolTip);
			btn.addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					textarea.setText(actionText);
				}
			});
			filJToolBar.add(btn);
		}
		
		add(filJToolBar, BorderLayout.NORTH);
		add(new JScrollPane(textarea), BorderLayout.CENTER);
		setVisible(true);
//		
	}
	
	public static void main(String[] args) {
		new java0602_JTooBar();
	}

}
