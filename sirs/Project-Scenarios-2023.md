Instituto Superior Técnico, Universidade de Lisboa

**Network and Computer Security**

# Project Scenarios

Congratulations! You have been hired by one of the following companies.
Each company has its business context and, more important, a set of security challenges.
Your team will have to write a proposal to address a specific security challenge.

Additional challenges can be proposed, as long as there is a clear security core, which will require the use of cryptographic primitives.

_Important note: the security aspects, both functional and assurance ones, are the essential points where you should focus your work and will be the main metrics to be considered in the grading. In the designed and proposed solutions, user interface concerns are secondary._

----

## 1. Retail: MusicMarkt

_Business Context_

MusicMarkt is an online store that sells all things music related.
It offers a large variety of items such as musical instruments, sound systems, CDs, vinyls and other merchandise.

MusicMarkt allows reservations to be made for some new products before they are made available.
These products are usually CDs, vinyls, limited edition items, etc.

In order to reward loyal costumers and loyal fans, MusicMarkt has a scoreboard for each band and artist that ranks customers by the money they have spent on items from that band or artist.
When reservations open for a new item, during the first 24 hours only the top ranked customers in the respective scoreboard(s) can make a reservation.

_Security Challenges_

(i) In MusicMarkt, each user has an account that contains personal information to facilitate future orders.
The access to the users' accounts must be correctly authenticated using also the user's mobile device.

(ii) MusicMarkt interacts with a third-party Payment service, to assure that the transactions are payed securely.
The customer information, such as adresses and payment details,  must be correctly protected and kept confidential, both in storage and in the network.

(iii) Limited edition items have a high demand in MusicMarkt, which means that they are usually targeted by scalpers hoping to make a profit by reselling them.
The item must have a digital proof of authenticity that is robust and verifiable by third parties, even if MusicMarkt goes out of business.

## 2. Transportation & Distribution: Lemon

_Business Context_

Lemon is an international shared electric vehicle company that operates in Portugal since 2018, both with electric scooters and electric bicycles.

Customers can look for and unlock these vehicles through a mobile app or a website, where they also perform the payment for the used services.

Lemon's employees also have an internal app to pick up wrongly parked vehicles, which has access to their location through GPS and suggests the best course with Google Maps integration.

_Security Challenges_

(i) Lemon wants to store the least amount of user data as possible, and the solution found was using an authorization protocol where users do not need to share their password with the app when logging in, meaning Lemon does not need to store user passwords.
Given that the employees have access to the GPS location of Lemon's vehicles, it must be guaranteed that they cannot access user data on rented vehicles.
With this in mind, users must be anonymized in the app to ensure customer privacy while still allowing for the service operation.

(ii) The platforms should allow Payment Initiation Services (PIS), inspired by the European Payment Services Directive (PSD2).
These services help to initiate a payment from the consumer's account on a bank to the merchant's account by creating an interface to bridge both accounts, filling in the information needed for the bank transfer (amount of the transaction, account number, message) and informing the store of the transaction.

(iii) It is important to make sure that the vehicles are where they are claimed to be at.
For this, a location certification system should be used to produce verifiable location information and prevent location spoofing resulting in the theft or misplacement of vehicles.

## 3. Restaurants & Tourism: TheCork

_Business Context_

TheCork is a service that allows its users to taste the best food and wines in town by enabling easy restaurant reservations via a very user-friendly mobile application that integrates seamlessly with the restaurants' calendars.

TheCork offers a mobile app to its customers to display the list of restaurants available at the user’s location.
It also allows them to book a table for a specific number of people if the restaurant still has free tables.
There is also a website that provides the same functionality.
TheCork also provides back-office for the restaurants which is used to manage the schedule and to approve or deny the customers reservations.

The system also has an external integration with a discount card service provider, that allows customers to use their card points in order to have discounts in their bookings.

_Security Challenges_

(i) TheCork has personal information about each customer, which needs to be kept private.
There is a need for an authentication server that can support both the app level and the back-office level, to avoid illegitimate users to get access to restaurant’s agenda / customer data.

