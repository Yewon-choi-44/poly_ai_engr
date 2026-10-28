<template>
    <div class="meal-css-tester-container ma-4 d-flex" :style="{ justifyContent }">
        <div class="meal-css-tester-item">AAA</div>
        <div class="meal-css-tester-item">BBBBBBB</div>
        <div class="meal-css-tester-item">CCCC</div>
    </div>
    <div class="ma-4">justify-content: {{ justifyContent }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="justifyContent">
        <template v-for="option in justifyOptions">
            <v-btn :text="option" :value="option"></v-btn>
        </template>
    </v-btn-toggle>
</template>

<script setup>
    import { ref } from 'vue'
    const justifyContent = ref("flex-start")
    const justifyOptions = ref([
        "flex-start",
        "flex-end",
        "center",
        "space-between",
        "space-around",
        "space-evenly"
    ])  
</script>

<style lang="scss" scoped>
    @import '@/assets/custom.css';
</style>