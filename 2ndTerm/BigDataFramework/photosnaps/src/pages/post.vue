<script setup lang="ts">
import { preview } from 'vite';

</script>

<template>
    <v-container class="d-flex fill-height">
        <v-sheet width="400" class="mx-auto">
            <v-col>
                <div class="text-h5 font-weight-bold">POST</div>
            </v-col>
            <v-img :height="previewH" :src="preview" cover class="my-4 ml-10"></v-img>
            <v-form>
                <v-file-input
                    density="compact" variant="outlined"
                    v-model="pictures" prepend-icon="mdi-image-search"
                    chips multiple @change="onFileChange"
                    label="Picture">
                </v-file-input>
                <v-text-field
                    v-model="title" density="compact"
                    variant="outlined" prepend-icon="mdi-format-title"
                    label="title"    
                ></v-text-field>
                <v-textarea
                    v-model="content" label="content" density="outlined"
                    variant="outlined" prepend-icon="mdi-content-paste" clearable
                ></v-textarea>
                <v-text-field
                    v-model="author" density="compact" variant="outlined"
                    prepend-icon="mdi-account-circle-outline" label="author"
                ></v-text-field>
                <v-row>
                    <v-spacer></v-spacer>
                    <v-btn
                        variant="elevated" color="blue"
                        class="text-none ma-2" @click="submitForm"
                        prepend-icon="mdi-plus">공유
                    </v-btn>
                    <v-btn
                        variant="elevated" class="text-none ma-2"
                        to="/postlist" prepend-icon="mdi-close">닫기
                    </v-btn>
                </v-row>
            </v-form>
        </v-sheet>
    </v-container>
</template>

<script setup>
    import { ref } from 'vue'
    import axios from 'axios'

    const title = ref('')
    const content = ref('')
    const author - ref('')
    const pictures = ref([])
    const preview = ref()
    const previewH = ref(0)
    const onFileChange = (event) => {
        if(event.target.files.length > 5) {
            pictures.value = []
            alert('사진을 5개 이하만 선택할 수 있습니다.')
            return
        }
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();

            reader.onload = (e) => {
                previewH.value = 250
                preview.value = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    }
    const submitForm = () => {
        axios.post('/api/posts/', {
            title: title.value,
            content: content.value,
            author: author.value,
            pictures: pictures.value
        }, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then((res) => {
            alert('성공')
        }).catch(error) => {
            alert('실패')
        })
    }
</script>