<template>
    <v-container>
        <ScopedSlotComponent v-slot="slotProps">
            <div class="ma-2">
                {{ slotProps.text }}
            </div>
            <hr>
            <div class="ma-2">
                {{ slotProps.text }}
            </div>
        </ScopedSlotComponent>
    </v-container>
</template>

<script setup>
import ScopedSlotComponent from '@/componets/ScopedSlotComponent.vue';
</script>