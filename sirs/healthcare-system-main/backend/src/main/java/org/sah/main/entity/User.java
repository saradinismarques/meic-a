package org.sah.main.entity;

import org.sah.main.dto.SignUpDto;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "patients")
public class User {
    @Id
    @GeneratedValue
    private Long id;

    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "email")
    private String email;

    @Column(name = "password")
    private String password;

    @ElementCollection
    @Column(name = "appointments", nullable = false)
    private List<Appointment> appointments = new ArrayList<>();

    public User() {
    }

    public User(String name, List<Appointment> appointments) {
        this.name = name;
        this.appointments = appointments;
    }

    public User(SignUpDto signUpDto) {
        this.id = null;
        this.name = signUpDto.getName();
        this.email = signUpDto.getEmail();
        this.password = signUpDto.getPassword(); // TODO Hash this password pls :)
    }

    public void setAppointments(List<Appointment> appointments) {
        this.appointments = appointments;
    }

    public List<Appointment> getAppointments() {
        return appointments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return this.email;
    }

    public Long getId() {
        return id;
    }
}
