package com.aitech.cafe.menu;

import java.sql.ResultSet;
import java.sql.SQLException;

import org.springframework.jdbc.core.RowMapper;

public class MenuRowMapper implements RowMapper<MenuVo>{
	
	@Override
	public MenuVo mapRow(ResultSet rs, int rowNum) throws SQLException{
		MenuVo menu = new MenuVo();
		menu.setMn_no(rs.getInt("mn_no"));
		menu.setMn_name(rs.getString("mn_name"));
		menu.setMn_price(rs.getInt("mn_price"));
		menu.setMn_desc(rs.getString("mn_desc"));
		menu.setMn_img(rs.getString("mn_img"));
		menu.setMn_reg_date(rs.getString("mn_reg_date"));
		menu.setMn_mod_date(rs.getString("mn_mod_date"));
		
		return menu;
	}

}
