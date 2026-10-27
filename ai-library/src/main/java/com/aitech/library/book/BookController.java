package com.aitech.library.book;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import com.aitech.library.member.MemberVo;

import jakarta.servlet.http.HttpSession;

@Controller
public class BookController {
	
	private static final String UPLOADDIR =
			System.getProperty("user.dir") + "/upload/book_images/";
	
	@Autowired
	private BookDao bookDao;
	
	public BookController(BookDao bookDao) {
		this.bookDao = bookDao;
	}

	@RequestMapping("/booklist")
	public String booklist(Model model) {
		List<BookVo> books = bookDao.getAllBook();
		model.addAttribute("books", books);
		return "book/book_list";
	}
	
	@RequestMapping("/registerbook")
	public String registerbook() {
		return "admin/register_book";
	}
	
	private String saveBookImg(MultipartFile file) throws Exception {
		File dir = new File(UPLOADDIR);
		if(!dir.exists())
			dir.mkdir();
		
		String fileName = new SimpleDateFormat("yyyyMMdd_HHmmss_").format(new Date())
				+ file.getOriginalFilename();
		file.transferTo(new File(UPLOADDIR + fileName));
		   
		return fileName;
	}
	
	private void deleteBookImg(String b_img) {
		if(b_img != null && !b_img.isEmpty()) {
			new File(UPLOADDIR + b_img).delete();
		}
	}
	
	@RequestMapping("/registerbookconfirm")
	public String registerbookconfirm(BookVo bookVo, 
			@RequestParam("b_img_file") MultipartFile file) throws Exception {
		if(!file.isEmpty()) {
			bookVo.setB_img(saveBookImg(file));
		}
		bookDao.insertBook(bookVo);
		return "redirect:managementbook";
	}
	
	@RequestMapping("/managementbook")
	public String managementbook(Model model) {
		List<BookVo> books = bookDao.getAllBook();
		model.addAttribute("books", books);
		return "admin/management_book";
	}
	
	@RequestMapping("/detailbook")
	public String detailbook(@RequestParam("b_no") int b_no, Model model) {
		BookVo book = bookDao.getDetailBook(b_no);
		if(book == null)
			return "redirect:/booklist";
		model.addAttribute("book", book);
		return "book/book_detail";
	}
	
	@RequestMapping("/modifybook")
	public String modifybook(@RequestParam("b_no") int b_no, Model model) {
		model.addAttribute("book", bookDao.getDetailBook(b_no));
		return "admin/modify_book";
	}
	
	@RequestMapping("/modifybookconfirm")
	public String modifybookconfirm(BookVo bookVo,
			@RequestParam("b_img_file") MultipartFile file) throws Exception {
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
	
	@RequestMapping("/searchbook")
	public String searchbook(@RequestParam("searchTxt") String searchTxt, Model model) {
		model.addAttribute("books", bookDao.searchBook(searchTxt));
		model.addAttribute("searchTxt", searchTxt);
		return "book/book_list";
	}
	
	@RequestMapping("/rentalbook")
	public String rentalbook(@RequestParam("b_no") int b_no, HttpSession session) {
		MemberVo loginMember = (MemberVo) session.getAttribute("loginMember");
		if (loginMember == null) {
			return "redirect:/loginmember";
		}
		
		if("ADMIN".equals(loginMember.getM_role())) {
			return "redirect:/booklist";
		}
		
		BookVo book = bookDao.getDetailBook(b_no);
		if(book == null)
			return "redirect:booklist";
		
		if(book.getB_rental_able() != 1) {
			return "redirect:/detailbook?b_no=" + b_no;
		}
		
		bookDao.insertRentalBook(b_no, loginMember.getM_no());
		bookDao.updateRentalAble(b_no, 0);
		return "redirect:/detailbook?b_no=" + b_no;
	}
	
	@RequestMapping("/rentalbooklist")
	public String rentalbooklist(HttpSession session, Model model) {
		MemberVo loginMember = (MemberVo) session.getAttribute("loginMember");
		if(loginMember == null) {
			return "redirect:/loginmember";
		}
		
		List<RentalBookVo> rentalbooks = bookDao.getMyRentalBook(loginMember.getM_no());
		model.addAttribute("rentalbooks", rentalbooks);
		return "book/book_rental";
	}
	
	@RequestMapping("/returnbook")	
	public String returnbook(@RequestParam("rb_no") int rb_no, 
			@RequestParam("b_no") int b_no, HttpSession session) {
		if (session.getAttribute("loginMember") == null) {
			return "redirect:/loginmember";
		}
		bookDao.returnBook(rb_no);
		bookDao.updateRentalAble(b_no, 1);
		return "redirect:/rentalbooklist";
		
	}
}
