<template>
    <v-container class="d-flex align-center justify-center fill-height">
        <div class="screed mx-4 left">
            <img 
            v-for="(image, index) in images"
            :src="image"
            :key="index"
            ref="slides"
            class="screen-img"/>
        </div>
        <div class="mx-4 pa-4 right">
            <div class="border pa-4 login-right d-flex flex-column justify-center">
                <v-form @submit.prevent>
                    <v-text-field 
                        density="compact"
                        label="사용자이름"
                        variant="outlined"
                        v-model="form.username"
                        autocomplete="username">
                    </v-text-field>
                    <v-text-field
                        dentsity="compact"
                        label="비밀번호"
                        variant="outlined"
                        type="password"
                        v-model="form.password"
                        autocomplete="current-password"
                    ></v-text-field>
                    <v-btn 
                    text="로그인" 
                    variant="flat" 
                    color="indigo" 
                    @click="submit" 
                    block></v-btn>
                </v-form>
            </div>
            <div class="border pa-4 mt-4 d-flex justify-center">
                <div class="py-2">계정이 없으신가요?</div>
                <v-btn
                    variant="plain"
                    to="/signup">
                    <div class="signup-btn" >가입하기</div>
                </v-btn>
            </div>
        </div>
        <v-snackbar v-model="snackbar">
            {{  snackbarText }}
            <template v-slot:actions>
                <v-btn color="pink" variant="text"
                    @click="snackbar = false">
                    close
                </v-btn>
            </template>
        </v-snackbar>
    </v-container>
</template>

<script setup>
import axios from 'axios';
import gsap from 'gsap';
import {ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user'

import screenshot1 from '@/assets/screenshot1-2x.png'
import screenshot2 from '@/assets/screenshot2-2x.png'
import screenshot3 from '@/assets/screenshot3-2x.png'
import screenshot4 from '@/assets/screenshot4-2x.png'

const images = [screenshot1, screenshot2, screenshot3, screenshot4];
const slides = ref([]);
let tl, ctx;

onMounted(() => {
    ctx = gsap.context((self) =>{
        tl = gsap.timeline({repeat: -1, repeatDelay: 1});
        slides.value.forEach((slide) => {
           tl.to(slide, { opacity: 1, duration: 1})
           .to(slide, { opacity: 0 , duration: 1}, "+=1");
       });
   });
});

onUnmounted(() => {
    ctx.revert();
});
const snackbar = ref(false)
const snackbarText = ref('')
const router = useRouter()

const form = ref({
    username: '',
    password: ''
})

const api = '/api/login/'

const submit = () => {
    axios.post(api, {
        username: form.value.username,
        password: form.value.password
    }, {
        withCredentials: true
    }).then((res) => {
        const userStore = useUserStore()
        userStore.login(res.data.sessionid)
        axios.defaults.headers.common['X-CSRFToken'] = res.data.csrftoken
        snackbarText.value = '로그인 성공'
        snackbar.value = true
        router.push({path: '/postlist' })
    }).catch((e) => {
        console.error(e)
        snackbarText.value = '로그인 정보를 바르게 입력하세요.'
        snackbar.value = true
    })
}
</script>

<style scoped>
    @import "@/assets/custom.css";
</style>