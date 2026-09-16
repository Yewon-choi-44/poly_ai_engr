<template>
    <v-container>
        <v-btn @click="show = !show">토글: 슬라이드+페이드</v-btn>
        <Transition name="slide-fade" class="ma-3">
            <p v-if="show">안녕</p>
            
        </Transition>
         <Transition name="slide-fade1" class="ma-3">
            <p v-if="show">안녕</p>
            
        </Transition>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    const show = ref(true)
</script>

<style scoped>
    .slide-fade-enter-active {
        transition: all 0.3s ease-out;
    }
    .slide-fade-leave-active {
        transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
    }
    .slide-fade-enter-from,
    .slide-fade-leave-to {
        transition: translateY(40px);
        opacity: 0;
    }


    .slide-fade1-enter-active {
        transition: all 0.9s ease-out;
    }
    .slide-fade1-leave-active {
        transition: all 1.0s cubic-bezier(2, 0.9, 0.8, 3);
    }
    .slide-fade1-enter-from {
        transition: translateX(40px);
    }
    .slide-fade1-leave-to {
        transition: translateY(40px);
        opacity: 0;
    }
</style>