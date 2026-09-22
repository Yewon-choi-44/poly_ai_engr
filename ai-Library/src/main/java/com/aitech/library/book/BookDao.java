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
	
//	public BookDao(DataSource dataSource) {
//		this.dataSource = dataSource;
//	}
	@Autowired
	public BookDao(JdbcTemplate jdbcTemplate) {
		this.jdbcTemplate = jdbcTemplate;
	}
	
	
	public void insertBook(BookVo bookVo) {
		String sql = "INSERT INTO book(b_name, b_author, b_publisher, b_publish_year, "
				+ "b_isbn, b_call_number, b_rental_able, "
				+ "b_img, b_reg_date, b_mod_date) " + "VALUES(?, ?, ?, ?, ?, ?, ?, ?, now(), now())";

		jdbcTemplate.update(sql, bookVo.getB_name(), bookVo.getB_author(), 
				bookVo.getB_publisher(), bookVo.getB_publish_year(), bookVo.getB_isbn(), 
				bookVo.getB_call_number(), bookVo.getB_rental_able(), bookVo.getB_img() );
	}
		
	

	public List<BookVo> getAllBook() {
		String sql = "SELECT * FROM book ORDER BY b_no";
		return jdbcTemplate.query(sql, new BookRowMapper());
	}

	public BookVo getDetailBook(int b_no) {
		String sql = "SELECT * FROM book WHERE b_no = ?";
		return jdbcTemplate.queryForObject(sql, new BookRowMapper(), b_no);
	}
	
                                                                                                                                                                                                                         
   	public void updateBook(BookVo bookVo) {                                                                                                                                                                                  
   			String sql = "UPDATE book SET b_name = ? , b_author = ? , b_publisher = ? , "
   					+ "b_publish_year = ? , b_isbn = ? , b_call_number = ? , b_rental_able = ? , "
   					+ "b_img = ? , b_reg_date = now() , b_mod_date = now() WHERE b_no = ?";
   			jdbcTemplate.update(sql, bookVo.getB_name(), bookVo.getB_author(), bookVo.getB_publisher(), 
   					bookVo.getB_publish_year(), bookVo.getB_isbn(), bookVo.getB_call_number(), bookVo.getB_rental_able(), 
   					bookVo.getB_img(), bookVo.getB_no());       	
   	}                                                                                                                                                                               	
   	
   	public void deleteBook(int b_no) {                                                                                                                                                                                  
   		String sql = "DELETE FROM book WHERE b_no = ?";
   		int rows = jdbcTemplate.update(sql, b_no);
   	}                                                                                                                                                                               	
    	                                                                                                                                                                                                                            	
}