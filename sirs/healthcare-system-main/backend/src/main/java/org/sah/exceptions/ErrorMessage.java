package org.sah.exceptions;

public enum ErrorMessage {

	NO_SUCH_USER("The user with the e-mail %s doesn't exist", 1001),
	USER_ALREADY_EXISTS("An user with the e-mail %s already exists", 1002);
	private final String label;
	private final int code;

	ErrorMessage(String label, int code) {
		this.label = label;
		this.code = code;
	}

	public String getLabel() {
		return this.label;
	}

	public int getCode() {
		return this.code;
	}
}
