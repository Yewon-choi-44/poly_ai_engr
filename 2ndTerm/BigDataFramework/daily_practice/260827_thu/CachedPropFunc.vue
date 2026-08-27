<script setup>
    import { ref, reactive, computed } from 'vue'

    const author = reactive({
        name: 'John Doe',
        books: [
            'Vue 2 - Advanced Guide',
            'Vue 3 - Basic Guide',
            'Vue 4 - The Mystery'
        ]
    })

    
    const publishedBooksMessage = computed(() => {
        console.log('computed')
        return author.books.length > 0 ? 'Yes' : 'No'
    })

    const calculateBooksMessage = () => {
        console.log('calculate')
        return author.books.length > 0 ? 'Yes' : 'No'
    }
</script>

<template>
    <p>computed property</p>
    <br>
    <p>Has published books:</p>
    <span>#1 {{ publishedBooksMessage }}</span>
    <span>#2 {{ publishedBooksMessage }}</span>
    <span>#3 {{ publishedBooksMessage }}</span>
    <br>
    <br>
    <p>method</p>
    <hr>
    <p>Has published books:</p>
    <span>#1 {{ calculateBooksMessage() }}</span>
    <span>#2 {{ calculateBooksMessage() }}</span>
    <span>#3 {{ calculateBooksMessage() }}</span>
</template>