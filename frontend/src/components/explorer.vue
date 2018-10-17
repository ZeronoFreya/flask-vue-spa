<template>
    <div class="explorer">
        <div class="label-wrapper" @click="toggleChildren">
            <div :style="indent" :class="labelClasses">
                <i v-if="nodes" class="fa" :class="iconClasses"></i>
                {{ label }}
            </div>
        </div>
        
        <explorer
            v-if="showChildren"
            v-for="node in nodes"
            :nodes="node.nodes"
            :label="node.label"
            :depth="depth + 1"></explorer>
    </div>
</template>
<script>
export default {
    props: ["label", "nodes", "depth"],
    data() {
        return {
            showChildren: false,
        };
    },
    name: "explorer",
    computed: {
        iconClasses() {
            return {
                "fa-plus-square-o": !this.showChildren,
                "fa-minus-square-o": this.showChildren,
            };
        },
        labelClasses() {
            return { "has-children": this.nodes };
        },
        indent() {
            return { transform: `translate(${this.depth * 50}px)` };
        },
    },
    methods: {
        toggleChildren() {
            this.showChildren = !this.showChildren;
        },
    },
};
</script>
<style lang="scss" scoped>
.explorer {
    text-align: left;
    .label-wrapper {
        padding-bottom: 10px;
        margin-bottom: 10px;
        border-bottom: 1px solid #ccc;
        .has-children {
            cursor: pointer;
        }
    }
}
</style>

