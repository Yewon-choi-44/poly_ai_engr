import java.sql.Statement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

public class jdbc0609_connection {
	public static void main(String[] args) {
		try {
			Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/madang", "root", "#mysql123");
//			System.out.println("성공");
			Statement stmt = conn.createStatement();
			ResultSet res = stmt.executeQuery("select * from book");
			
			while (res.next()) {
				System.out.println(res.getInt("bookid") + "\t");
				System.out.println(res.getString("bookname") + "\t");
				System.out.println(res.getString("publisher") + "\t");
				System.out.println(res.getInt("price") + "\t");
				System.out.println(res.getInt(1) + "\t");
 			}
			res.close();
			conn.close();

		} catch (SQLException e) { // 걍 Exception e라고 쓰면 모든 통합 에러 메시지가 나올거다 참고
			e.printStackTrace();
			System.out.println("에러");
		}
	}
}
