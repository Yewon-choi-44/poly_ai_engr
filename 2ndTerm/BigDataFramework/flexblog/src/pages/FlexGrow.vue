<template>
    <div class="meal-css-tester-container ma-4 d-flex">
        <div class="meal-css-tester-item" :style="{ flexGrow: flexGrow1 }">AAA</div>
        <div class="meal-css-tester-item" :style="{ flexGrow: flexGrow2 }">BBBBBBB</div>
        <div class="meal-css-tester-item" :style="{ flexGrow: flexGrow3 }">CCCC</div>
    </div>

    <div class="ma-4">1. flex-grow: {{ flexGrow1 }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="flexGrow1">
        <template v-for="option in growOptions">
            <v-btn :text="option" :value="option"></v-btn>
        </template>
    </v-btn-toggle>

    <div class="ma-4">2. flex-grow: {{ flexGrow2 }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="flexGrow2">
        <template v-for="option in growOptions">
            <v-btn :text="option" :value="option"></v-btn>
        </template>
    </v-btn-toggle>

    <div class="ma-4">3. flex-grow: {{ flexGrow3 }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="flexGrow3">
        <template v-for="option in growOptions">
            <v-btn :text="option" :value="option"></v-btn>
        </template>
    </v-btn-toggle>
</template>

<script setup>
    import { ref } from 'vue'

    const flexGrow1 = ref("0")
    const flexGrow2 = ref("0")
    const flexGrow3 = ref("0")
    const growOptions = ref([
        "0",
        "1",
        "2",
        "3"
    ])
</script>

<style lang="scss" scoped>
    @import "@/assets/custom.css"
</style>