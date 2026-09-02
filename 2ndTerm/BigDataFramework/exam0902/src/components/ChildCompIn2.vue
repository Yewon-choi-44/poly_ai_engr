<template>
    <v-container class="border-md border-info">
        <v-row>
            <div class="ma-2">
                부모 바인딩 v-model은: {{ modelValue }}
            </div>
        </v-row>
        <v-row>
            <input
                :value="props.modelValue"
                @input="emit('update:modelValue', $event.target.value)"
                class="ma-2 border-thin pa-2"
            />
        </v-row>
    </v-container>
</template>

<script setup>
    const props = defineProps(['modelValue'])
    const emit = defineEmits(['update:modelValue'])
</script>