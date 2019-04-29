<template>
  <div>
    <h1 class="display-2">Edit Tournament</h1>

    <v-tabs v-model="activeTab">
      <v-tab ripple :key="1">
        Players
      </v-tab>
      <v-tab ripple :key="2">
        Matches
      </v-tab>

      <v-tab-item :key="1">
        TODO
      </v-tab-item>

      <v-tab-item :key="2">
        <v-data-table
        hide-actions
        :headers="headers"
        :items="matches"
        class="elevation-1">

          <template v-slot:items="props">
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
              <v-checkbox v-model="props.item.exclude"></v-checkbox>
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
    activeTab: 2,
    headers: [
      {text: 'Winner', value: 'winner', sortable: false},
      {text: '', value: 'swap', sortable: false},
      {text: 'Loser', value: 'loser', sortable: false},
      {text: 'Exclude', value: 'exclude', sortable: false, width: '1%'},
    ],

    matches: [
      {winner: 'Ryan', loser: 'Lane', exclude: false, swapped: false},
      {winner: 'DJSwerve', loser: 'LaneOG', exclude: false, swapped: false},
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
