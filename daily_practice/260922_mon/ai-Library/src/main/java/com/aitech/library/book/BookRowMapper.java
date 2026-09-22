package com.aitech.library.book;

import java.sql.ResultSet;
import java.sql.SQLException;

import org.springframework.jdbc.core.RowMapper;

public class BookRowMapper implements RowMapper<BookVo>{

	@Override
	public BookVo mapRow(ResultSet rs, int rowNum) throws SQLException {
		BookVo book = new BookVo();
		book.setB_no(rs.getInt("b_no"));
		book.setB_name(rs.getString("b_name"));
		book.setB_author(rs.getString("b_author"));
		book.setB_publisher(rs.getString("b_publisher"));
		book.setB_publish_year(rs.getString("b_publish_year"));
		book.setB_isbn(rs.getString("b_isbn"));
		book.setB_call_number(rs.getString("b_call_number"));
		book.setB_rental_able(rs.getInt("b_rental_able"));
		book.setB_img(rs.getString("b_img"));
		return book;
	}

}
