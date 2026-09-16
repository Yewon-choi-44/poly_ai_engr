<template>
    <v-container>
        <v-btn @click="show = !show">토글</v-btn>
        <Transition name = "nested" @after-enter="logging">
            <div v-if="show" class="outer ma-2">
                Hello
                <div class="inner ma-2">
                    안녕
                </div>
            </div>
        </Transition>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    const show = ref(true)
    const logging = () => {
        console.log('logging')
    }
</script>

<style scoped>
    .nested-enter-active,
    .nested-leave-active {
        transition: all 1s linear;
    }

    .nested-enter-from,
    .nested-leave-to {
        transform: translateX(100px);
        opacity: 0;
    }

    .nested-enter-active .inner,
    .nested-enter-active .inner {
        transition: all 2s ease-in-out;
    }

    .nested-enter-from .inner,
    .nested-leave-to .inner {
        transform: translateX(100px);
        opacity: 0;
    }

    .nested-enter-active .inner {
        transition-delay: 1s;
    }
</style>