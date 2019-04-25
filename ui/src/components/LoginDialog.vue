<template>
    <v-dialog v-model="dialog" max-width="290">
      <v-card>
        <v-card-title class="headline">Login</v-card-title>

        <v-card-text>
          <v-container>
          <v-form v-model="valid">
            <v-text-field label="Username"
                          :rules="required"
                          required>
            </v-text-field>

            <v-text-field label="Password"
                          v-model="password"
                          type="password"
                          :rules="required"
                          required>
            </v-text-field>
          </v-form>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="primary"
                 flat
                 :disabled="!valid"
                 @click.stop="dialog=false">
                 Login
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
export default {
  props: {
    value: Boolean,
  },
  computed: {
    dialog: {
      get() {
        return this.value;
      },
      set(value) {
        if (!value) {
          this.password = '';
        }
        this.$emit('input', value);
      },
    }
  },
  data: () => ({
    password: '',
    valid: false,
    required: [v => !!v || 'Field is required'],
  })
}
</script>
