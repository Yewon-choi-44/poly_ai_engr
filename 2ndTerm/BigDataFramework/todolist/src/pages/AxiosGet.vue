<template>
    <v-app>
        <v-main class="ma-4">
            data: {{ data }}
            <v-divider></v-divider>
            <div class = "my-2">LIST</div>
            <v-divider></v-divider>
            <template v-for="row in data" :key="row">
                <v-sheet> {{ row }} </v-sheet>
            </template>
            <v-btn class="my-2" @click="axiosget">
                GET
            </v-btn>
        </v-main>
    </v-app>
</template>

<script setup>
    import { ref } from 'vue'
    import axios from 'axios'
    const data = ref('')
    const url = "http://syntaxwiki.com:9993/items/?format=json"
    const axiosget = () => {
        axios.get(url, {}, {
        }).then((res) => {
            data.value = res.data.results
        })
    }
</script>