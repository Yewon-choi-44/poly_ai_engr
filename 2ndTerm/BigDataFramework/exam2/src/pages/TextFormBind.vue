<script setup>
    import { ref } from 'vue'
    const message = ref(null)
    const multiLineMessage = ref(null)
</script>

<template>
    <v-card class="ma-2 pa-2">
        <p>메세지: {{ message }}</p>
        <input class="outlined" v-model="message" placeholder="메시지 입력하기"/>
    </v-card>

    <v-card class="ma-2 pa-2">
        <p>여러 줄 메세지:</p>
        <p class="wrap height-200">{{ multiLineMessage }}</p>
        <v-divider></v-divider>
        <textarea
            class="outlined mt-3 height-200"
            v-model="multiLineMessage"
            placeholder="여러 줄 메세지 입력">
        </textarea>
    </v-card>
    
    <!-- 줄바꿈을 화면 적용 여부 결정하는 클래스 - wrap -->
</template>

<style>
    .height-200 {
        height: 200px;
    }

    .outlined {
        border-style: solid;
    }

    .wrap {
        white-space: pre-line
    }
</style>
