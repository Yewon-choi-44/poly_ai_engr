<template>
    <v-container>
        <v-btn @click="insert" class="ma-2">무작위 인덱스에 추가</v-btn>
        <v-btn @click="remove" class="ma-2">무작위 인덱스에 삭제</v-btn>
        <TransitionGroup name="list" tag="ul" class="ma-4">
            <li v-for="item in items" :key="item">{{ item }}</li>
        </TransitionGroup>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    const items = ref([1, 2, 3, 4, 5])
    let id = items.value.length + 1

    const insert = () => {
        const i = Math.round(Math.random() * items.value.length)
        items.value.splice(i, 0, id++)
    }

    const remove = (item) => {
        const i = Math.round(Math.random() * items.value.length)
        items.value.splice(i, 1)
    }
</script>

<style scoped>
    .list-enter-active,
    .list-leave-active {
        transition: all 0.5s ease;
    }
    .list-enter-from,
    .list-leave-to {
        opacity: 0;
        transform: translateX(30px);
    }
</style>