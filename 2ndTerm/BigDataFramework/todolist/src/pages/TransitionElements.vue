<template>
    <v-container>
        <span style = "margin-right: 20px;">클릭 시 상태 변경:</span>
        <div class = "my-4" style = "height: 100px;">
            <Transition name="slide-up">
                <v-btn v-if="docState === 'saved'" prepend-icon="$vuetify" @click="docState === 'edited'">수정</v-btn>
                <v-btn v-else-if="docState === 'edited'" prepend-icon="$vuetify" @click="docState === 'editing'">저장</v-btn>
                <v-btn v-else-if="docState === 'editing'" prepend-icon="$vuetify" @click="docState === 'saved'">취소</v-btn>
            </Transition>
        </div>
        
        <span style = "margin-right: 20px">클릭 시 상태 변경(out-in):</span>
        <div class = "btn-container my-4" style = "height: 100px;">
            <v-btn v-if="docState1 === 'saved'" prepend-icon="$vuetify" color="indigo" @click="docState1 === 'edited'">수정</v-btn>
            <v-btn v-else-if="docState1 === 'edited'" prepend-icon="$vuetify" color="indigo" @click="docState1 === 'editing'">저장</v-btn>
            <v-btn v-else-if="docState1 === 'editing'" prepend-icon="$vuetify" color="indigo" @click="docState1 === 'saved'">취소</v-btn>
        </div>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    const docState = ref('saved')
    const docState1 = ref('saved')
</script>

<style scoped>
    button {
        position: absolute;
        white-space: pre;
    }

    .slide-up-enter-active,
    .slide-up-leave-active {
        transition: all 0.25s ease-out;
    }

    .slide-up-enter-from {
        opacity: 0;
        transform: translateY(30px);
    }

    .slide-up-leave-to {
        opacity: 0;
        transform: translateY(-30px);
    }
</style>