<script setup>
    import { ref } from 'vue'
    const picked = ref(null)
    const selected = ref(null)
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
                    <option>가</option>
                    <option>나</option>
                    <option>다</option>
                </select>
            </v-col>
        </v-row>
    </v-container>
</template>

<style scoped>
    .outlined {
        border-style: solid;
        appearance: auto;
    }
</style>

