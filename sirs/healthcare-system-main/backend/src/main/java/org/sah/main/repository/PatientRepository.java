package org.sah.main.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.sah.main.entity.User;

import javax.transaction.Transactional;
import java.util.Optional;

@Repository
@Transactional
public interface PatientRepository extends JpaRepository<User, Long> {
    Optional<User> findUserByEmail(String email);
}
