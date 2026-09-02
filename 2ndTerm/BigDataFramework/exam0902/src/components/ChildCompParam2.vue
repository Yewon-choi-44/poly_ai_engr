<template>
    <v-container class="border-md border-info">
        <v-row>
            <v-col>
                <div> title: {{ titleM }} </div>
                <div> subtitle: {{ subtitleM }}</div>
                <div> content: {{ contentM }}</div>

                <div class="my-2">
                    <span class="mr-2">Title: </span>
                    <input class="border-md w-75" v-model="titleM"/>
                </div>
                <div class="my-2">
                    <span class="mr-2">SubTitle: </span>    
                    <input class="border-md" v-model="subtitleM"></input>    
                </div>
                <div class="my-2">
                    <span class="mr-2">Content: </span>    
                    <input class="border-md" v-model="contentM"></input>    
                </div>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
    const titleM = defineModel('title')
    const subtitleM = defineModel('subtitle')
    const contentM =defineModel('content')
</script>