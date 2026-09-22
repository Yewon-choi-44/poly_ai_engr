package com.aitech.library.book;

import java.io.File;
import java.sql.Connection;
import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import com.aitech.library.book.BookDao;

@Controller
public class BookController {
	
	private static final String uploadDir = System.getProperty("user.dir") + "/upload/book_images/"; //파일 저장 경로
	
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

		
	@RequestMapping("/registerbookconfirm")
	public String registerbookconfirm(BookVo bookVo, 
			@RequestParam("b_img_file") MultipartFile file) throws Exception {
		if(!file.isEmpty()) { // 선택 파일이 있으면
			bookVo.setB_img(saveBookImg(file)); // 실제 파일명.확장자만 DB 저장
		}
		bookDao.insertBook(bookVo);
		return "redirect:managementbook";
	}

	
	private String saveBookImg(MultipartFile file) throws Exception {
		File dir = new File(uploadDir); 
		
		if(!dir.exists()) 
			dir.mkdirs(); 
			
		String fileName = new SimpleDateFormat("yyyyMMdd_HHmmss_").format(new Date()) 
				+ file.getOriginalFilename();
		file.transferTo(new File(uploadDir + fileName));
		return fileName;
	}
	
	private void deleteBookImg(String b_img) {
		if(b_img != null && b_img.isEmpty()) {
			new File(uploadDir + b_img).delete();
		}
	}
	
	
	@RequestMapping("/managementbook")
	public String managementbook(Model model) {
		List<BookVo> books = bookDao.getAllBook();
		model.addAttribute("books",books);
		return "admin/management_book";
		
	}
	
	@RequestMapping("/bookdetail")
	public String bookDetail(@RequestParam("b_no") int b_no, Model model) {
		model.addAttribute("book", bookDao.getDetailBook(b_no));
		return "book/book_detail";
		
	}
	
	
	@RequestMapping("/modifybook")
	public String modifybook(@RequestParam("b_no") int b_no, Model model) {
		model.addAttribute("book", bookDao.getDetailBook(b_no));	
		return "admin/modify_book";
		}
	
	
	@RequestMapping("/modifybookconfirm")
	public String modifybookconfirm(BookVo bookVo, @RequestParam("b_img_file") MultipartFile file) throws Exception {
		
		BookVo oldBook = bookDao.getDetailBook(bookVo.getB_no());
		
		if(!file.isEmpty()) {
			bookVo.setB_img(saveBookImg(file));
			deleteBookImg(oldBook.getB_img());
		} else {
			bookVo.setB_img(oldBook.getB_img());
		}
		bookDao.updateBook(bookVo);
		return "redirect:managementbook";
	}
	
	
	@RequestMapping("/deletebook")
	public String deletebook(@RequestParam("b_no") int b_no) {
		BookVo oldBook = bookDao.getDetailBook(b_no);
		bookDao.deleteBook(b_no);	
		deleteBookImg(oldBook.getB_img());
		return "redirect:managementbook";
	}
}

