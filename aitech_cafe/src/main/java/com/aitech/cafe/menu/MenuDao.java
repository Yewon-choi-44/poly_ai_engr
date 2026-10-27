package com.aitech.cafe.menu;

import java.util.List;

import org.jspecify.annotations.Nullable;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import com.aitech.library.book.BookRowMapper;

@Repository
public class MenuDao {

	private final JdbcTemplate jdbcTemplate;
	
	@Autowired
	public MenuDao(JdbcTemplate jdbcTemplate) {
		this.jdbcTemplate = jdbcTemplate;
	}
	
	
	public List<MenuVo> getAllMenu() {
		String sql = "SELECT * FROM menu ORDER BY n_no";
		return jdbcTemplate.query(sql, new MenuRowMapper());
	}


	public List<MenuVo> searchMenu(String searchTxt) {
		String sql = "SELECT * FROM book WHERE n_name LIKE ? ORDER BY n_no";
		return jdbcTemplate.query(sql, new MenuRowMapper(), "%"+searchTxt + "%");
	}
	

	

}
