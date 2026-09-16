<template>
    <ul>
        <li v-if="isLoading">Loading...</li>
        <li v-for="item in items">
            <slot name="item" v-bind="item"></slot>
        </li>
    </ul>
    <slot name="more" :load="load"></slot>
</template>

<script setup>
    import { onMounted, ref } from 'vue'
    const props = defineProps(['api-url', 'per-page'])
    const items = ref([])
    const isLoading = ref(true)
    const load = () => {
        isLoading.value = true
        setTimeout(() => {
            items.value.push(...[
                { body: 'Scoped Slots Guide', username: 'Evan You', likes: 20},
                { body: 'Vue Tutorial', username: 'Natalia Tepluhina', likes: 10}
            ])  
            isLoading.value = false
        }, 1000)
    }
    onMounted(() => {
        load()
    })
</script>

<style scoped>
    ul { 
        list-style-type: none;
        padding: 5px;
        background: linear-gradient(315deg, #42d392 25%, #647eff);
    }
    li {
        padding: 5px 20px;
        margin: 10px;
        bacakground: #fff;
    }
</style>