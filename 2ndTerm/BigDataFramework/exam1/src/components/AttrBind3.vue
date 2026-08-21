<template>
    <p>이미지 URL {{ imagePath }} </p>
    <br>
    <img :src="imagePath"/>
</template>

<script lang="js" setup>
    import { ref } from 'vue';
    const imagePath = "https://sponsors.vuejs.org/images/chrome_frameworks_fund.png";
</script>

<style>
</style>