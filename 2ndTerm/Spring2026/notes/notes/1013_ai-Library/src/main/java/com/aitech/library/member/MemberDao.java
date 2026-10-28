package com.aitech.library.member;

import org.jspecify.annotations.Nullable;
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
	
	public void insertMember(MemberVo memberVo) {
		String sql = "INSERT INTO member(m_id, m_pw, m_name, m_gender, "
				+ "m_mail, m_phone, m_role, m_reg_date, m_mod_date) "
				+ "VALUES(?, ?, ?, ?, ?, ?, 'USER', now(), now())";
		jdbcTemplate.update(sql, memberVo.getM_id(), memberVo.getM_pw(), memberVo.getM_name(),
				memberVo.getM_gender(), memberVo.getM_mail(), memberVo.getM_phone());
	}

	public int countById(String m_id) {
		String sql = "SELECT count(*) FROM member WHERE m_id = ?";
		return jdbcTemplate.queryForObject(sql, Integer.class, m_id);
	}

	public MemberVo getMemberById(String m_id) {
		String sql = "SELECT * FROM member WHERE m_id = ?";
		try {
			return jdbcTemplate.queryForObject(sql, new MemberRowMapper(), m_id);
		} catch (EmptyResultDataAccessException e) {
			return null;
		}
	}

	public MemberVo getDetailMember(int m_no) {
		String sql = "SELECT * FROM member WHERE m_no = ?";
		try {
			return jdbcTemplate.queryForObject(sql, new MemberRowMapper(), m_no);
		} catch (EmptyResultDataAccessException e) {
			return null;
		}
	}

	public void updateMember(MemberVo memberVo) {
		String sql ="UPDATE member SET m_pw=?, m_name=?, m_gender=?, "
				+ "m_phone=?, m_mail=?, m_mod_date=now() WHERE m_no=?";
		jdbcTemplate.update(sql, memberVo.getM_pw(), memberVo.getM_name(), memberVo.getM_gender(), 
				memberVo.getM_phone(), memberVo.getM_mail(), memberVo.getM_no());
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
