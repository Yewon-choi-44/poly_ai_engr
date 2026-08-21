<template> 
    <p> 텍스트 보간법 사용: {{ rawHtml }} </p>
    <br>
    <p> v-html 디렉티브 사용: <span v-html="rawhtml"></span></p>
</template>

<script lang="js" setup>
    import { ref } from 'vue';
    const rawHtml = '<span style = "color:red">이것은 빨간색이어야 합니다.</span>';
</script>

<style>
</style>