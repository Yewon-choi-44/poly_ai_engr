<template>
    <span style = "color:red"><h1>아래에 자식 컴포넌트가 있습니다...</h1></span>
    <h1 class = "counter" ref="h1Ref">{{ count1 }}</h1>
    <button @click="increment">increment</button>
    <button @click="withoutTick">nextTick 없이</button>
    <button @click="withTick">nextTick 있이</button>
</template>

<script setup>
import { ref, nextTick } from 'vue'
const count1 = ref(0)
const h1Ref = ref(null)
const sleep = (ms) => new Promise(r => setTimeout(r, ms))

const withoutTick = () => {
    count1.value += 1
    console.log('DOM 즉시 확인:', h1Ref.value.textContent) // dom 반영 전
}
const withTick = async () => {
    count1.value +=1
    await nextTick()
    console.log('DOM nextTick 후 확인:', h1Ref.value.textContent) // dom 반영
}
const increment = async () => {
    for (let i=0 ; i<5 ; i++){
        count1.value += 1
        await nextTick()
        await sleep(400)
    }
}
</script>

<style scoped>
    .counter {
        transition: all 0.3s ease;
    font-size: 3rem;
    }
</style>