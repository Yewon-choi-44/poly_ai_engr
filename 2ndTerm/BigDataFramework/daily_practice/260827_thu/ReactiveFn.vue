<template>
    <span style= "color:red"><h1>아래에 자식 컴포넌트가 있습니다...</h1></span>
    <div>
        <button @click="increment">
            {{ state.count }}
        </button>
    </div>
</template>

<script setup>
    import { reactive } from 'vue'
    const state = reactive({ count: 0 })
    const increment = () => {
        state.count++
    }
</script>