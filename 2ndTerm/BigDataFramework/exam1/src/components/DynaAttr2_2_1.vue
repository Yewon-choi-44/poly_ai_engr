<template>
    <p><span v-html="DynaAttr2_2_1"></span></p>
   <div>
    <div v-bind="objectOfAttrs">div</div>
   </div>
</template>

<script lang = "js" setup>
    import { ref } from 'vue';
    const DynaAttr2_2_1 = '<span style = "color:red"><h1>아래에 자식 컴포넌트가 있습니다..</h1></span>';
    const objectOfAttrs = {
        id: 'container',
        class: 'wrapper',
        style:'red'
    }    
</script>


<style>
</style>
