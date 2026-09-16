<template>
    <v-container class="fill-height">
        <v-row justify="center" align-content="center">
            <div ref="title" class="title-text">404 Page not found</div>
            <div class="title-text" ref="exclamation">!</div>
            <div class="break"></div>
            <div ref="subtitle" class="subtitle-text">
                OOPS! We couldn't find that page.
            </div>
        </v-row>
    </v-container>
</template>

<script setup>
    import { onMounted, onUnmounted, ref } from 'vue';
    import gsap from 'gsap';

    const title = ref(null)
    const subtitle = ref(null)
    const main = ref()
    let tl
    let ctx

    const splitText = (element) => {
        const text = element.innerText;
        element.innerHTML = "";
        text.split("").forEach((char) => {
            const span = document.createElement("span");
            span.innerText = char === " " ? "\u00A0" : char;
            element.appendChild(span);
        });
    };

    onMounted(() => {
        splitText(title.value)
        splitText(subtitle.value)
        ctx = gsap.context((self) => {
            tl = gsap.timeline()
            tl.set(title.value.children, {
                opacity: 0, y: 50
            }).set(subtitle.value.children, {
                opacity: 0, y: 50
            })
            
            .to(title.value.children, {
                opacity: 1, y: 0,
                stagger: 0.05,
                duration: 2,
                ease: "back.out(1.7)"
            })
            
            .to(exclamation.value, {
                opacity: 1,
                y: 0,
                stagger: 0.05,
                duration: 0.1,
                ease: "back.out(1,7)"
            }, 1)
            
            .to(subtitle.value.children, {
                opacity: 1,
                y: 0,
                stagger: 0.05,
                duration: 2,
                ease: "back.out(1.7)"
            }, 1).fromTo(exclamation.value, {
                rotationY: 0,
            }, {
                rotationY: 180,
                color: '#ff5722',
                duration: 1,
                stagger: 0.1,
                repeat: -1,
                yoyo: true,
                ease: "power1.inOut"
            }, 2);
        })
    })
    
    onUnmounted(() => {
        ctx.revert();
    });
</script>

<style lang="scss" scoped>
    .break {
        flex-basis: 100%;
        height: 0;
    }

    .title-text {
        font-size: 5rem;
        perspective: 800px;
    }

    .subtitle-text {
        font-size: 2rem;
        color: #616162;
    }
</style>

<route lang="json">
    {
        "path": "/:pathMatch(.*)*"
    }
</route>