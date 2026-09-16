<template>
    <v-container class="fill-height">
        <v-row justify="center" align-content="center">
            <div ref="title" class="title-text">
                <h1><br>404 Page not found!</h1>
            </div>
            <div class="break"></div>
            
            <div ref="subtitle" class="subtitle-text">
                OOPS! We couldn't find that page.
            </div>
        </v-row>
    </v-container>
</template>

<script setup>
</script>


<route lang="json">
    {
        "path": "/:pathMatch(.*)*"
    }
</route>