<template>
  <div>
    <h1 class="display-2">Add Tournament</h1>
    <v-stepper v-model="step">
      <v-stepper-header>
        <v-stepper-step :complete="step > 1" step="1" editable>Upload Tournament</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="step > 2" step="2">Fix Tags</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">Verify</v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <v-form v-model="valid">
            <v-text-field v-model="tournamentUrl"
                          label="Tournament URL"
                          :rules="urlRules"
                          required>
            </v-text-field>

            <!-- TODO: Call the gaR upload endpoint. -->
            <v-btn
              color="primary"
              @click="step = 2"
              :disabled="!valid"
              >
              Upload
            </v-btn>
          </v-form>
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-card
            class="mb-5"
            color="grey lighten-1"
            height="200px"
            ></v-card>

          <v-btn
            color="primary"
            @click="step = 3"
            >
            Continue
          </v-btn>

            <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-content step="3">
          <v-card
            class="mb-5"
            color="grey lighten-1"
            height="200px"
            ></v-card>

          <v-btn
            color="primary"
            @click="step = 0"
            >
            Continue
          </v-btn>

            <v-btn flat>Cancel</v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </div>
</template>

<script>
export default {
  data: () => ({
    step: 1,
    tournamentUrl: '',
    valid: false,

    urlRules: [
      v => !!v || 'URL is required',
      v => /challonge.com\/.+/.test(v) || 'URL must be valid',
    ],
  }),
}
</script>