(ii) TheCork’s users keep their credit card data information stored in the app in order to facilitate reservations at high-end restaurants that need you to leave a deposit. This data needs to be safe and confidential at the device level and on-the-wire when it gets sent to TheCork’s servers and to the Credit Card company.

(iii) TheCork allows their users to buy Gift Cards (that may differ in cost) to offer.
These Gift Cards can be then redeemed by anyone and the respective funds will be added to the user's wallet.
However, these cards may only be redeemed once.
There is a need to ensure that no-one can tamper these Gift Cards to change their value, use them several times, etc.

## 4. Insurance & Banking: NCMB

_Business context_

Nova Caixa Milenar Bancária NCMB is a bank that operates in Portugal since 1900.
It has a large portfolio of clients, from individuals to small businesses, and large multi-national organizations.
NCMB has a large catalog of products: credit cards, mortgages, and small loans, and acts as a financial broker (allowing customers to trade shares and other assets).

The front-office of the NCMB offers a public website that displays the products and services; a private website in which clients can access their bank account information and subscribe to their products.
The information presented on the websites and corresponding features can also be accessed through a mobile app.

A back-office is used by the bank employees to contact the clients, propose new products, and manage the portfolio of the customers (buy and sell financial assets).

The system has integration with external institutions, namely, the Bank of Portugal (to communicate the financial details of the customers) and insurance companies (to promote insurance services that are associated with the loans).

_Security challenges_

(i) There are some concerns with the access to the financial information of the clients.
The authenticity of the information and the privacy of the clients needs to be assured.
It is necessary to provide a Two-Factor Authentication (2FA) mechanism that requires the bank customers to use an alternative device when logging in the bank app.

(ii) The bank allows its clients to subscribe to any product and service remotely.
However, there are concerns that both the bank employees and the clients can be impersonated.
Also, financial information should be kept private.

(iii) The bank needs to gather and store sensitive information about its clients in different layers.
The information systems should allow fine-grained access to the records to the relevant staff (account managers) for some layers.
Other users (clerks), can see some other fields of information.
There should also be mechanisms in place to allow access in special circumstances, for example, during an audit process.

## 5. Healthcare: SAH

_Business context_

_Saint Acutis_ hospital operates in Portugal since 2020.
It provides Urgent Care, open 24/7 (24 hours, 7 days a week).
It also provides Speciality Consultations, including: Orthopedy, Cardiology, and Dermatology.

The front-office of the hospital offers both a public web site, for displaying general information, and a customer web site, where patients can check their appointments and make new ones.
There is also a mobile application that provides the same functionality.

The back-office is used to manage the schedule, the room reservations, and the medical records.

The system has integrations with external institutions, namely, the Ministry for Health, and several exam facilities and laboratories.

_Security challenges_

(i) There are some concerns with the access to _test results_ from external labs.
The authenticity of the information and the privacy of the patients needs to be assured.
Also, the medical test data has to be archived in a way such that its authenticity can be verified later, if necessary.

(ii) The hospital is considering the option to provide remote consultation through chat and teleconference (audio with optional video).
However, there are concerns that both the Doctors and the patients can be impersonated.
Also, in the case of Celebrities, there may be attemps to breach privacy on purpose.

(iii) The hospital needs to gather and store sensitive information from patients.
The information systems should allow fine-grained and contextualized access to the records to the relevant staff, like Doctors and Nurses.
There should also be mechanisms in place to allow access on special circumstances, like Emergencies or Pandemics.

## 6. Legal: ALA

_Business Context_

The ALA (Ávila & Lisieux Attorneys) is a Law Firm providing legal services in both Fiscal and Criminal Law.
The legal office has a front-end server that runs a web site displaying the usual overview of the firm organization, areas of activity and contact information, as well as providing some services to both ALA lawyers and clients.
This website and services can be accessed both by desktop browsers and by a mobile application.

The ALA website services are connected to a back-office that is used to manage all persistent data.

Furthermore some of these services involve third party entities within the Portuguese legal system with which legal documents must be exchanged.

