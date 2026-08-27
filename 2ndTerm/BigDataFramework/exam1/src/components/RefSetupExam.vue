<template>
<span style = "color:red"><h1>아래에 자식 컴포넌트가 있습니다..</h1></span>
    <button @click="increment">
        {{ count }}
    </button>
</template>

<script setup>
    import { ref } from 'vue'
    const count = ref(0)
    const increment = () => {
        count.value++
    }
    
</script>