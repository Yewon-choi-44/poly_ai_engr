<template>
    <v-container>
        <input ref="eleRef" class="border-md mx-3" />
        <v-btn @click="getValue">참조확인1</v-btn>
        <ul>
            <li v-for="item in list" ref="itemRefs" class="ma-2">
                {{ item }}    
            </li>
        </ul>
        <v-btn @click="getItemRefs">참조확인2</v-btn>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    const eleRef = ref(null)
    const getValue = () => {
        alert('eleRef Value ' + eleRef.value.value)
    }

    const list = ref([1, 2, 3])
    const itemRefs = ref([])
    const getItemRefs = () => {
        itemRefs.value.forEach((ele) => {
            console.log(ele)
            console.log(ele.innerHTML)
        })
    }
</script>