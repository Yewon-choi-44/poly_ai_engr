<template>
<span style = "color:red"><h1>아래에 자식 컴포넌트가 있습니다..</h1></span>
    <div>
        <button @click="increment">
            {{ count }}
        </button>
        {{ count1 }}
    </div>
    <div>
        {{ count2 }}
    </div>
</template>
<script>

import { ref } from 'vue'
export default {
    setup () {
        const count = ref(0)
        let count2 = 5
        const increment = () => {
            count.value++
            count2++;
        }
        return {
            count,
            count1: count,
            count2 : count2,
            increment
        }
    }
}
</script>