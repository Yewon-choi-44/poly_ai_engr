<template>
  <v-container class="pa-10">
    <v-row>
      <v-col>
        <div class="text-h5 font-weight-bold">Featured Stories</div>
      </v-col>
      <v-spacer></v-spacer>
      <v-col text-right align-self="center">
        <v-btn depressed class="text-none" color="grey-lighten-4">
          <span class="text-h6 text-grey">Popular Stories</span>
        </v-btn>
      </v-col>
    </v-row>
    <v-row justify-start class="mt-7">
      <v-card
        elevation="12" 
        width="468"  
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)" 
        class="ma-4">
        <v-img
          height="468"
          cover
          src="https://images.unsplash.com/photo-1525138079-9424be9df411?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=675&q=80">
          <v-card-title class="text-white">#title</v-card-title>
        </v-img>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn size="small" color="surface-variant" variant="text" icon="mdi-heart"></v-btn>
          <v-btn size="small" color="surface-variant" variant="text" icon="mdi-bookmark"></v-btn>
          <v-btn size="small" color="surface-variant" variant="text" icon="mdi-share-variant"></v-btn>
        </v-card-actions>
        <v-divider></v-divider>
        <v-card-title class="text-blue">#title</v-card-title>
        <v-card-text>
            #content
        </v-card-text>
      </v-card>
    </v-row>

  </v-container>
</template>

<script setup>
  import { reactive } from 'vue'
  const cards = reactive([{
      src: "https://images.unsplash.com/photo-1525138079-9424be9df411?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=675&q=80", 
      title: 'title1',
      content: 'contents1 ~~ contents1'
    }, {
      src: "https://images.unsplash.com/photo-1523224949444-170258978eef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=564&q=80",
      title: 'title2',
      content: 'contents2 ~~ contents2'
    }, {
      src: "https://images.unsplash.com/photo-1551818633-579bccc6210c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80",
      title: 'title3',
      content: 'contents3 ~~~ contents3'
    }, {
      src: "https://images.unsplash.com/photo-1478296046035-d4fc77bec472?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80",
      title: 'title4',
      content: 'contents 4 ~~~ contenst4'
    }])
</script>

<style>
</style>