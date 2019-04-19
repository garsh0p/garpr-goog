<template>
  <div>
    <h1 class="display-2">Login</h1>

    <v-form ref="form" v-model="valid">
        <v-text-field
            label="Username"
            :rules="[v => !!v || 'Field is required']"
            required>
        </v-text-field>

        <v-text-field
            label="Password"
            type="password"
            :rules="[v => !!v || 'Field is required']"
            required>
        </v-text-field>

        <v-btn :disabled="!valid" color="success">
            Login
        </v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
    data: () => ({
        valid: true,
    }),
}
</script>
