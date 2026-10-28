<template>
    <div class="meal-css-tester-container ma-4 d-flex position-relative" style="justify-content: center;" :style="{ alignItems, height: '15rem' }">
        <div class="meal-css-tester-item" style="font-size: 30px;">AAA</div>    
        <div class="meal-css-tester-item" style="font-size: 14px;">BBBBBBB</div>    
        <div class="meal-css-tester-item" style="font-size: 50px; width: 150px;">CCCC</div>    
        <div class="meal-css-tester-item" style="font-size: 40px; width: 150px;">gggg</div>
        <div v-if="alignItems == 'baseline'" class="baseline"></div> 
    </div>

    <div class="ma-4">align-items: {{ alignItems }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="alignItems">
        <template v-for="option in options">
            <v-btn :text="option" :value="option"></v-btn>
        </template>
    </v-btn-toggle>
</template>

<script setup>
    import { ref } from 'vue'
    const alignItems = ref("stretch")
    const options = ref([
        "stretch",
        "flex-start",
        "flex-end",
        "center",
        "baseline"
    ])
</script>

<style lang="scss" scoped>
    @import '@/assets/custom.css';
</style>