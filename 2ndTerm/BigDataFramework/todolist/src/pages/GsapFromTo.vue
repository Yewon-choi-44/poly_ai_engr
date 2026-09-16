<template>
    <div class="container">
        <div class="box gradient-green green"></div>
        <div class="box gradient-purple purple"></div>
        <div class="box gradient-blue blue"></div>
    </div>
</template>

<script setup>
    import gsap from 'gsap';
    import { onMounted } from 'vue';

    onMounted(() => {
        gsap.to(".green", {rotation:96000, x: 150, duration: 30});
        gsap.from(".purple", {rotation: -96000, x: -200, duration: 30});
        gsap.fromTo(".blue", {x: -100}, {rotation: 360, x: 200, duration: 1});
    })
</script>

<style >
    @import '@/assets/gsap.css';
</style>