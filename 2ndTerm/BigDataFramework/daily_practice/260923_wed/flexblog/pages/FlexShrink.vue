<template>
    <div class="meal-css-tester-container ma-4 d-flex" ref="flexContainer">
        <div class="meal-css-tester-item d-flex" :style="{ flexBasis: `${width1}px`, flexShrink: flexShrink1 }">
            A {{ shrinkw }} x ({{ width1 }} x {{ flexShrink1 }} / {{ basisWeightSum }}) 
            = {{ (shrinkw * width1 * flexShrink1 / basisWeightSum).toFixed(0) }}
            <div class="v-line"></div>
        </div>
        <div class="meal-css-tester-item d-flex" :style="{ flexBasis: `${width2}px`, flexShrink: flexShrink2 }">
            A {{ shrinkw }} x ({{ width2 }} x {{ flexShrink2 }} / {{ basisWeightSum }}) 
            = {{ (shrinkw * width2 * flexShrink2 / basisWeightSum).toFixed(0) }}
            <div class="v-line"></div>
        </div>
        <div class="meal-css-tester-item d-flex" :style="{ flexBasis: `${width3}px`, flexShrink: flexShrink3 }">
            A {{ shrinkw }} x ({{ width3 }} x {{ flexShrink3 }} / {{ basisWeightSum }}) 
            = {{ (shrinkw * width3 * flexShrink3 / basisWeightSum).toFixed(0) }}
            <div class="v-line"></div>
        </div>
    </div>

    <div class="ma-4">
        <div>컨테이너 width : {{ containerWidth }}px</div>
        <div>아이템 기본 width 합계 : {{ width1 + width2 + width3 }}px</div>
        <div>아이템 줄어든 width 합계 : {{ width1 + width2 + width3 - containerWidth }}px</div>
    </div>

    <div class="ma-4">1. flex-shrink: {{ flexShrink1 }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="flexShrink1">
        <template v-for="option in options">
            <v-btn :text="`${option}`" :value="option"></v-btn>
        </template>
    </v-btn-toggle>

    <div class="ma-4">2. flex-shrink: {{ flexShrink2 }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="flexShrink2">
        <template v-for="option in options">
            <v-btn :text="`${option}`" :value="option"></v-btn>
        </template>
    </v-btn-toggle>

    <div class="ma-4">3. flex-shrink: {{ flexShrink3 }}</div>
    <v-btn-toggle variant="outlined" divided class="ma-4" v-model="flexShrink3">
        <template v-for="option in options">
            <v-btn :text="`${option}`" :value="option"></v-btn>
        </template>
    </v-btn-toggle>
</template>

<script setup>
    import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
    const flexContainer = ref(null)
    const containerWidth = ref(0)
    const width1 = ref(200)
    const width2 = ref(300)
    const width3 = ref(300)
    const flexShrink1 = ref(1)
    const flexShrink2 = ref(1)
    const flexShrink3 = ref(1)
    const shrinkw = ref(0)
    const basisWeightSum = computed(() => {
        return width1.value * flexShrink1.value + width2.value * flexShrink2.value + width3.value * flexShrink3.value
    })
    const updateDivWidth = () => {
        console.log(flexContainer.value)
        containerWidth.value = flexContainer.value.clientWidth
        shrinkw.value = containerWidth.value - width1.value - width2.value - width3.value
    };

    onMounted(() => {
        updateDivWidth();
        window.addEventListener('resize', updateDivWidth);
    })

    onBeforeUnmount(() => {
        window.removeEventListener('resize', updateDivWidth);
    })

    const options = ref([
        0,
        1,
        2,
        3
    ])
</script>

<style lang="scss scoped">
    @import "@/assets/custom.css";
</style>
