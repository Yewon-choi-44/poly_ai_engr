<template>
    <div>MyComponent</div>
    <MyComponent class="baz boo ma-2"/>
    <hr>
    <div>MyMultiComponent</div>
    <MyMultiComponent class="baz ma-2"/>
</template>

<script setup>
    import MyComponent from '@/components/MyComponent.vue';
    import MyMultiComponent from '@/components/MyMultiComponent.vue';
</script>

<style>
    .baz { background-color: orange; }
</style>