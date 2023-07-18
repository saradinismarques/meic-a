package org.sah.main.service;

import com.auth0.jwt.interfaces.RSAKeyProvider;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.security.Key;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.interfaces.RSAPrivateKey;
import java.security.interfaces.RSAPublicKey;

@Service
@Transactional
public class KeyProviderService {
    private KeyPair keyPair;

    public KeyProviderService() {
        try {
            KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
            kpg.initialize(2048);
            keyPair = kpg.generateKeyPair();
        } catch (NoSuchAlgorithmException exception) {
            // No such algorithm
        }
    }

    public KeyPair getKeyPair() {
        return keyPair;
    }
}
