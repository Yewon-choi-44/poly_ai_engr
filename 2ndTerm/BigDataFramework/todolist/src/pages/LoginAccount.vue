<template>
    <v-layout class="auth-wrapper d-flex align-center justify-center auth-bg">
        <VCard class="auth-card pa-4 pt-7" max-width="448">
            <VCardItem class="justify-center">
                <VCardTitle class="font-weight-semibold text-2xl text-uppercase">
                    To Do List
                </VCardTitle>
            </VCardItem>
            <VCardText class="pt-2">
                <p class="mb-0">로그인하세요.</p>
            </VCardText>
            <VCardText>
                <VForm @submit.prevent="() => {}">
                    <VRow>
                        <!-- email -->
                        <VCol cols = "12">
                           <VTextField v-model = "form.username" label="Username" />
                        </VCol>

                        <!-- password -->
                        <VCol cols="12">
                            <VTextField 
                                v-model = "form.password"
                                label = "Password"
                                :type="isPasswordVisible ? 'text' : 'password'"
                                :append-inner-icon="isPasswordVisible ? 'mdi-eye-off-outline' : 'mdi-eye-outline'"
                                @click:append-inner = "isPasswordVisible = !isPasswordVisible"/>

                            <!-- remember me checkbox -->
                            <div class="d-flex align-center justify-space-between flex-wrap mt-1 mb-4">
                                <VCheckbox v-model="form.remember" label="Remember me"/>
                            </div>

                            <!-- login button -->
                            <VBtn block @click="submit" text="Login"/>
                           </VCol>
                           <!-- create account -->
                           <VCol cols="12" class="text-center text-base">
                                <span>New on our platform?</span>
                                <RouterLink class="text-primary ms-2" to="/signup">계정 생성</RouterLink>
                           </VCol>
                    </VRow>
                </VForm>
            </VCardText>
        </VCard>
        <v-snackbar v-model="snackbar">
            {{ snackbarText }}
            <template v-slot:actions>
                <v-btn color="pink" variant="text" @click="snackbar = false">Close</v-btn>
            </template>
        </v-snackbar>
    </v-layout>
</template>

<script setup>
    import axios from 'axios'
    import { ref } from 'vue'
    import { useRouter } from 'vue-router'

    const snackbar = ref(false)
    const snackbarText = ref('')
    const router = useRouter()

    const form = ref({
        username: '',
        password: '',
        remember: false,
    })

    const isPasswordVisible = ref(false)
    const api = 'http://localhost:3000/api/login/'

    const submit = () => {
        axios.post(api, {
            username: form.value.username,
            password: form.value.password
        }, {
            withCredentials: true
        }).then((res) => {
            if(form.value.remember) {
                consol.log('set userInfo')
                window.localStorage.setItem('userLogin', btoa(JSON.stringify(form.value)))
            } else {
                window.localStorage.removeItem('userLogin')
            }
            window.sessionStorage.setItem('userInfo', btoa(JSON.stringify(res.data.data)))
            axios.defaults.headers.common['X-CSRFToken'] = res.data.csrftoken
            snackbarText.value = '로그인 성공'
            snackbar.value = true
            router.push({path: 'profileaccount'})
        }).catch(() => {
            snackbarText.value = '로그인 정보를 바르게 입력하세요.'
            snackbar.value = true
        })
    }

    //

    let strUserLogin = window.localStorage.getItem('userLogin')
    if(strUserLogin) {
        const userLogin = JSON.parse(window.atob(strUserLogin))
        console.log('userLogin', userLogin)
        form.value = userLogin
    }
</script>

<style scoped>
    @import '@/assets/main.css';
</style>