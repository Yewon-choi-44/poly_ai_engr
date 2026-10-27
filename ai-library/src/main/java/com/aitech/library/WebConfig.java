package com.aitech.library;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer{
	public void addInterceptors(InterceptorRegistry registory) {
		registory.addInterceptor(new LoginCheckInterceptor()).addPathPatterns("/rentalbook", "/rentalbooklist", 
				"/returnbook","/modifymember", "/modifymemberconfirm", "/deletebook");
	}
}
