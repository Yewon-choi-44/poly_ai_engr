<template>
    <div>{{ number + 1 }}</div><br>
    <div>{{ ok ? '예': '아니오' }}</div><br>
    <div>{{ message.split('').reverse().join('')}}</div><br>
    <div :id="`list-${id}`"> div{{ `list-${id}` }}</div><br>
</template>

<script lang="js" setup>
    import { ref } from 'vue';
    
    const number = 1;
    const ok = true;
    const message = '안녕하세요';
    const id = 7;

</script>

<style>
</style>