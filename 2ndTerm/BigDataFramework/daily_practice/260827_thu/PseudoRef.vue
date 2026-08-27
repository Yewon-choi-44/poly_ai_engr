<template>
    <span style= "color:red"><h1>아래에 자식 컴포넌트가 있습니다...</h1></span>
    <button @click="count.value++">
        {{ count.value }}
    </button>
</template>

<script setup>
    // 실제 구현이 아닌 유사 코드
    import { getCurrentInstance } from 'vue'
    const instant = getCurrentInstance()
    const count = {
        _value: 0,
        get value() {
            // track()
            console.log('get', this._value)
            return this._value
        },
        set value(newValue) {
            this_value = newValue
            console.log('set', this_value)
            //trigger()
            if(instant) {
                instant.proxy.$forceUpdate()
            }
        }
    }
</script>