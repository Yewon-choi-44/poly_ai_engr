import java.awt.FlowLayout;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JList;
import javax.swing.JScrollPane;

public class java0526_JList extends JFrame{
	String[] fruits = {"apple", "banana", " kiwi", "mango","pear","peach","berry","strawberry", "blueberry"};
	ImageIcon[] imgs = {new ImageIcon("images/icon1.png"), new ImageIcon("images/icon2.png"),
						new ImageIcon("images/icon3.png"), new ImageIcon("images/icon4.png")};
	
	public java0526_JList() {
		setTitle("리스트 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		JList<String> list1 = new JList<String>(fruits);
		JList<ImageIcon> list2 = new JList<ImageIcon>(imgs);
		JList<String> list3 = new JList<String>(fruits);
		JScrollPane jsp = new JScrollPane(list3);
	
		add(list1);
		add(list2);
		add(jsp);
		
		setSize(300, 300);
		setVisible(true);
	}
	public static void main(String[] args) {
		new java0526_JList();
	}

}
