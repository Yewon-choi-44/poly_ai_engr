<template>
    <div class = "fill-height d-flex flex-column align-center justify-center">
        <div class="border d-flex flex-column justify-center pa-10 signup-box">
            <div class="logo my-10 align-self-center"></div>
            <div>가입하세요!</div>
            <v-form @submit.prevent>
                <v-text-field
                    density="compact" label="사용자 ID"
                    variant="outlined" v-model="form.username">
                </v-text-field>
            
                <v-text-field
                    density="compact" label="비밀번호"
                    variant="outlined" v-model="form.password1">
                </v-text-field>

                <v-text-field
                    density="compact" label="사용자이름"
                    variant="outlined" v-model="form.first_name">
                </v-text-field>

                <v-file-input
                    v-model="files" prepend-icon=""
                    density="compact" variant="outlined"
                    append-inner-icon="mdi-image-search"
                    label="프로필 사진">
                </v-file-input>

                <v-btn
                    text="가입" variant="flat" color="indigo" @click="submit" block>
                </v-btn>
        </v-form>
    </div>
    <div class="border mt-5 pa-8 signup-box d-flex justify-center">
        <div class="py-2">계정이 있으신가요?</div>
        <v-btn variant="plain" to="/login">
            <div class="login-btn">로그인</div>
        </v-btn>
    </div>
    </div>

    <v-snackbar v-model="snackbar">
        {{  snackbarText }}
        <template v-slot:actions>
            <v-btn color="pink" variant="text"
            @click="snackbar = false">Close</v-btn> 
        </template>
    </v-snackbar>
</template>

<script setup>
    import { ref } from 'vue'
    import axios from 'axios'
    const form = ref({
        username: '',
        password1: '',
        password2: '',
        first_name: ''
    })

    const files = ref([])
    const snackbar = ref(false)
    const snackbarText = ref('')
    const isEmpty = value => {
        if (value === null || value === undefined || value === '')
            return true
        return !!(Array.isArray(value) && value.length === 0)
    }

    const host = '/api'
    const api = '/authuser/'
    const submit = () => {
        form.value.password2 = form.value.password1;
        if(isEmpty(form.value.username)) {
            snackbarText.value = '유저명을 입력해주세요.'
            snackbar.value = true
        } else if(isEmpty(form.value.password1)) {
            snackbarText.value = '비밀번호를 입력해주세요.'
            snackbar.value = true
        } else if(form.value.password1 != form.value.password2) {
            snackbarText.value = '비밀번호와 확인이 다릅니다.'
            snackbar.value = true
        } else {
            axios.post(`${host}${api}`, {...form.value, picture: files.value}, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(() => {
                snackbarText.value = '계정이 생성되었습니다.'
                snackbar.value = true
            }).catch((error) => {
                alert(error.response.data)
            })
        }
    }
</script>

<style scoped>
    @import "@/assets/custom.css";
</style>