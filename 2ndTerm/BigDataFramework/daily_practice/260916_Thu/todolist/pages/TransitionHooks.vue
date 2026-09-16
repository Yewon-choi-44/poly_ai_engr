<template>
    <v-container>
        <v-btn @click="show = !show">토글</v-btn>
        <Transition
            class="ma-4"
            name="slide-fade"
            @before-enter="onBeforeEnter"
            @enter="onEnter"
            @after-enter="onAfterEnter"
            @enter-cancelled="onEnterCancelled"
            @before-leave="onBeforeLeave"
            @leave="onLeave"
            @after-leave="onAfterLeave"
            @leave-cancelled="onLeaveCancelled">
            <p v-if="show">안녕</p>
        </Transition>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'

    const show = ref(true)

    // 엘리먼트가 DOM에 삽입되기 전에 호출됨
    // 이것을 사용하여 엘리먼트의 "enter-from" 상태 설정
    function onBeforeEnter(el) { console.log('before-enter') }

    
    // 엘리먼트가 삽입되고 1 프레임 후 호출됨.
    // 진입 애니메이션을 시작하는 데 사용함
    function onEnter(el, done) {
        // CSS와 함께 사용되는 경우, 선택적으로 트랜지션 종료 나타내기 위해 done 콜백 호출
        console.log('enter')
        // done()
        // 호출 즉시 트래지션 종료
    }

    // 진입 트랜지션이 완료되면 호출
    function onAfterEnter(el) { 
        console.log('after-enter')
    }

    // 진입 트랜지션 취소가 완료되기 전 호출
    function onEnterCancelled(el) {
        console.log('enter-cancelled')
    }

    // 진출 훅 전에 호출
    // 대부분의 경우 그냥 진출 훅을 사용해야 함ㄴ
    function onBeforeLeave(el) {
        console.log('before-leave')
    }

    // 진출 트랜지션이 시작될 때 호출
    // 진출 애니메이션을 시작하는 데 사용
    function onLeave(el, done) { 
        // CSS와 함께 사용되는 경우 선택적으로 트랜지션 종료 나타내기 위해 done 콜백 호출
        console.log('leave')
        // done()
    }

    // 진출 트랜지션 완료 후, 엘리먼트가 DOM에서 제거된 후 호출
    function onAfterLeave(el) {
        console.log('after-leave')
    }

    // v-show 트랜지션에서만 사용 가능
    function onLeaveCancelled(el) {
        console.log('leave-cancelled')
    }
</script>

<style scoped>
    .slide-fade-enter-active {
        transition: all 3s ease-out;
    }
    .slide-fade-leave-active {
        transition: all 2s cubic-bezier(1, 0.5, 0.8, 1);
    }
    .slide-fade-enter-from, .slide-fade-leave-to {
        transform: translateX(40px);
        opacity: 0;
    }
</style>