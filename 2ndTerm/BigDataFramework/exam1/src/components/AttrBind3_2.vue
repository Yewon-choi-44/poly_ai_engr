<template>

    <img :src="imagePath"/>
    <button @click="changeimg">변경</button>
</template>

<script lang="js" setup>
    import { ref } from 'vue';
    const imagePath = "https://sponsors.vuejs.org/images/chrome_frameworks_fund.png";

    const changeimg = () => {
        imagePath.value = "https://aka-dolfood.moall.shop/data/goods/sm7396/small/thum4/KakaoTalk_20260804_165859549.png";
    }
</script>

<style>
</style>
