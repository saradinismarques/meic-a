package org.sah.main.service;

import com.auth0.jwk.JwkProvider;
import com.auth0.jwk.JwkProviderBuilder;
import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTCreationException;
import org.sah.exceptions.ErrorMessage;
import org.sah.exceptions.SAHException;
import org.sah.main.dto.SignUpDto;
import org.sah.main.entity.User;
import org.sah.main.repository.PatientRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.sah.main.entity.Appointment;

import javax.transaction.Transactional;
import java.security.KeyPair;
import java.security.interfaces.RSAPrivateKey;
import java.security.interfaces.RSAPublicKey;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.TimeUnit;

import static java.lang.System.exit;

@Service
@Transactional
public class PatientService {
    private HashMap<String, Long> sessions = new HashMap<>();
    @Autowired
    private PatientRepository patientRepository;

    public PatientService(PatientRepository patientRepository) {


        this.patientRepository = patientRepository;
    }

    public User getUser(String userEmail) {
        return patientRepository.findUserByEmail(userEmail).orElseThrow(() -> new SAHException(ErrorMessage.NO_SUCH_USER, userEmail));
    }
    public String getSessionToken(User user, KeyPair keyPair) {
        try {

            Algorithm algorithm = Algorithm.RSA256((RSAPublicKey) keyPair.getPublic(), (RSAPrivateKey) keyPair.getPrivate());
            String token = JWT.create().withSubject(user.getEmail())
                    .sign(algorithm);
            sessions.put(token, user.getId());
            return token;
        } catch (JWTCreationException exception) {
            // Invalid Signing configuration
            exit(1);
            return null;
        }
    }

    public List<Appointment> getAppointments(Long id) {
        return patientRepository.findById(id).orElseThrow().getAppointments();
    }

    public void checkNoUser(String email) {
        if (patientRepository.findUserByEmail(email).isPresent()) {
            throw new SAHException(ErrorMessage.USER_ALREADY_EXISTS, email);
        }
    }

    public User registerUser(SignUpDto signUpDto) {
        User user = new User(signUpDto);
        user = patientRepository.save(user);
        return user;
    }
}
