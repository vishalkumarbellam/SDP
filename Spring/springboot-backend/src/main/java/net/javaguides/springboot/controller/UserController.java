package net.javaguides.springboot.controller;
import net.javaguides.springboot.model.User;

import net.javaguides.springboot.repository.UserRepository;
import net.javaguides.springboot.services.UserService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin(origins="http://localhost:3000")
public class UserController {
	
	@Autowired
	private UserService s;

	@Autowired
	private UserRepository userRepository;
	
	
	@PostMapping("/user")
	User newUser(@RequestBody User newUser)
	{   
		return s.create(newUser);
	}
	
	
	
	@RequestMapping("/check")
		String checkUser(@RequestBody User checkUser)
		{
		System.out.println(checkUser);
		return s.checkUser(checkUser);
	}
}
