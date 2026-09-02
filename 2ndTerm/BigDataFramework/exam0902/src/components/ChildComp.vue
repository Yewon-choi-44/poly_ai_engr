<template>
    <v-container class="border-md border-info">
        <v-row>
            <div class="ma-2">
                부모 바인딩 v-model은: {{ model }}
            </div>
        </v-row>
        <v-row>
            <input v-model="model" class="ma-2 border-thin pa-2"/>
        </v-row>
    </v-container>
</template>

<script setup>
    const model = defineModel()
</script>