package net.javaguides.springboot.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

@Entity
public class User {
	
	@Id
	private String Id;
	private String name;
	private String emailId;
	private long phn_no; 	
	private String password;
	@Override
	public String toString() {
		return "User [Id=" + Id + ", name=" + name + ", emailId=" + emailId + ", phn_no=" + phn_no + ", password="
				+ password + "]";
	}
	public String getId() {
		return Id;
	}
	public void setId(String id) {
		Id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getEmailId() {
		return emailId;
	}
	public void setEmailId(String emailId) {
		this.emailId = emailId;
	}
	public long getPhn_no() {
		return phn_no;
	}
	public void setPhn_no(long phn_no) {
		this.phn_no = phn_no;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	
	
	
}
