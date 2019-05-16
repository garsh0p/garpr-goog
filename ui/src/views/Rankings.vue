<template>
  <div>
    <RankingsControlPanel v-if="loggedIn" />

    <h1 class="display-2">Rankings</h1>

    <v-data-table
      hide-actions
      :headers="headers"
      :items="players"
      class="elevation-1">

      <template v-slot:items="props">
        <td><!-- TODO: Rank up/down --></td>
        <td class="font-weight-bold">{{props.item.rank}}</td>
        <td>{{props.item.name}}</td>
        <td>{{props.item.rating}}</td>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import RankingsControlPanel from '@/components/RankingsControlPanel.vue'

export default {
  components: {
    RankingsControlPanel,
  },
  data: () => ({
    loggedIn: true,

    headers: [
      {text: '', value: 'delta', sortable: false, width: '1%'},
      {text: 'Rank', value: 'rank', sortable: false, width: '1%'},
      {text: 'Name', value: 'name', sortable: false},
      {text: 'Rating', value: 'rating', sortable: false},
    ],

    // TODO: Make that API call.
    players: [
      {delta: 0, rank: 1, name: 'gaR', rating: 35.091},
      {delta: 0, rank: 2, name: 'Bryan', rating: 34.908},
      {delta: 0, rank: 3, name: 'emoDinosaur', rating: 33.453},
      {delta: 0, rank: 4, name: 'Neal', rating: 32.751},
    ],
  }),
}
</script>
