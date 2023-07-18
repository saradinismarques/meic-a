package org.sah.main.entity;

import javax.persistence.*;

@Entity
@Embeddable
public class Appointment {
    @Id
    @GeneratedValue
    private Long id;

    @Column(name = "type")
    private String type;

    @Column(name = "doctor")
    private String doctor;

    @Column(name = "description")
    private String description;

    public Appointment(){
    }

    public Appointment(String type, String doctor, String description){
        this.type = type;
        this.doctor = doctor;
        this.description = description;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getDoctor() {
        return doctor;
    }

    public void setDoctor(String doctor) {
        this.doctor = doctor;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}
