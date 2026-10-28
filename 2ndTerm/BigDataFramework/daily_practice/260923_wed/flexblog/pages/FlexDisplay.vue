<template>
    <div class="meal-css-tester-container ma-4" :style="{ display: boxDisplay }">
        <div class = "meal-css-tester-item">AAA</div>
        <div class = "meal-css-tester-item">BBBBBBB</div>
        <div class = "meal-css-tester-item">CCCCC</div>
    </div>

    <div class="ma-4">display: {{ boxDisplay }}</div>
    <v-btn-toggle
        variant = "outlined"
        divided class = "ma-4"
        v-model = "boxDisplay">
        <v-btn text="block" value="block"></v-btn>
        <v-btn text="flex" value="flex"></v-btn>
    </v-btn-toggle>
</template>

<script setup>
    import { ref } from 'vue'
    const boxDisplay = ref("block")
</script>

<style lang="css">
    @import '@/assets/custom.css';
</style>
