<template>
    <div class="ma-4">
        <ChildExpose ref = "child" />
        <div>child ref: {{ child }}</div>
        <v-btn @click="test">테스트</v-btn>
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    import ChildExpose from '@/componets/ChildExpose.vue';

    const child = ref(null)
    const test = () => {
        console.log(child.value)
        child.value.open()
    }

</script>