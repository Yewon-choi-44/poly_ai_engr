<template>
    <v-container>
        <v-btn @click="show = !show">토글</v-btn>
        <Transition
            @before-enter="onBeforeEnter"
            @enter="onEnter"
            @leave="onLeave"
            :css="false">
            <div class="gsap-box" v-if="show"></div>
        </Transition>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    import gsap from 'gsap'
    const show = ref(true)
    
    const onBeforeEnter = (el) => {
        gsap.set(el, {
            scaleX: 0.25,
            scaleY: 0.25,
            opacity: 1
        })
    }

    const onEnter = (el, done) => {
        gsap.to(el, {
            duration: 1,
            scaleX: 1,
            scaleY: 1,
            opacity: 1,
            ease: 1,
            ease: 'elastic.inOut(2.5,1)',
            onComplete: done
        })
    }

    const onLeave = (el, done) => {
        gsap.to(el, {
            duration: 0.7,
            scaleX: 1,
            scaleY: 1,
            x: 300,
            ease: 'elastic.inOut(2.5, 1)'
        })
        gsap.to(el, {
            duration: 0.2,
            delay: 0.5,
            opacity: 0,
            onComplete: done
        })
    }
</script>
<style scoped>
    .gsap-box {
        background: #42b883;
        margin-top: 20px;
        width: 20px;
        height: 30px;
        border-radius: 50%;
    }
</style>