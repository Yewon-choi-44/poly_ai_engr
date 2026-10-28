<template>
    <v-container>
        <v-sheet width="400" class="mx-auto">
            <v-col>
                <div class="text-h5 font-weight-bold">Post</div>
            </v-col>
            <v-form>
                <v-text-field
                    v-model="title"
                    prepend-icon="mdi-format-title"
                    label="title">
                </v-text-field>
                <v-textarea
                    v-model="content"
                    label="content"
                    prepend-icon="mdi-content-paste"
                    clearable>
                </v-textarea>
                <v-text-field
                    v-model="author"
                    prepend-icon="mdi-subtitles"
                    label="author"
                ></v-text-field>

                <v-file-input
                    v-model="pictures"
                    prepend-icon=""
                    append-inner-icon="mdi-image-search"
                    label="picture"
                ></v-file-input>

                <n-date-input
                    v-model="dueDate"
                    prepend-icon="mdi-clipboard-text-clock"
                    label="picture">
                </n-date-input>

                <v-row>
                    <v-spacer></v-spacer>
                    <v-btn
                        variant="elevated"
                        color="blue"
                        class="text-none ma-2"
                        @click="submitForm"
                        prepend-icon="mdi-plus"
                    >저장</v-btn>
                    <v-btn
                        variant="elevated"
                        class="text-none ma-2"
                        to="/"
                        prepend-icon="mdi-close"
                    >닫기</v-btn>
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
    const author = ref('')
    const pictures = ref()

    const api = ""
    console.log('여기까진 됨')
    const submitForm = () => {
        axios.post('http://syntaxwiki.com:9993/blogposts/', {
            title: title.value,
            content: content.value,
            author: author.value,
            picture1: pictures.value},{
            headers:{
                'Content-Type': 'multipart/form-data'
            }
        }).then((res) => {
            alert('등록되었습니다.')
        }).catch((error) => {
            alert(error)
        })
    }
</script>