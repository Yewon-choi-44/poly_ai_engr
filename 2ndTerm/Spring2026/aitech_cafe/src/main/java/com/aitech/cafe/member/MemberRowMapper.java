package com.aitech.cafe.member;

import java.sql.ResultSet;
import java.sql.SQLException;

import org.springframework.jdbc.core.RowMapper;

public class MemberRowMapper implements RowMapper<MemberVo> {
	@Override
	public MemberVo mapRow(ResultSet rs, int rowNum) throws SQLException {
		MemberVo member = new MemberVo();
		member.setM_no(rs.getInt("m_no"));
		member.setM_id(rs.getString("m_id"));
		member.setM_pw(rs.getString("m_pw"));
		member.setM_name(rs.getString("m_name"));
		
		return member;
	}
}
