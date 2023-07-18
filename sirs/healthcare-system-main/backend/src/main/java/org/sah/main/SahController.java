package org.sah.main;

import org.sah.main.dto.SignUpDto;
import org.sah.main.entity.User;
import org.sah.main.service.KeyProviderService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.sah.main.dto.LoginDto;
import org.sah.main.service.PatientService;

@RestController
public class SahController {
	@Autowired
	private KeyProviderService keyProviderService;
	@Autowired
	private PatientService patientService;

	@PostMapping("/login")
	public String logIn(@RequestBody LoginDto loginDto) {
		User user = patientService.getUser(loginDto.getEmail());
		return patientService.getSessionToken(user, keyProviderService.getKeyPair());
	}
	@PostMapping("/signup")
	public String signUp(@RequestBody SignUpDto signUpDto) {
		patientService.checkNoUser(signUpDto.getEmail());

		User user = patientService.registerUser(signUpDto);

		return patientService.getSessionToken(user, keyProviderService.getKeyPair());
	}
}