package com.aitech.cafe.menu;

import java.util.List;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class MenuController {

	private static final String UPLOADDIR = 
			System.getProperty("user.dir") + "/upload/menu_images/";
	
	@Autowired
	private MenuDao menuDao;

	public MenuController(MenuDao menuDao) {
		this.menuDao = menuDao; 
	}
	
	
	@RequestMapping("/searchmenu")
	public String searchmenu(@RequestParam("searchTxt") String searchTxt, Model model) {
		model.addAttribute("menus", menuDao.searchMenu(searchTxt));
		model.addAttribute("searchTxt", searchTxt);
		return "menu/menu_list";
		
	}
	
	
	
	
}
