<template>
    <p>책을 가지고 있다:</p>
    <span>{{ publishedBooksMessage }}</span>
    <v-btn variant="text" icon="mdi-menu"></v-btn>
    <span>{{ publishedBooksMessage }}</span>
</template>

<script setup>
    import { reactive, computed } from 'vue'

    const author = reactive({
        name: 'John Doe',
        books: [
            'Vue 2 - Advanced Guide',
            'Vue 3 - Basic Guide',
            'Vue 4 - The Mystery'
        ]
    })

    // 계산된 ref
    const publishedBooksMessage = computed(() => {
        console.log('call')
        return author.books.length > 0 ? 'Yes' : 'No'
    })
</script>