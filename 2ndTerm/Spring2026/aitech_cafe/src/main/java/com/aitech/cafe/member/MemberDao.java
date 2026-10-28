package com.aitech.cafe.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class MemberDao {
	private JdbcTemplate jdbcTemplate;
	
	@Autowired
	public MemberDao(JdbcTemplate jdbcTemplate) {
		this.jdbcTemplate = jdbcTemplate;
	}
	
	public MemberVo getMemberById(String m_id) {
		String sql = "SELECT * FROM member WHERE m_id = ?";
		try {
			return jdbcTemplate.queryForObject(sql, new MemberRowMapper(), m_id);			
		} catch (EmptyResultDataAccessException e) {
			return null;
		}
	}
	
}
