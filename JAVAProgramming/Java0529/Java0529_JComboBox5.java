import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JSlider;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class Java0529_JComboBox5 extends JFrame {
	JLabel colorlbl =new JLabel();
	JSlider[] sl = new JSlider[3];
	
	public Java0529_JComboBox5() {
		setTitle("슬라이더");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(new FlowLayout());
		
		colorlbl.setText("color RGB");
		colorlbl.setPreferredSize(new Dimension(200,50));
		for(int i = 0; i< sl.length; i++) {
			sl[i] = new JSlider(JSlider.HORIZONTAL, 0, 255, 128);
			sl[i].setPaintLabels(true);
			sl[i].setPaintTicks(true);
			sl[i].setPaintTrack(true);
			sl[i].setMajorTickSpacing(50);
			sl[i].setMinorTickSpacing(10);
			
			sl[i].addChangeListener(new ChangeListener() {
				@Override
				public void stateChanged(ChangeEvent e) {
					int r = sl[0].getValue();
					int g = sl[1].getValue();
					int b = sl[2].getValue();
					colorlbl.setText("color R" + r + " G" + g + " B" + b);
					colorlbl.setBackground(new Color(r,g,b));
				}
			});
			
			add(sl[i]);
		}
		
		add(colorlbl);
		
	}
	public static void main(String[] args) {
		new Java0529_JComboBox5();
		
	}
}
