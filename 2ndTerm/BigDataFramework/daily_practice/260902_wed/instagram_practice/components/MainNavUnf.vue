<template>
  <v-navigation-drawer color="grey-lighten-4" floating class="pa-4" app permanent>
  
    <v-row class="pa-1">
      <v-col>
        <v-img
          width="130px"
          lazy-src="../assets/instagram_logo.png"
          src="../assets/instagram_logo.png"
        ></v-img>
      </v-col>
    </v-row>

    <v-row class="mt-10" justify="center">
      <v-col cols="auto">
          <v-avatar class="outlined" size="100">
            <v-avatar size="90">
              <v-img
                lazy-src="../assets/leo_messi.jpg"
                src="../assets/leo_messi.jpg"
              />
            </v-avatar>
          </v-avatar>
        </v-col>
   </v-row>
   <v-row justify="center" >
      <v-col cols="auto">
      <div class="mt-1 text-h6 font-weight-bold text-center">Leo Messi</div>
      <div class="text-subtitle-2 text-grey text-center">Miami, South Florida</div>
      </v-col>
    </v-row>
   
    <v-row justify="center">
        <v-col cols="auto">
          <div class="text-subtitle-2 font-weight-bold">Post</div>
          <div class="text-subtitle-2 text-grey text-center">1094</div>
        </v-col>
        <v-col cols="auto">
          <div class="text-subtitle-2 font-weight-bold">Followers</div>
          <div class="text-subtitle-2 text-grey text-center">4.8억</div>
        </v-col>
        <v-col cols="auto">
          <div class="text-subtitle-2 font-weight-bold">Following</div>
          <div class="text-subtitle-2 text-grey text-center">299</div>
        </v-col>
    </v-row>

    <v-list dense nav active-class="text-red font-weight-bold" class="mt-10">
        <v-list-item :value="title" :prepend-icon="icon">
          <v-list-item-title>{{ title }}</v-list-item-title>
        </v-list-item>
        
        <!--<v-list-item  
          v-for="[icon, title] in menu"
          :value="title"
          :prepend-icon="icon">
          <v-list-item-title>{{ title }}</v-list-item-title>
        </v-list-item>-->
    </v-list>
  </v-navigation-drawer>
</template>

<script setup>
  import { reactive, ref } from 'vue'

  const title = ref('Feed')
  const icon = ref('mdi-home-outline')

  const menu = reactive([
    ['mdi-home-outline', 'Feed'],
    ['mdi-compass-outline', 'Explore'],
    ['mdi-pound', 'Trending'],
    ['mdi-check-decagram', 'Top Post'],
    ['mdi-account-outline', 'People'],
    ['mdi-bell-outline', 'Notification'],
    ['mdi-send-outline', 'Direct'],
    ['mdi-chart-pie', 'Status'],
    ['mdi-cog-outline', 'Settings']
  ])
</script>

<style>
.v-avatar.outlined {
  border: 2px solid #e7596f;
  background-color: transparent;
  border-radius: 50%;
  height: 100px;
  width: 100px;
}
</style>