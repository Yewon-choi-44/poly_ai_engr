<template>
    <div>
        <MyComponent v-slot="slotProps">
            1 {{ slotProps.text }} {{ slotProps.count }}
        </MyComponent>

        <MyComponent v-slot="{ text, count }">
            2 {{ text }} {{ count }}
        </MyComponent>
    </div>
</template>

<script setup>
import MyComponent from '@/components/MyComponent.vue';
</script>