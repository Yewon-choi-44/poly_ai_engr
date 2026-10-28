<template>
    <div class="meal-css-tester-container ma-4 d-flex align-center" :style="{ height: '15rem'}" >
        <div class="meal-css-tester-item d-flex" :style="{ alignSelf: alignSelf1 }">aaaaaa</div>
        <div class="meal-css-tester-item d-flex" :style="{ alignSelf: alignSelf2 }">bbbbbbbbbbb</div>
        <div class="meal-css-tester-item d-flex" :style="{ alignSelf: alignSelf3 }">Gggg</div>
    </div>

    <div class="ma-4">1. align-self1: {{  alignSelf1  }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="alignSelf1">
        <template v-for="option in options">
            <v-btn :text="option" :value="option"></v-btn>
        </template>
    </v-btn-toggle>

    <div class="ma-4">2. align-self2: {{ alignSelf2 }}</div>
     <v-btn-toggle variant="outlined" divided class="ma-4" v-model="alignSelf2">
        <template v-for="option in options">
            <v-btn :text="option" :value="option"></v-btn>
        </template>
    </v-btn-toggle>

    <div class="ma-4">2. align-self3: {{ alignSelf3 }}</div>
     <v-btn-toggle variant="outlined" divided class="ma-4" v-model="alignSelf3">
        <template v-for="option in options">
            <v-btn :text="option" :value="option"></v-btn>
        </template>
    </v-btn-toggle>
</template>

<script setup>
    import { ref } from 'vue'

    const alignSelf1 = ref("auto")
    const alignSelf2 = ref("auto")
    const alignSelf3 = ref("auto")
    const options = ref([
        "auto",
        "stretch",
        "flex-start",
        "flex-end",
        "center",
        "baseline"
    ])
</script>

<style lang="scss" scoped>
    @import "@/assets/custom.css";
</style>