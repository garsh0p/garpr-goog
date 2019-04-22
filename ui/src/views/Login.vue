<template>
  <div>
    <h1 class="display-2">Login</h1>

    <v-form ref="form" v-model="valid">
      <v-text-field
        label="Username"
        :rules="required"
        required>
      </v-text-field>

      <v-text-field
        label="Password"
        type="password"
        :rules="required"
        required>
      </v-text-field>

      <v-btn :disabled="!valid" color="success" to="admin">
        Login
      </v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data: () => ({
    valid: false,
    required: [v => !!v || 'Field is required'],
  }),
}
</script>
