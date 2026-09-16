<template>
    <v-container>
        <v-text-field v-model="query" 
            label = "Keyword"
            width="200"
            prepend-icon="mdi-magnify"
            variant="outlined"
        />

        <TransitionGroup 
            tag="ul"
            :css="false"
            @before-enter="onBeforeEnter"
            @enter="onEnter"
            @leave="onLeave"
            class="mx-4">

            <li v-for="(item, index) in computedList"
            :key="item.msg"
            :data-index="index">{{ item.msg }}</li>
        </TransitionGroup>
    </v-container>
</template>

<script setup>
    import { ref, computed } from 'vue'
    import gsap from 'gsap'

    const query = ref('') 
    const list = ref([             
        { msg: 'apple' },
        { msg: 'banana' },
        { msg: 'cherry' },
        { msg: 'durian' },
    ])

    const computedList = computed(() => {
        return list.value.filter((item) => item.msg.toLowerCase().includes(query.value))
    })

    const onBeforeEnter = (el) => {
        el.style.opacity = 0
        el.style.height = 0
    }

    const onEnter = (el, done) => {
        gsap.to(el, {
            opacity: 1,
            height: '1.6em',
            delay: el.dataset.index * 0.5,
            onComplete: done
        })
    }

    const onLeave = (el, done) => {
        gsap.to(el, {
            opacity: 0,
            height: 0,
            delay: el.dataset.index * 0.5,
            onComplete: done
        })
    }
</script>