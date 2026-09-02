<template>
    <div>
        {{ a }}, {{ b }}
    </div>
    <div v-if="shown">
        Shown!
    </div>
</template>

<script setup>
    import { ref, defineExpose } from 'vue'
    const a = 1
    const b = ref(2)
    const shown = ref(false)
    const open = () => (shown.value = true)
    defineExpose({ a, b, open })
</script>