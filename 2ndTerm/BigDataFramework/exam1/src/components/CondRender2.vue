<template>
    <button @click="toggle">전환</button><br>
    <h1 v-if="type === 'A'">A!</h1>
    <h1 v-else-if="type === 'B'">B!</h1>
    <h1 v-else-if="type === 'C'">C!</h1>
    <h1 v-else>A/B/C 아님</h1>
</template>

<script setup>
    import { ref } from 'vue';
    const type = ref('A');
    const toggle = () => {
        switch(type.value) {
            case 'A': type.value = 'B'; break;
            case 'B': type.value = 'C'; break;
            case 'C': type.value = 'D'; break;
            default: type.value = 'A'; break;
        }
    }
</script>
