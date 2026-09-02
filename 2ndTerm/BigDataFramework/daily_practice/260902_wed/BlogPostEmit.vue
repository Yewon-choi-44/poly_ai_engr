<script setup>

    defineProps(['title'])
    const emit = defineEmits(['enlarge-text'])

    const enlarge = () => {
        // $emit('enlarge-text')
        emit('enlarge-text')
    }
</script>

<template>
    <div class = "blog-post">
        <h4>{{ title }}</h4>
        <v-btn @click="$emit('enlarge-text')">텍스트 크게</v-btn>
        <v-btn @click="enlarge">텍스트 크게</v-btn>
    </div>
</template>

<style scoped>
    .blog-post {
        margin: 10px;
        border: 1px solid;
        padding: 5px;
    }

</style>