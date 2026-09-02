<template>
    <div>
        <LifeCycleHookComp v-if="isMounted" @unmount-evt="isMounted=false" />
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    import LifeCycleHookComp from '@/components/LifeCycleHookComp.vue'
    const isMounted = ref(true)
</script>