<template>
    <div class="meal-css-tester-container ma-4 d-flex">
        <div class="meal-css-tester-item" :style="{ flexBasis, flexGrow }">AAA</div>
        <div class="meal-css-tester-item" :style="{ flexBasis, flexGrow }">BBBBBBBBB</div>
        <div class="meal-css-tester-item" :style="{ flexBasis, flexGrow }">CCCC</div>
    </div>
    <div class="ma-4">flex-basis: {{ flexBasis }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="flexBasis">
        <template v-for="option in basisOptions">
            <v-btn :text="option" :value="option"></v-btn>
        </template>
    </v-btn-toggle>

    <div class="ma-4">flex-grow: {{  flexGrow  }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="flexGrow">
        <template v-for="option in growOptions">
            <v-btn :text="option" :value="option"></v-btn>
        </template>
    </v-btn-toggle>
</template>

<script setup>
    import { ref } from 'vue'
    const flexBasis = ref("auto")
    const basisOptions = ref([
        "auto",
        "50%",
        "200px",
        "content"
    ])

    const flexGrow = ref("0")
    const growOptions = ref([
        "0",
        "1"
    ])
</script>

<style lang="scss" scoped>
    @import '@/assets/custom.css';
</style>