package com.aitech.library.book;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.aitech.library.book.BookDao;

@Controller
public class BookController {
	
	@Autowired
	private BookDao bookDao;
		
	public BookController(BookDao bookDao) {
		this.bookDao = bookDao;
	}
	
	@RequestMapping("/booklist")
	public String booklist(Model model) {
		List<BookVo> books = bookDao.getAllBook();
		model.addAttribute("books",books);
		return "book/book_list";
	
	}
	
	@RequestMapping("/registerbook")
	public String registerbook() {
			return "admin/register_book";
		}
}

