<template>
    <button @click="increment">1 추가</button>
    <br>
    <p>숫자 값은: {{ count }}</p>
</template>

<script setup>
    import { ref } from 'vue';

    const count = ref(0);
    function increment() {
        count.value++;
    }
</script>

<style>
</style>