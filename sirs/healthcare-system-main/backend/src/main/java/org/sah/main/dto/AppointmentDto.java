package org.sah.main.dto;

import java.io.Serializable;

public class AppointmentDto implements Serializable {

    private Long id;
    private String type;
    private String doctor;
    private String description;

    public AppointmentDto(){
    }

    public AppointmentDto(Long id, String type, String doctor, String description){
        this.id = id;
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
