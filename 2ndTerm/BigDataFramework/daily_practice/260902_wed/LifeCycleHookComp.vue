<template>
    <div>
        <div>count: {{ count }}</div>
        <v-btn class="ma-2" prepend-icon="$vuetify" @click="update">업데이트</v-btn>
        <v-btn class="ma-2" prepend-icon="$vuetify" @click="upmount">인마운트</v-btn>
    </div>

</template>

<script setup>
    import { onMounted, onUnMounted, onUpdated, ref } from 'vue';
    onMounted(() => { console.log('컴포넌트가 마운트 됐습니다.') })
    onUpdated(() => { console.log('컴포넌트가 업데이트 됐습니다.') })
    onUnMounted(() => { console.log('컴포넌트가 언마운트 됐습니다.') })
    const count = ref(0)
    const update = () => { count.value++ }
    const emit = defineEmits(['unmountEvt'])
    const unmount = () => { emit('unmountEvt')}

</script>