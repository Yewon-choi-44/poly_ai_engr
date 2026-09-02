<template>
    <v-container>
        Parent Model: {{ textModel1 }}
        <hr>
        
        <div class="mt-6">Type #1</div>
        <hr>
        <ChildCompIn v-model="textModel1" class="my-3" />

        <div>Type #2</div>
        Parent Model: {{ textModel2 }}
        <hr>
        <ChildCompIn v-model="textModel2" class="my-3" />
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    import ChildCompIn from '@/components/ChildCompIn2.vue'
    const textModel1 = ref('init')
    const textModel2 = ref('init')
</script>