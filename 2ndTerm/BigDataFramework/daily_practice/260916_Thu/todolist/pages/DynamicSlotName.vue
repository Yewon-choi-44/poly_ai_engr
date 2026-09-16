<template>
    <BaseLayout>
        <template v-slot:[currentSlot]>
            <p>This is the content for the {{ currentSlot }}</p>
        </template>
    </BaseLayout>

    <v-btn @click="changeSlot('header')">Show Header</v-btn>
    <v-btn @click="changeSlot('default')">Show Default</v-btn>
    <v-btn @click="changeSlot('footer')">Show Footer</v-btn>
</template>

<script setup>
import BaseLayout from '@/components/BaseLayout.vue';
import { ref } from 'vue'

const currentSlot = ref('header')
const changeSlot = (name) => {
    currentSlot.value = name
}
</script>