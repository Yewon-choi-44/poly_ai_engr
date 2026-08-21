<template>
   <div>
    <div v-bind="objectOfAttrs">div</div>
   </div>
</template>

<script lang = "js" setup>
    import { ref } from 'vue';
    const objectOfAttrs = {
        id: 'container',
        class: 'wrapper'
    }    
</script>

<style>
</style>
