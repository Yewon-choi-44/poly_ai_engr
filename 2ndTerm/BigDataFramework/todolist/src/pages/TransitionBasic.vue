<template>
    <v-container>
        <v-btn @click="show = !show">토글</v-btn>
        <Transition class="ma-3">
            <p v-if="show">안녕</p>
        </Transition>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    const show = ref(true)
</script>

<style scoped>
    .v-enter-active, .v-leave-active {
        transition: opacity 3s ease;
    }
    .v-enter-from, .v-leave-to {
        opacity: 0;
    }
</style>