<template>
    <div>
        <button :disabled="isButtonDisabledf1">False 버튼1 - {{ isButtonDisabeldf1 }}</button>
        <button :disabled="isButtonDisabledf2">False 버튼2 - {{ isButtonDisabledf2 }}</button>
        <button :disabled="isButtonDisabledf3">False 버튼3 - {{ isButtonDisabledf3 }}</button>
        <button :disabled="isButtonDisabledf4">False 버튼4 - {{ isButtonDisabledf4 }}</button>
    </div>
    <div>
        <button :disabled="isButtonDisabledt1">True 버튼1 - {{ isButtonDisabeldt1 }}</button>
        <button :disabled="isButtonDisabledt2">True 버튼2 - {{ isButtonDisabledt2 }}</button>
        <button :disabled="isButtonDisabledt3">True 버튼3 - {{ isButtonDisabledt3 }}</button>
    </div>
</template>

<script lang="js" setup>
    import { ref } from 'vue'
    const isButtonDisabledf1 = ref(false)
    const isButtonDisabledf2 = ref(null)
    const isButtonDisabledf3 = ref(undefined)
    const isButtonDisabledf4 = ref(0)
    
    const isButtonDisabledt1 = ref(true)
    const isButtonDisabledt2 = ref("")
    const isButtonDisabledt3 = ref("true")
</script>

<style scoped>
    div {
        display: flex;
        flex-direction: column;
    }
    button {
        margin: 5px;
    }
</style>