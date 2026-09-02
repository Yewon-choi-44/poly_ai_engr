<template>
    <v-container>
        Parent Model: {{ textModel }}
        <hr>
        <ChildComp v-model="textModel" class="my-3" />
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    import ChildComp from '@/components/ChildComp.vue'
    const textModel = ref('init')
</script>