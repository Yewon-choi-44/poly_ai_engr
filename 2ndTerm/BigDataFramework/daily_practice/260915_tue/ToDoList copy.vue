<template>
    <v-container class="pa-10">
        <v-row>
            <v-col>
                <div class="text-h5 font-weight-bold">To Do List</div>
            </v-col>
            <v-spacer></v-spacer>

            <v-col text-right align-self="center">
                <v-btn variant="elevated" color="red" class="text-none mr-5" to="/createtodo">
                <span class="mr-2">
                    <v-icon class="mr-2">mdi-plus</v-icon>Create New Card
                </span>
                </v-btn>
            </v-col>
        </v-row>
        <v-row justify-start class="mt-7">
            <ToDoCard v-for="item in cards" :item="item" :key="item.id"></ToDoCard>
            <v-card v-for="item in cards"
                :key="item.id"
                elevation="12"
                width="468"
                gradient="to botton, rgba(0, 0, 0, .1), rgba(0,0,0,.5)"
                class="ma-4">

                <v-card-title>{{ item.title }}</v-card-title>
                <v-card-subtitle>{{ item.created_at }} # {{ item.remote_ip }} </v-card-subtitle>
                <v-card-subtitle>DueTo {{ item.due_date }} D: {{ item.description }} </v-card-subtitle>
                <v-card-text>{{ item.content }}</v-card-text>
                <v-card-actions>
                    <v-btn color="blue-darken-4 ma-1" variant="flat" prepend-icon="mdi-details">Details</v-btn>
                    <v-spacer></v-spacer>
                    <v-btn size="small" color="surface-variant" variant="text" icon="mdi-heart"></v-btn>
                    <v-btn size="small" color="surface-variant" variant="text" icon="mdi-bookmark"></v-btn>
                    <v-btn size="small" color="surface-variant" variant="text" icon="mdi-share-variant"></v-btn>
                </v-card-actions>
            </v-card>
        </v-row>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    import axios from 'axios'

    const cards = ref([{}])

    axios.get('http://syntaxwiki.com:9993/items/?format=json', { }, {
        headers: {
            'Access-Control-Allow-Headers': '*',
        }
    }).then(function(response) {
        cards.value = response.data.results
    })
</script>