<template>
    <v-app-bar flat app clipped-right color="white" clipped>
      <div class="d-flex align-center">
        <v-card color="grey-lighten-5" outlined width="300px" class="pa-2 ml-4">
          <v-row>
            <v-col>
              <v-icon color="grey">mdi-magnify-expand</v-icon>
              <span class="ml-2 text-grey">Search</span>
            </v-col>
            <v-col class="text-right">
              <v-icon color="grey">mdi-microphone-outline</v-icon>
            </v-col>
          </v-row>
        </v-card>
      </div>
      
      <v-spacer></v-spacer>

      <v-btn variant="elevated" color="red" class="text-none mr-5">
        <span class="mr-2">
          <v-icon class="mr-2">mdi-plus</v-icon>Create New Post
        </span>
      </v-btn>
      <v-btn icon class="mr-2">
        <v-icon>mdi-email-outline</v-icon>
      </v-btn>
      <v-btn icon class="mr-5">
        <v-icon>mdi-heart-outline</v-icon>
      </v-btn>
      <v-avatar size="30">
        <img
          lazy-src="https://images.unsplash.com/photo-1549068106-b024baf5062d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80"
          src="https://images.unsplash.com/photo-1549068106-b024baf5062d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80"
          alt="John"
        />
      </v-avatar>
      <v-icon>mdi-menu-down</v-icon>
    </v-app-bar>
</template>

<script setup>

</script>

<style lang="scss" scoped>

</style>