<script setup>
    import { ref, computed } from 'vue'

    const firstName = ref('John')
    const lastName = ref('Doe')

    const fullName = computed({
        // getter
        get() {
            return firstName.value + ' ' + lastName.value
        },
        // setter
        set(newValue) {
            // Note: we are using destrucutring assignment syntax here.
            [firstName.value, lastName.value] = newValue.split(' ')
        }
    })
</script>

<template>
    <v-app>
    <v-main class = "pa-4">
        <v-text-field
            label="FullName"
            @update:modelValue="newValue => fullName = newValue"
        ></v-text-field>
        <v-list>
        <v-list-item>
            <v-list-item-title>
                FullName: {{ fullName }}
            </v-list-item-title>
            <v-list-item-subtitle>
                FirstName: {{ firstName }}
                LastName: {{ lastName }}
            </v-list-item-subtitle>
        </v-list-item>
        </v-list>
    </v-main>
    </v-app>
</template>