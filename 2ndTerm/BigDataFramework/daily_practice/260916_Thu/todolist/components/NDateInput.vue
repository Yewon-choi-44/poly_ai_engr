<template>
    <v-text-field
        v-model="display"
        :label="props1.label"
        prepend-icon="$calendar"
        @click:control="onClick"
        @click:prepend="onClick"
        readonly clearable
        persistent-clear
        @click:clear="onClear">
        
        <v-menu 
            v-model="menu"
            :close-on-content-click="false"
            activator="parent">
            <v-confirm-edit
                v-model="model"
                @save="onSave">
                <template v-slot:default="{ model: proxyModel, actions }">
                    <v-date-picker
                        v-model = "proxyModel.value"
                        weeks-in-month="dynamiic"
                        :hide-header="true">
                        <!-- OK Btn -->
                        <template v-slot:actions>
                            <component :is="actions"></component>
                        </template>
                    </v-date-picker>
                </template>
            </v-confirm-edit>
        </v-menu>
    </v-text-field>
</template>

<script setup>
    import { shallowRef, computed } from 'vue'
    import { DateTime } from 'luxon'

    const props1 = defineProps(['label'])
    const menu = shallowRef(false)
    const model = defineModel()
    const display = computed({
        get() {
            let dt = DateTime.fromJSDate(model.value)
            if (dt.isValid) {
                return dt.toFormat('yyyy-MM-dd')
            }
            return ''
        }
    })

    const onSave = () => {
        menu.value = false
    }

    const onClick = (e) => {
        e.preventDefault()
        e.stopPropagation()
    }

    const onClear = (e) => {
        model.value = null
    }
</script>