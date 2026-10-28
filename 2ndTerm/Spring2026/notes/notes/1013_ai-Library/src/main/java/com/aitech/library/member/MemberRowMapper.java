package com.aitech.library.member;

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
		member.setM_gender(rs.getString("m_gender"));
		member.setM_phone(rs.getString("m_phone"));
		member.setM_mail(rs.getString("m_mail"));
		member.setM_role(rs.getString("m_role"));
		member.setM_reg_date(rs.getString("m_reg_date"));
		member.setM_mod_date(rs.getString("m_mod_date"));
		return member;
	}

}
