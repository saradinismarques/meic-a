<template>
  <v-form
      class="pa-10"
      ref="form"
      v-model="valid"
      lazy-validation
  >
    <v-text-field
        v-model="email"
        :rules="emailRules"
        label="E-mail"
        required
    ></v-text-field>

    <v-text-field
        v-model="password"
        :rules="passwordRules"
        :type="show1 ? 'text' : 'password'"
        label="Password"
        required
    ></v-text-field>

    <v-btn
        color="success"
        class="mr-4"
        @click="login"
    >
      Log In
    </v-btn>
  </v-form>
</template>

<script>
import LoginDto from "../models/LoginDto.ts";
import RemoteServices from "../services/RemoteServices.ts";

export default {
  data: () => ({
    valid: true,
    email: '',
    password: '',
    show1: '',
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
    async login() {
      let token = await RemoteServices.login(new LoginDto(this.email, this.password))
      console.log(token)
    }
  }
};
</script>
