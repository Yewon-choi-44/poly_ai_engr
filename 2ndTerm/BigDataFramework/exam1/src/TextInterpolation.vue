<template>
    <span>Message: {{ msg }} </span>
</template>
<script lang = "js" setup>
    import { ref } from 'vue';
    const msg = ref("Hello");
</script>