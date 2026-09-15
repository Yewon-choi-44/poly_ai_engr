<template>
    <v-app-bar color="teal-darken-4">
        <template v-slot:image>
            <v-img gradient = "to top right, rgba(19, 84, 122, .8), rgba(128, 208, 199, .8)">
            </v-img>
        </template>
        <template v-slot:prepend>
            <v-btn icon>
                <v-icon>mdi-apps</v-icon>
            </v-btn>
        </template>
        <v-app-bar-title>
            ToDoList
        </v-app-bar-title>
    </v-app-bar>
</template>

<script setup>
</script>