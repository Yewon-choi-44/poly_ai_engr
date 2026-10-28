<template>
    <div class="meal-css-tester-container ma-4 d-flex" :style="{ flexDirection }">
        <div class="meal-css-tester-item">AAA</div>
        <div class="meal-css-tester-item">BBBBBBB</div>
        <div class="meal-css-tester-item">CCCC</div>
    </div>
    <div class="ma-4">flex-direction: {{  boxDirection }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="flexDirection">
        <v-btn text="row" value="row"></v-btn>
        <v-btn text="row-reverse" value="row-reverse"></v-btn>
        <v-btn text="column-reverse" value="column-reverse"></v-btn>
    </v-btn-toggle>
</template>

<script setup>
    import { ref } from 'vue'
    const flexDirection = ref("row")
</script>

<style lang="scss" scoped>
    @import '@/assets/custom.css';
</style>