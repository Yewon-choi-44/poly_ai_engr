import javax.swing.JButton;
import javax.swing.JFrame;

public class Java0522_SecondSwing extends JFrame{
	public Java0522_SecondSwing() {
		setTitle("Null Sample");
		setSize(300, 200);
		setLayout(null);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JButton btns[] = new JButton[9];
		for(int i=0 ; i < btns.length ; i++) {
			btns[i] = new JButton(Integer.toString(i+1));
			btns[i].setBounds(i*15  , i*35, 100, 30);
			add(btns[i]);
		}
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new Java0522_SecondSwing();
	}

}
