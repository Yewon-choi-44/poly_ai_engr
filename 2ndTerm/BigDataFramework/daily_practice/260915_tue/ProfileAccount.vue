<template>
    <div class = "auth-wrapper d-flex align-center justify-center pa-4 auth-bg">
        <VCard class="auth-card pa-4 pt-7" max-width="448">
            <VCardItem class="justify-center">
                <VCardTitle class="font-weight-semibold text-2xl text-uppercase">User Profile</VCardTitle>
            </VCardItem>

            <VCardText class="pt-2">
                <h5 class="text-h5 font-weight-semibold mb-1">Hello! {{ username }}</h5>
                <p class="mb-0">반갑습니다.</p>
            </VCardText>

            <VCardText>
                <VForm @submit.prevent>
                    <VRow>
                        <VCol cols="12" class="text-center">
                            <VAvatar color="grey" size="300">
                                <v-img cover :src="src">사진표시</v-img>
                            </VAvatar>
                        </VCol>
                        <!-- create account -->
                        <VCol cols="12" class="text-center text-base"><span>소속 폴리텍6대학 {{ username }}</span></VCol>

                        <VCol cols="12" class="d-flex align-center"><VDivider /><span class="mx-4">or</span><VDivider /></VCol>
                        <VCol cols="6" class="text-center"><VBtn>Logout</VBtn></VCol>
                    </VRow>
                </VForm>
            </VCardText>
        </VCard>

        <v-snackbar v-model="snackbar">
            {{ snackbarText }}
            <template v-slot:actions>
                <v-btn
                    color="pink"
                    variant="text"
                    @click="snackbar = false">Close</v-btn>
            </template>
        </v-snackbar>
    </div>
</template>

<script setup>
    import axios from 'axios'
    import { onMounted, ref } from 'vue'
    import { useRouter } from 'vue-router'

    const snackbar = ref(false)
    const snackbarText = ref('')
    const router = useRouter()
    const username = ref('Unknown')
    const src = ref("https://cdn.vuetifyjs.com/images/profiles/marcus.jpg")

    const host = 'http://localhost:3000/api'
    const logout = () => {
        axios.post(`${host}/logout/`,{}, {
            withCredentials: true
        }).then(() => {
            snackbarText.value = "로그아웃되었습니다."
            snackbar.value = true
            router.push({path: '/login'})
        })
    }

    const refresh = () => {
        axios.get(`${host}/auth/`,{
            withCredentials: true
        })
        .then(function(res) {
            console.log('user', res)
            let user = res.data
            username.value = user.username
            src.value = user.picture
        })
    }

    onMounted(() => {
        refresh()
    })
</script>