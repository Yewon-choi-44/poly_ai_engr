<script setup>
</script>

<template>
    <div class="alert-box ma-2">
        <strong>이것은 데모용 에러입니다.</strong>
        <slot />
    </div>
</template>

<style scoped>
    .alert-box {
        color: #666;
        border: 1px solid red;
        border-radius: 4px;
        padding: 20px;
        background-color: #f8f8f8;
    }

    strong {
        color: red;
        display: block;
    }

    strong::before {
        font: normal normal normal 24px/1 "Material Design Icons";
        content: '\F0026';
    }

</style>