<template>
    <div>
        <h1 reactive({{ state1 }}) </h1>
        <h1> ref({{ state2 }}) </h1>
        <button @click="test1">btn1</button>
        <button @click="test2">btn2</button>
    </div>
</template>

<script setup>
    import { ref, reactive } from 'vue'
    const state1 = reactive({ count: 0})
    const state2 = ref({ count: 0})

    const callSomeFn1 = (c) => { c += 15 }
    const callSomeFn2 = (c) => { c.count += 15 }
    const callSomeFn3 = (c) => { c.value.count += 15 }

    const test1 = () => {
        callSomeFn1(state1.count)
        callSomeFn1(state2.value.count)
    }
    const test2 = () => {
        callSomeFn2(state1)
        callSomeFn3(state2)
    }
</script>