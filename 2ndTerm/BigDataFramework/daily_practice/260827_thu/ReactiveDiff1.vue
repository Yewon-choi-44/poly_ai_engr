<template>
    <div>
        <h1> reactive.count: {{ state1.count }} </h1>
        <h1> ref.count: {{ state2.count }} </h1>
        <button @click="test1">btn1</button>
    </div>
</template>

<script setup>
    import {ref, reactive } from 'vue'

    const state1 = reactive({ count: 0})
    const state2 = ref({ count: 0})

    const test1 = () => {
        state1.count++
        state2.value.count++
    }
</script>
