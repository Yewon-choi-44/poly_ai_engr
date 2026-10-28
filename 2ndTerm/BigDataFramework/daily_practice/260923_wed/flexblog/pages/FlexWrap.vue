<template>
    <div class="meal-css-tester-container ma-4 d-flex" :style="{flexWrap, width: '13rem'}">
        <div class="meal-css-tester-item">AAA</div>
        <div class="meal-css-tester-item">BBBBBBB</div>
        <div class="meal-css-tester-item">CCCC</div>
    </div>
    <div class="ma-4">flex-wrap: {{ flexWrap }}</div>
    <v-btn-toggle
        variant="outlined" divided class="ma-4" v-model="flexWrap">
        <v-btn text="nowrap" value="nowrap"></v-btn>
        <v-btn text="wrap" value="wrap"></v-btn>
        <v-btn text="wrap-reverse" value="wrap-reverse"></v-btn>
    </v-btn-toggle>
</template>

<script setup>
    import { ref } from 'vue'
    const flexWrap = ref("nowrap")
</script>

<style lang="scss" scoped>
    @import '@/assets/custom.css';
</style>
