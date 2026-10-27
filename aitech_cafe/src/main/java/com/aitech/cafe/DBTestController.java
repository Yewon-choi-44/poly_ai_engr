package com.aitech.cafe;

import java.sql.Connection;
import java.sql.SQLException;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class DBTestController {
	@Autowired
	private DataSource dataSource;
	
	@RequestMapping("/dbtest")
	@ResponseBody
	public String dbtest() {
		Connection conn;
		try {
			conn = dataSource.getConnection();
			String schema = conn.getCatalog();
			conn.close();
			return "DB 연결 성공 접속 스키마 = " + schema;
		}catch (SQLException e) {
			return "연결 실패" + e.getMessage();
		}
	}
}
