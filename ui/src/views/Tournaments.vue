<template>
  <div>
    <v-layout row>
      <v-flex grow>
        <h1 class="display-2">Tournaments</h1>
      </v-flex>
      <v-btn
            v-if="loggedIn"
            color="error"
            @click.stop="uploadDialog=true">
        Upload a Tournament
      </v-btn>
      <UploadDialog v-model="uploadDialog" />
    </v-layout>

    <v-data-table
      hide-actions
      :headers="headers"
      :items="tournaments"
      class="elevation-1">

      <template v-slot:items="props">
        <td>{{props.item.date}}</td>
        <td>{{props.item.name}}</td>
        <td v-if="loggedIn">
          <v-btn icon>
            <v-icon>delete
            </v-icon>
          </v-btn>
        </td>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import UploadDialog from '@/components/UploadDialog.vue';

export default {
  components: {
    UploadDialog,
  },
  data: () => ({
    loggedIn: false,
    uploadDialog: false,

    allHeaders: [
      {text: 'Date', value: 'date', sortable: false, width: '1%'},
      {text: 'Name', value: 'name', sortable: false},
      {text: '', value: 'delete', sortable: false},
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
  computed: {
    headers: function() {
      if (!this.loggedIn) {
        return this.allHeaders.slice(0, -1);
      }

      return this.allHeaders;
    }
  },
}
</script>
