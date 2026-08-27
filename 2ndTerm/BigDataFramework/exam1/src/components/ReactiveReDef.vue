<template>
    <span style= "color:red"><h1>아래에 자식 컴포넌트가 있습니다...</h1></span>
    <div>
        <h1> {{ raw }}</h1>
        <h1> {{ proxy }}</h1>
        <h1> {{ state }}</h1>
    </div>
</template>

<script setup>
    import { reactive, ref } from 'vue'
    const raw = {'vue': 'good'}
    const state = ref(raw)
    const proxy = reactive(raw)

    // 반응형으로 재정의 된 것은 원본과 같지 않습니다.
    console.log(proxy == raw) // false

    // 객체를 reactive() 한 반환 값과 프록시는 동일합니다.
    console.log(reactive(raw) === proxy) // true

    // 프록시를 reactive()한 반환 값과 프록시는 동일합니다.
    console.log(reactive(proxy) === proxy) // true

    // 객체를 ref() 한 반환 값과 state는 다르다.
    console.log(ref(raw) === state) // false
    // state를 ref() 한 반환 값과 state는 동일합니다.
    console.log(ref(state) == state) // true
</script>