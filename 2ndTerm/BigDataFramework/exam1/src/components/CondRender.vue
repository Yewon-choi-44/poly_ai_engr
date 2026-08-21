<template>
    <button @click="toggle">전환</button>
    <br>
    <h1 v-if="awesome">v-if Vue is awesome!</h1>
    <br>
    <h1 v-show="!awesome">v-show Vue is awesome!</h1>
</template>

<script setup>
    import { ref } from 'vue';

    const awesome = ref(true);
    function toggle() {
        awesome.value = !awesome.value
    }
</script>

<style>
</style>