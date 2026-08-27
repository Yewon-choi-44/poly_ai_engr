<template>
    <v-container class="d-flex flex-column fill-height pa-0">
        <v-btn-toggle v-model="filter" mandatory density="comfortable">   
            <v-btn value="all" >전체</v-btn>
            <v-btn value="incomplete" >미완료</v-btn>
        </v-btn-toggle>
    
        <div class="flex-grow-1 overflow-y-auto px-4" style="min-height: 0;">
            <template v-for="todo in todos" :key="todo.id">
                <v-card v-if="filter == 'all' || !todo.isComplete" class="mx-auto" width="400">
                    <v-card-title>{{ todo.name }}</v-card-title>
                    <v-card-text class="bg-surface-light pt-4">{{ todo.title }}</v-card-text>
                </v-card>
            </template>
        </div>
    </v-container>
</template>

<script setup>
    import { ref, reactive } from 'vue'
    let itemList = [...Array(8).keys()].map(i => {
        return {
            id: `${i}`, name: `name${i+1}`,
            title: `title${i}`, isComplete: Boolean(i % 2)
        }
    })
    const filter = ref('all')
    const todos = reactive(itemList)
</script>