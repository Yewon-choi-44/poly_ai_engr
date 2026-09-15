<template>
    <v-container>
        <div> header </div>
        <header>
            <slot name="header"></slot>
        </header>
        <hr>
        <div> main </div>
        <main><slot></slot></main>
        <hr>
        <div> footer </div>
        <footer>
            <slot name="footer"></slot>
        </footer>
    </v-container>
</template>