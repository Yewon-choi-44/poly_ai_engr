<template>
    <v-container>
        <v-row>
            <v-col>
                Title Model: {{ textTitle }}
                <hr>
                SubTitle Model: {{ textSubTitle }}
                <hr>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="6">
                <div class="mt-6">Named v-model</div>
                <hr>
                <ChildCompParam
                    v-model:title="textTitle"
                    v-model:subtitle="textSubTitle"
                    class="my-3" />
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    import ChildCompParam from '@/components/ChildCompParam.vue'
    const textTitle = ref('titleParent')
    const textSubTitle = ref('subtitleParent')

</script>