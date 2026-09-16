<template>
    <v-container>
        <v-btn @click="show = !show">토글</v-btn>
        <Transition class="ma-4" name="custom-classes" 
        enter-active-class="animate__animated animate__tada"
        leave-active-class="animate__animated animate__flip">
        <!-- leave-active-class="animate__animated animate__bounceOutRight"> -->
        <!-- leave-active-class="animate__animated animate__wobble"> -->
        <!-- leave-active-class="animate__animated animate__jello"> -->
        <!-- leave-active-class="animate__animated animate__swing"> -->
        <!-- leave-active-class="animate__animated animate__heartBeat"> -->
        <!-- leave-active-class="animate__animated animate__headShake"> -->
        <p v-if="show">안녕</p>
        </Transition>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    const show = ref(true)
</script>

<style>
    @import '@/assets/animate.min.css';
</style>