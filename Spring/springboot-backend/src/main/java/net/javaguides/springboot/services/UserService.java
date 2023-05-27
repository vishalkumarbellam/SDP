package net.javaguides.springboot.services;

import java.util.Optional;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import net.javaguides.springboot.model.User;
import net.javaguides.springboot.repository.UserRepository;

@Service
public class UserService  {
	
	@Autowired
	private UserRepository userRepository;
	
	public User create(User u)
	{

		   u.setId(Long.toString(u.getPhn_no()).charAt(0)+u.getPassword()+u.getName());
		   System.out.println(u);
			return userRepository.save(u);

	}
	
	public String checkUser(User u)
	{
		Optional<User> opt = userRepository.findById(u.getPassword()+u.getName());
		//if log(row) is not present, creates a new log
		if(opt.isEmpty())
			return("Wrong password");
		else
			return("login Succcessful");
		
		
	}

}
