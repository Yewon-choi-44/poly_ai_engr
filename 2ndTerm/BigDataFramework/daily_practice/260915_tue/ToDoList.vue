<template>
<v-container class="pa-10">
    <v-row>
        <v-col>
            <div class="text-h5 font-weight-bold">
                <VAvatar
                  color="grey"
                  size="36">
                  <v-img cover :src="picture"></v-img>
                </VAvatar>
                To Do List
            </div>
            <div class="ma-2">안녕하세요. {{ username }} 님!</div>
        </v-col>
        <v-col class="text-right" align-self="center">
            <v-btn
                variant="elevated" 
                class="text-none mr-5"
                @click="refresh">
                <v-icon>
                    mdi-refresh
                </v-icon>
            </v-btn>

            <v-btn
                variant="elevated" 
                color="red" 
                class="text-none mr-5"
                to="/createtodo">
                <span class="mr-2">
                    <v-icon class="mr-2">
                        mdi-plus
                    </v-icon>
                     New Card
                </span>
            </v-btn>
        </v-col>
    </v-row>

    <v-row justify-start class="mt-7">
        <!-- VHover 예제-->
        <ToDoCard v-for="item in cards" :key="item.id" :item="item"></ToDoCard>
    </v-row>
</v-container>
</template>

<script setup>
    import { onMounted, ref } from 'vue'
    import axios from 'axios'
    import ToDoCard from './ToDoCard.vue';

    const cards = ref([{}])
    const username = ref('unknown')
    const picture = ref('https://cdn.vuetifyjs.com/images/profiles/marcus.jpg')
    
    const host = 'http://syntaxwiki.com:9993'
    

    const refresh = () => {
        axios.get(`${host}/items/?format=json`,{ 
            //withCredentials: true
        }, {
        }).then(function(response) {
            cards.value = response.data.results
        })
    }

    const loadUser = () => {
      axios.get(`${host}/auth/`,{ }, {
        withCredentials: true
      })
      .then(function(res) {
        console.log(res)
        let user = res.data
        username.value = user.username
        picture.value = user.picture
    })}
    
    onMounted(() => {
        loadUser()
        refresh()
    })
</script>
<style scoped>
    .item {
        flex: 1 1 calc(50% - 10px);
        margin: 5px;
        box-sizing: border-box;
        display: flex;
    }

</style>