package com.aitech.library.book;

import java.sql.ResultSet;
import java.sql.SQLException;

import org.springframework.jdbc.core.RowMapper;

public class RentalBookVoRowMapper implements RowMapper<RentalBookVo>{
	
	@Override
	public RentalBookVo mapRow(ResultSet rs, int rowNum) throws SQLException {
		RentalBookVo rental = new RentalBookVo();
		rental.setRb_no(rs.getInt("rb_no"));
		rental.setB_no(rs.getInt("b_no"));
		rental.setB_name(rs.getString("b_name"));
		rental.setB_call_number(rs.getString("b_call_number"));
		rental.setB_img(rs.getString("b_img"));
		rental.setRb_start_date(rs.getString("rb_start_date"));
		rental.setRb_end_date(rs.getString("rb_end_date"));
		return rental;
	}
	
}
