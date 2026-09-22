package com.aitech.library;

import java.sql.Connection;
import java.sql.SQLException;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.aitech.library.book.BookDao;

@Controller
public class DBTestController {
	
//	@Autowired
//	private DataSource dataSource;
//	
//	@Autowired
//	private BookDao bookDao;
//	
//	@RequestMapping("/dbTest")
//	@ResponseBody
//	public String dbTest() {
//		Connection conn;
//		try {
//			conn = dataSource.getConnection();
//			String schema = conn.getCatalog();
//			conn.close();
//			return "DB 연결 성공 접속 스키마 = " + schema;
//		} catch (SQLException e) {
//			e.printStackTrace();
//			return "연결 실패 " + e.getMessage();
//		}
//	}
//	
//	
//	@RequestMapping("/dbInsert")
//	@ResponseBody
//	public String dbInsert() {
//		bookDao.insertBook();
//		return "DB Insert 완료";
//	}
}
