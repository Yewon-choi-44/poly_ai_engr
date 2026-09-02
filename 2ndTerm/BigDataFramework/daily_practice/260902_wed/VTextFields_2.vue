<template>
    <v-container>
        <div>{{ text1 }}</div>
        <v-text-field label="Label" prepend-icon="$vuetify" v-model="text1"></v-text-field>

        <div>{{ text2 }}</div>
        <v-text-field label="Label" prepend-inner-icon="mdi-abjad-arabic" clearable v-model="text2"></v-text-field>

        <div>{{ text3 }}</div>
        <v-text-field label="Label" append-icon="mdi-menu" variant="underlined" clearable v-model="text3"></v-text-field>
    </v-container>
    
    <a :href="icon_change" target="_blank" rel="noopener noreferrer">아이콘 변경 외부 링크 </a>
</template>

<script setup>
    import { ref } from 'vue'
    const text1 = ref('text1')
    const text2 = ref('text2')
    const text3 = ref('text3')

    const icon_change = ref('https://pictogrammers.com/library/mdi/')
</script>