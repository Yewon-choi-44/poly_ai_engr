<template>
    <div class="position-relative border box-orange" style="top: 20px; left: 20px; ">
        Relative
    </div>
    <div class="position-absolute border box-orange" style="margin-top:30px; top: 20px; left:20px;">
        Absolute
    </div>

    <div class="parent border-dotted border-orange pa-4 position-relative" 
    style="margin-top: 60px; height: 200px; width: 600px;">
        <div class="child border-dotted position-absolute" style>
            child1
        </div>
        <div class="child border-dotted position-absolute" :style="{top: child2top + 'px', left:child2left + 'px'}">
            child2
        </div>
        <div class="child border-dotted position-absolute" style="right: 10px; bottom: 20px;">
            child3
        </div>
    </div>

    <v-number-input
        style="width: 200px"
        class="ma-2"
        controlVariant="stacked"
        variant="solo"
        v-model="child2top"
        :hideInput="false"
        label="top(px)">
    </v-number-input>

    <v-number-input
        style="width: 200px"
        class="ma-2"
        controlVariant="stacked"
        variant="solo"
        v-model="child2left"
        :hideInput="false"
        label="top(px)">
    </v-number-input>

    <div>grant-parent</div>
        <div class="grand-parent border-dotted position-relative pa-4" style="margin-top: 60px;">
            <div class="parent border-dotted pa-4" style="margin-top: 60px; height: 200px; width: 600px;">
                <div class="child border-dotted position-absolute">absolute-child1</div>
                <div class="child border-dotted position-absolute" style="top: 20px;">absolute(t20)-child2</div>
                <div class="child border-dotted position-absolute" style="right: 10px; bottom: 20px;">absolute(r10, b20)-child3</div>
                <div class="child border-dotted position-absolute">relative(t40)-child2</div>
            </div> 
        </div>
</template>

<style lang="scss" scoped>
    .box-orange {
        background-color: orange;
    }
    .box-orange {
        border-color: orange;
    }

    .parent {
        border-color: orange;
    }
    .grant-parent {
        border-color: red;
    }
</style>

<script setup>
    
</script>