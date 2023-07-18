<template>
  <v-form
      class="pa-10"
      ref="form"
      v-model="valid"
      lazy-validation
  >
    <v-text-field
        v-model="name"
        :rules="nameRules"
        label="Name"
        required
    ></v-text-field>

    <v-text-field
        v-model="email"
        :rules="emailRules"
        label="E-mail"
        required
    ></v-text-field>

    <v-text-field
        v-model="password"
        :counter="8"
        :rules="passwordRules"
        :type="show1 ? 'text' : 'password'"
        label="Password"
        required
    ></v-text-field>

    <v-btn
        color="success"
        class="mr-4"
        @click="signup"
    >
      Sign Up
    </v-btn>
  </v-form>
</template>

<script>
import RemoteServices from "../services/RemoteServices.ts";
import SignUpDto from "../models/SignUpDto.ts";

export default {
  data: () => ({
    valid: true,
    name: '',
    email: '',
    password: '',
    show1: '',
    nameRules: [
      v => !!v || 'Name is required',
    ],
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
    passwordRules: [
      v => !!v || 'Put a password',
      v => (v && v.length >= 8) || 'Password must be 8 or more characters',
    ],
    select: null,
    checkbox: false,
  }),
  methods: {
    async signup() {
      let token = await RemoteServices.signup(new SignUpDto(this.name, this.email, this.password));
      console.log(token);
    }
  }
};
</script>
