<template>
    <v-container>
        Parent Model: {{ textModel }}
        <hr>
        <div class="mt-6">Type #1</div>
        <hr>
        <ChildCompIn v-model="textModel" class="my-3" />

        <div>Type #2</div>
        <hr>
        <ChildCompIn
            :modelValue="textModel"
            @update:modelValue="$event => (textModel = $event)"
            class="my-3" />
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    import ChildCompIn from '@/components/ChildCompIn.vue'
    const textModel = ref('init')
</script>