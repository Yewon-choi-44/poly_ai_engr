<script setup>
    import { ref } from 'vue'
    const checked = ref(true)
    const checkedNames = ref([])
</script>

<template>
    <input type="checkbox" id="checkbox" v-model="checked"/>
    <label for="checkbox">{{ checked }}</label>
    <p>선택된 객체 {{ checked }}</p>

    <v-divider></v-divider>

    <div>체크된 이름: {{ checkedNames }}</div>

    <input type="checkbox" id="jack" value="젝" v-model="checkedNames">
    <label for="jack">잭</label>

    <input type="checkbox" id="john" value="존" v-model="checkedNames">
    <label for="jack">존</label>

    <input type="checkbox" id="mike" value="마이크" v-model="checkedNames">
    <label for="jack">마이크</label>
</template>