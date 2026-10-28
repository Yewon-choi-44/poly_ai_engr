<template>
 
    <v-hover v-slot="{ isHovering, props }">
    <v-card 
        elevation="12"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        class="ma-4 card-item"
        width="100%"
        v-bind="props">
        <v-overlay
          :model-value="isHovering"
          class="align-center justify-center"
          scrim="#036358"
          contained>
          <!-- <v-img class="" -->
        </v-overlay>
        <v-card-title>{{ item.title }}</v-card-title>
        <v-card-subtitle>{{ item.content }}</v-card-subtitle>
        <v-card-text>{{ item.author }} </v-card-text>
        <v-file>{{ item.picture1 }}</v-file>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn variant="mdi-book-open-page-variant" prepend-icon="mdi-book-open-page-variant" :to="`item/${item.id}`">
                더보기
            </v-btn>
            <v-btn size="small" color="surface-variant"
                variant="text" icon="mdi-heart"></v-btn>
                <v-btn size="small" color="surface-variant"
                variant="text" icon="mdi-bookmark"></v-btn>
                <v-btn size="small" color="surface-variant"
                variant="text" icon="mdi-share-variant"></v-btn>
        </v-card-actions>
    </v-card>
    </v-hover>
</template>

<script setup>
defineProps(['item'])
</script>

<style scoped>
    .hover {
        height: 100%;
        width: 100%;
        position: absolute;
        display: flex;
        justify-content: center;
        align-items: center;
        opacity: 0.6;
    }
    .hover-btn {
        opacity: 1;
    }
</style>