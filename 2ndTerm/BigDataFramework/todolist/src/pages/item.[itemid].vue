<template>
    <v-container>
        <v-card class="pa-4 pt-7" max-width="600">
            <v-card-item>
                <v-card-title>{{ item.title }}</v-card-title>
                <v-card-subtitle class="pt-2">
                    <v-icon icon="mdi-alarm"></v-icon>
                    등록 {{ item.created_at }} # {{ item.remote_ip }}
                </v-card-subtitle>
                <v-card-subtitle class="pt-2 text-pink">
                    <v-icon icon="mdi-alarm"></v-icon>
                    만료 {{ item.due_date }}
                </v-card-subtitle>
                <v-card-text class="text-h6">
                    {{ item.content }}
                </v-card-text>
            </v-card-item>
            <v-divider class="mx-4 mb-1"></v-divider>
            <v-card-subtitle>{{  item.description }}</v-card-subtitle>
            <v-card-actions>
                <v-btn
                    text="Back"
                    block= border
                    color="orange" to="/"    
                ></v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script setup>
    import { ref, onMounted } from 'vue'
    import { useRoute } from 'vue-router'
    import axios from 'axios'

    //dynamic route에서 파라미터를 획득
    const route = useRoute()
    const itemid = route.params.itemid
    const item = ref({})

    const load = () => {
        axios.get(`http://syntaxwiki.com:9993/item/${itemid}`).then((res) => {
            console.log('res', res)
            item.value = res.data
        })
    }
    onMounted(() => {
        load()
    })
</script>