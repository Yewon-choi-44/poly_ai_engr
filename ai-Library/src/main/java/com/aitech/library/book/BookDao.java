package com.aitech.library.book;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class BookDao {
//	private DataSource dataSource;
	private JdbcTemplate jdbcTemplate;
	
	@Autowired
//	public BookDao(DataSource dataSource) {
//		this.dataSource = dataSource;
//	}
	public BookDao(DataSource dataSource) {
		this.jdbcTemplate = jdbcTemplate;
	}
	
	public void insertBook() {
		String sql = "INSERT INTO book(b_name, b_author, b_rental_able, b_reg_date, b_mod_date) " + "VALUES(?, ?, ?, now(), now())";
		
		try {
//			Connection conn = dataSource.getConnection();
			Connection conn = jdbcTemplate.getConnection();
			PreparedStatement pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, "JDBC로 입력한 책");
			pstmt.setString(2, "홍길동");
			pstmt.setInt(3, 1);
			pstmt.executeUpdate();
			conn.close();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	public List<BookVo> getAllBook() {
		String sql = "SELECT * FROM book ORDER BY b_no";
		List<BookVo> books = new ArrayList<>();
		
		try {
//			Connection conn = dataSource.getConnection();
			Connection conn = jdbcTemplate.getConnection();
			PreparedStatement pstmt = conn.prepareStatement(sql);
			ResultSet rs = pstmt.executeQuery();
			while (rs.next()) {
				
			}
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return books;
	}
}
