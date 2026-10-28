package com.aitech.library.book;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class BookDao {
//	private DataSource dataSource;
	private JdbcTemplate jdbcTemplate;

	@Autowired
	public BookDao(JdbcTemplate jdbcTemplate) {
		this.jdbcTemplate = jdbcTemplate;
	}

//	public BookDao(DataSource dataSource) {
//		this.dataSource = dataSource;
//	}

	public void insertBook(BookVo bookVo) {
		String sql = "INSERT INTO book(b_name, b_author, b_publisher, b_publish_year, "
				+ "b_isbn, b_call_number, b_rental_able, b_img, b_reg_date, b_mod_date) "
				+ "VALUES(?, ?, ?, ?, ?, ?, ?, ?, now(), now())";
		jdbcTemplate.update(sql, bookVo.getB_name(), bookVo.getB_author(), bookVo.getB_publisher(),
				bookVo.getB_publisher_year(), bookVo.getB_isbn(), bookVo.getB_call_number(), bookVo.getB_rental_able(),
				bookVo.getB_img());
	}

	public List<BookVo> getAllBook() {
		String sql = "SELECT * FROM book ORDER BY b_no";
		return jdbcTemplate.query(sql, new BookRowMapper());
	}

	public BookVo getDetailBook(int b_no) {
		String sql = "SELECT * FROM book WHERE b_no = ?";
		try {
			return jdbcTemplate.queryForObject(sql, new BookRowMapper(), b_no);
		} catch (EmptyResultDataAccessException e) {
			return null;
		}
	}

	public void updateBook(BookVo bookVo) {
		String sql = "UPDATE book SET b_name = ?, b_author = ?, b_publisher = ?,"
				+ " b_publish_year = ?, b_isbn = ?, b_call_number = ?, b_rental_able = ?,"
				+ " b_img = ?, b_reg_date = now(), b_mod_date = now() WHERE b_no = ?";
		jdbcTemplate.update(sql, bookVo.getB_name(), bookVo.getB_author(), bookVo.getB_publisher(),
				bookVo.getB_publisher_year(), bookVo.getB_isbn(), bookVo.getB_call_number(), 
				bookVo.getB_rental_able(), bookVo.getB_img(), bookVo.getB_no());
	}
	
	public void deleteBook(int b_no) {
		String sql = "DELETE FROM book WHERE b_no = ?";
		jdbcTemplate.update(sql, b_no);
	}
	
	public List<BookVo> searchBook(String searchTxt) {
		String sql = "SELECT * FROM book WHERE b_name LIKE ? ORDER BY b_no";
		return jdbcTemplate.query(sql, new BookRowMapper(), "%"+searchTxt + "%");
	}
	
	public void insertRentalBook(int b_no, int m_no) {
		String sql = "INSERT INTO rentalbook(b_no, m_no, rb_start_date,"
				+ " rb_reg_date, rb_mod_date)"
				+ " VALUES(?, ?, now(), now(), now())";
		jdbcTemplate.update(sql, b_no, m_no);
	}
	
	public void updateRentalAble(int b_no, int b_rental_able) {
		String sql = "UPDATE book SET b_rental_able = ? WHERE b_no = ?";
		jdbcTemplate.update(sql, b_rental_able, b_no);
	}
	
	public List<RentalBookVo> getMyRentalBook(int m_no) {
		String sql = "SELECT rb.rb_no, rb.b_no,"
				+ " DATE_FORMAT(rb.rb_start_date, '%Y-%m-%d') AS rb_start_date,"
				+ " DATE_FORMAT(rb.rb_end_date, '%Y-%m-%d') AS rb_end_date,"
				+ " b.b_name, b.b_call_number, b.b_img"
				+ " FROM rentalbook rb JOIN book b ON rb.b_no = b.b_no"
				+ " WHERE rb.m_no = ? ORDER BY rb.rb_no DESC";
		return jdbcTemplate.query(sql, new RentalBookVoRowMapper(), m_no);
	}
	
	public void returnBook(int rb_no) {
		String sql = "UPDATE rentalbook SET rb_end_date = now(), "
				+ "rb_mod_date = now() WHERE rb_no = ?";
		jdbcTemplate.update(sql, rb_no);
	}
}
