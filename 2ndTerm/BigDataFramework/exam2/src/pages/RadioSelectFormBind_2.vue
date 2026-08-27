<script setup>
    import { ref } from 'vue'
    const picked = ref(null)
    const selected = ref(null)
    const option_value = ref('https://velog.io/@minsu2344/Vue-v-model%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-select-checkbox-radio-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B0%94%EC%9D%B8%EB%94%A9')
</script>

<template>
    <v-container class="ma-2">
        <v-row class="ma-2">
            <v-col>
                <div>라디오 바인딩</div>
                <div>선택한 것: {{ picked }}</div>
                <input type="radio" id="one" value="하나" v-model="picked" />
                <label for="one">하나</label>
                <input type="radio" id="two" value="둘" v-model="picked" />
                <label for="two">둘</label>
            </v-col>
        </v-row>

        <v-divider></v-divider>
        <v-row class="ma-2">
            <v-col>
                <div>셀렉트 바인딩></div>
                <div>선택됨: {{ selected }}</div>
                <select class="outlined" v-model="selected">
                    <option disabled value="">다음 중 하나를 선택하세요.</option>
                    <option value="1">가</option>
                    <option value="2">나</option>
                    <option value="3">다</option>
                </select>
            </v-col>
        </v-row>
        <a :href="option_value" target="_blank" rel="noopener noreferrer">양방향 바인딩</a>
    </v-container>

</template>

<style scoped>
    .outlined {
        border-style: solid;
        appearance: auto;
    }
</style>

