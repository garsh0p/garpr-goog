<template>
  <div>
    <h1 class="display-2">Edit Tournament</h1>

    <v-tabs>
      <v-tab ripple :key="1">
        Players
      </v-tab>
      <v-tab ripple :key="2">
        Matches
      </v-tab>

      <v-tab-item :key="1">
        <v-data-table
            hide-actions
            :headers="playerHeaders"
            :items="players"
            class="elevation-1">

          <template v-slot:items="props">
            <td>
              <v-checkbox hide-details v-model="props.item.isNew">
              </v-checkbox>
            </td>
            <td>
              <v-text-field v-model="props.item.tag"
                            :label="props.item.originalTag"
                            clearable>
              </v-text-field>
            </td>
          </template>
        </v-data-table>
      </v-tab-item>

      <v-tab-item :key="2">
        <v-data-table hide-actions
                      :headers="headers"
                      :items="matches"
                      class="elevation-1">

            <template v-slot:items="props">
              <td>
              {{props.item.round}}
            </td>
              <td style="color: green"
                  :style="tagStyles(props.item)">
                {{props.item.winner}}
              </td>
            <td>
              <v-btn icon @click="swapWinner(props.item)">
                <v-icon>swap_horiz</v-icon>
              </v-btn>
            </td>
            <td style="color: red"
                :style="tagStyles(props.item)">
              {{props.item.loser}}
            </td>
            <td>
              <v-checkbox v-model="props.item.exclude" hide-details>
              </v-checkbox>
            </td>
          </template>
        </v-data-table>
      </v-tab-item>
      </v-tabs>
  </div>
</template>

<script>
export default {
  data: () => ({
    headers: [
      {text: 'Round', value: 'round', sortable: false, width: '1%'},
      {text: 'Winner', value: 'winner', sortable: false},
      {text: '', value: 'swap', sortable: false},
      {text: 'Loser', value: 'loser', sortable: false},
      {text: 'Exclude', value: 'exclude', sortable: false, width: '1%'},
    ],

    matches: [
      {round: 'WR1', winner: 'Ryan', loser: 'Lane', exclude: false, swapped: false},
      {round: 'WR1', winner: 'DJSwerve', loser: 'LaneOG', exclude: false, swapped: false},
    ],

    playerHeaders: [
      {text: 'New Player?', value: 'isNew', sortable: false, width: '1%'},
      {text: 'Tag', value: 'tag', sortable: false},
    ],

    players: [
      {tag: null, originalTag: 'Ryan', isNew: false},
      {tag: null, originalTag: 'Lane', isNew: false},
      {tag: null, originalTag: 'DJSwerve', isNew: false},
      {tag: null, originalTag: 'LaneOG', isNew: false},
    ],
  }),
  methods: {
    swapWinner: function(item) {
      [item.winner, item.loser] = [item.loser, item.winner];
      item.swapped = !item.swapped;
    },

    tagStyles: function(item) {
      let style = {};
      if (item.swapped) {
        style.fontWeight = 'bold';
      }
      if (item.exclude) {
        style.textDecoration = 'line-through';
      }

      return style;
    },
  },
}
</script>
