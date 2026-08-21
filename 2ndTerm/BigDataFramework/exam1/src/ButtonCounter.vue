<script lang="js" setup> // 자바 스크립트 코드임을 명시 
import { ref } from 'vue' 

const count = ref(0) //ref() : 반응형으로 만들어주는 함수
const count1 = ref(0)
</script>

<template>
    <button @click="count++">당신은 {{ count }} 번 클릭했습니다. </button> // 텍스트 보간법 {{}}
    <div></div>
    <button @click="count1--">당신은 {{ count1 }} 번 클릭했습니다. </button>
</template>