<template>
    <div class = "auth-wrapper d-flex align-center justify-center pa-4 auth-bg">
        <VCard class="auth-card pa-4 pt-7" max-width="448">
            <VCardItem class="justify-center">
                <VCardTitle class="font-weight-semibold text-2xl text-uppercase">
                    To Do List
                </VCardTitle>
            </VCardItem>
            
            <VCardText class="pt-2">
            <h5 class="text-h5 font-weight-semibold mb-1">
                계정 생성
            </h5>
            <p class="mb-0">계정 정보를 입력하세요.</p>
        </VCardText>

        <VCardText>
            <VForm @submit.prevent="submit">
                <VRow>
                    <VCol cols="12">
                        <VTextField v-model="form.username" label="Username" />
                    </VCol>
                    
                    <!-- password1 -->
                    <VCol cols="12">
                        <VTextField
                            v-model = "form.password1"
                            label = "Password"
                            :type="isPassword1Visible ? 'text' : 'password'"
                            :append-inner-icon="isPassword1Visible ? 'mdi-eye-off-outline' : 'mdi-eye-outline'"
                            @click:append-inner="isPassword1Visible = !isPassword1Visible" />
                            
                            <!-- password2 -->
                            <VTextField
                            v-model="form.password2"
                            label="Confirm Password"
                            class="mt-2"
                            :type="isPassword2Visible ? 'text' : 'password'"
                            :append-inner-icon="isPassword2Visible ? 'mdi-eye-off-outline' : 'mdi-eye-outline'"
                            @click:append-inner="isPassword2Visible = !isPassword2Visible"
                            />
                        </VCol>
                        
                        <VCol cols="12">
                            <v-file-input
                                v-model="files"
                                prepend-icon=""
                                append-inner-icon="mdi-image-search"
                                label="Profile Picture">
                            </v-file-input>
                        </VCol>

                        <VCol cols="12">
                        <VBtn block type="submit" text="Sign Up" />
                    </VCol>

                    <!-- login instead -->
                    <VCol cols="12" class="text-center text-base">
                        <span>Already have an account?</span>
                        <RouterLink class="text-primary ms-2" to="login">로그인</RouterLink>
                    </VCol>

                    <VCol cols="12" class="d-flex align-center">
                        <VDivider />
                        <span class="mx-4">or</span>
                        <VDivider />
                    </VCol>
                </VRow>
            </VForm>
        </VCardText>
        </VCard>
    </div>
    <v-snackbar
        v-model="snackbar">
        {{ snackbarText }}
        <template v-slot:actions>
            <v-btn
                color="pink"
                variant="text"
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
    })
    const files = ref([])
    const isPassword1Visible = ref(false)
    const isPassword2Visible = ref(false)
    const snackbar = ref(false)
    const snackbarText = ref('')
    const isEmpty = value => {
        if (value === null || value === undefined || value === '')
            return true
        return !!(Array.isArray(value) && value.length === 0)
    }
    const host = 'http://syntaxwiki.com:9993'
    const api = '/authuser/'
    const submit = () => {
        if (isEmpty(form.value.username)) {
        snackbarText.value = '유저명을 입력해주세요.'
        snackbar.value = true
    } else if(isEmpty(form.value.password1)) {
        snackbarText.value = '비밀번호를 입력해주세요.'
        snackbar.value = true
    } else if(form.value.password1 != form.value.password2) {
        snackbarText.value = '비밀번호와 확인이 다릅니다.'
        snackbar.value = true
    } else {
        axios.post(`${host}${api}`, {...form.value, picture: files.value} , {
            headers: {
                'Content-Type' : 'multipart/form-data'
            }
        }).then(() => {
            snackbarText.value = '계정이 생성되었습니다.'
            snackbar.value = true
        }).catch((error) => {
            alert(error)
        })
    }
}
</script>

<style scoped>
    @import '@/assets/main.css';
</style>