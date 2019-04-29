<template>
    <v-card class="mb-3">
      <v-card-title class="headline">
        Rankings Control Panel
      </v-card-title>
      <v-card-text>
        <v-container>
          <h2 class="title">Ranking Qualification</h2>
          <v-form>
            <v-text-field
                    label="Must have attended at least"
                    type="number"
                    suffix="tournament(s)"
                    v-model="minAttendence">
            </v-text-field>
            <v-text-field
                    label="Over the past"
                    type="number"
                    suffix="days"
                    v-model="daysBack">
            </v-text-field>

            <h2 class="title">Tournament Inclusion</h2>
            <v-text-field
                    label="Include tournaments from the past"
                    type="number"
                    suffix="days"
                    v-model="rankingPeriod">
            </v-text-field>

            <h2 class="title">TrueSkill Parameters</h2>
            <v-text-field
                    label="mu"
                    hint="The initial mean of ratings. (default: 25)"
                    type="number"
                    v-model="trueskill.mu">
            </v-text-field>
            <v-text-field
                    label="sigma"
                    hint="The initial standard deviation of ratings. The recommended value is a mu/3. (default: 8.33)"
                    type="number"
                    v-model="trueskill.sigma">
            </v-text-field>
            <v-text-field
                    label="tau"
                    hint="The dynamic factor which restrains a fixation of rating. The recommended value is sigma/100. (default: 0.083)"
                    type="number"
                    v-model="trueskill.tau">
            </v-text-field>

            <v-btn color="error">Recalculate Rankings</v-btn>
          </v-form>
        </v-container>
      </v-card-text>
    </v-card>
</template>

<script>
export default {
  data: () => ({
    daysBack: 60,
    minAttendence: 1,
    rankingPeriod: 999,

    trueskill: {
      mu: 25.0,
      sigma: 8.33,
      tau: .083,
    },
  })
}
</script>
