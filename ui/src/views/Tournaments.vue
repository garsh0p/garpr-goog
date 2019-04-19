<template>
  <div>
    <h1 class="display-2">Tournaments</h1>

    <v-data-table
      hide-actions
      :headers="headers"
      :items="tournaments"
      class="elevation-1">

      <template v-slot:items="props">
        <td>{{props.item.date}}</td>
        <td>{{props.item.name}}</td>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  data: () => ({
    headers: [
      {text: 'Date', value: 'date', sortable: false, width: '1%'},
      {text: 'Name', value: 'name', sortable: false},
    ],

    // TODO: Make that API call.
    tournaments: [
      {date: '04/12/19', name: "MTV Melee 112 Amateur's Bracket"},
      {date: '04/11/19', name: "MTV Melee 112"},
      {date: '03/29/19', name: "MTV Melee 111 Amateur's Bracket"},
      {date: '03/28/19', name: "MTV Melee 111"},
      {date: '03/22/19', name: "MTV Melee 110 Amateur's Bracket"},
      {date: '03/21/19', name: "MTV Melee 110"},
    ],
  }),
}
</script>
