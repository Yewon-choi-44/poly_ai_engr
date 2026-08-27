<template>
    <span style= "color:red"><h1>아래에 자식 컴포넌트가 있습니다...</h1></span>
    <div>
        <button @click="mutateDeeply">trigger</button>
        <div>{{ obj.a }}</div>
        <div>{{ obj.nested.count }}</div>
        <div>{{ obj.arr }}</div>
    </div>

    <div>
        <button @click="mutateShallowly">trigger</button>
        <button @click="mutateShallowlyFixed">trigger2</button>
        <div>{{ shallowObj.a }}</div>
        <div>{{ shallowObj.nested.count }}</div>
        <div>{{ shallowObj.arr }}</div>
    </div>
</template>

<script setup>
    import { ref, shallowRef } from 'vue'

    const obj = ref({
        a: 0,
        nested: { count: 0 },
        arr: ['foo', 'bar']
    })

    const shallowObj = shallowRef({
        a: 0,
        nested: { count: 0 },
        arr: ['foo': 'bar']
    })

    const mutateDeeply = () => {
        obj.value.a++;
        obj.value.nested.count++
        obj.value.arr.push('baz')
    }

    const mutateShallowly = () => {
        shallowObj.value.a++;
        shallowObj.value.nested.count++
        shallowObj.value.arr.push('baz')
    }

    const mutateShallowlyFixed = () => {
        shallowObj.value = {
            ...shallowObj.value,
            a: shallowObj.value.a + 1,
            nested: { ...shallowObj.value.nested, count: shallowObj.value.nested.count + 1},
            arr: [...shallowObj.value.arr, 'baz']
        }
    }
</script>