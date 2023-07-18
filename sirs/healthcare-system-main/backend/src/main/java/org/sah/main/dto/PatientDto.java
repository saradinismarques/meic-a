package org.sah.main.dto;

import org.sah.main.entity.Appointment;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

public class PatientDto implements Serializable {

    private Long id;
    private String name;
    private List<Appointment> appointments = new ArrayList<>();

    public PatientDto(){
    }

    public PatientDto(Long id, String name, List<Appointment> appointments){
        this.id = id;
        this.name = name;
        this.appointments = appointments;
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
}