Since ALA handles court cases around sensitive topics that may involve people willing the compromise the data and systems of ALA, its managers are worried that some of its services might be attacked.
The weakest link seems to be the communication between the ALA system and both the ALA clients (desktop and mobile) and other external entities.

The following security challenges have been identified:

(i) Communication between ALA and its clients is especially sensitive.
Request documents submitted to the website should not be observable by malicious agents on the open networks and should be stored in a way that is only readable by the lawyer assigned to the specific client.

(ii) The system should allow clients to pick a proxy representative that can send documents to ALA on their behalf.
This power of representation must have a limited validity.

(iii) The temporal order of the submission of documents to ALA by clients can be relevant for legal procedures.
Therefore it should be possible for ALA managers to audit the order and submission timestamps of all documents in the system.
Furthermore, when a client submits a request, she should receive a receipt proving the reception of the document by ALA at the specific date and time.

## 7. Industry: StarDrive

_Business context_

StarDrive automotive is a company focused on self-driving and remote control vehicles.
The production plant deploys several sensors and actuators, to achieve a mostly automatic assembly line.
The entire production plant is controlled by a complex system that allows the engineers to oversee the production process and detect anomalies.

The front-office of the StarDrive management system allows the employees to monitor the production process.
A “public” version of the front-office can be accessed from the Intranet of StarDrive allowing any employee to see, in real-time, the production statistics and the distribution of the working shifts.
A private area of the front-office allows the factory employees to consult private information about their job status (for example: salary, absent working days, parental leaves, etc).

A back-office is used by the engineers to buy production parts, manage information about the factory employees (for example team salaries), query stock information, access information from the sensors, and access the actuators to control the production process.

The system has integration with external institutions, namely, providers, audit companies, accounting firms to process salaries and taxes, and car dealerships.

_Security challenges_

(i) There are some concerns regarding access to the control system of StarDrive.
Only authenticated engineers can manage the actuators of the factory.
Also, every access to the actuators needs to be stored for audit purposes.

(ii) The sensors and actuators receive periodic software updates.
It is necessary to ensure that the update process fetches the latest version from an authenticated repository.

(iii) The factory needs to store sensitive information from the production process (to prevent industrial espionage).
The information systems should allow fine-grained access to the production records from authenticated engineers.
There should also be mechanisms in place to allow access in special circumstances, for example, during an audit process.

## 8. Utilities: EcoGes

_Business Context_

EcoGes is the new system for the Electricity provider, which allows clients to have a minute-by-minute update on their energy consumption and production (if that is the case).
With this new system, the user will be able to monitor the energy cost of every household appliance or how much energy the solar panels are producing by logging into the EcoGes website.
This system is also used to manage the contract of every user and to calculate the monthly invoices regarding the consumed energy, the energy plan (flat rate or bi-hourly rate), and taxes.

This system is composed of a public website (front-office), for the clients to have access to energy consumption information and update their personal data; an internal private back-office (via a website or through a management console) where the employees of EcoGes can manage the system according to their role in the company (marketing, account manager, technical assistance, or system manager).

_Security Challenges_

(i) The users can update their information but cannot see the critical data, such as bank account ID and authorization, address, and other personal information.
The information is stored in the same physical database, but the data separation must be enforced by the use of cryptography.

(ii) The data is available according to the role:
    a) The marketing employees should not see personal information about the user other than his name, User ID, and energy consumption profile.
    b) The account manager should not be able to see the user consumption profile.
    c) The system manager can edit the energy cost, tax values, and other internal data but cannot see the user's information.  
These information compartments are protected with cryptography and the different access levels require specific keys.

(iii) If the user account is attacked, the attacker should not be able to get personal user information.
Ideally should not be able to get the user ID and his energy consumption profile.
The separation of personal data from consumption data is enforced by the use of cryptography.
The energy management system should be able to access one compartment but not the other.

----

[SIRS Faculty](mailto:meic-sirs@disciplinas.tecnico.ulisboa.pt)
