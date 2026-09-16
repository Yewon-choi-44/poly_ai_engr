<template>
    <FancyList api-url="url" :per-page="10">
        <template #item="{ body, username, likes }">
            <div class="item">
                <p>{{ body }} </p>
                <p class="meta">by {{ username }} | {{ likes }} likes </p>
            </div>
        </template>
        <template #more="{ load:loadMore }">
            <v-btn  @click = "loadMore"> More... </v-btn> //내부 함수를 사용
        </template>
    </FancyList>
</template>

<script setup>
    import FancyList from "@/components/FancyList.vue";
</script>

<style scoped>
    .meta {
        font-size: 12px;
        color: #42b883;
    }
</style>
