<template>
    <div class="explorer">
        <div class="label-wrapper" @click="toggleChildren">
            <div :style="indent" :class="labelClasses">
                <font-icon v-if="nodes" :icon="iconClasses"/>
                {{ label }}
            </div>
        </div>
        <explorer
            v-if="showChildren"
            v-for="node in nodes" 
            :key="node"
            :nodes="node.nodes"
            :label="node.label"
            :depth="depth + 1"></explorer>
    </div>
</template>
<script>
import { library } from "@fortawesome/fontawesome-svg-core";
import { faPlusSquare, faMinusSquare  } from "@fortawesome/free-solid-svg-icons";
// library.add(faCoffee, faSpinner );

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
            return this.showChildren ? faMinusSquare : faPlusSquare;
        },
        labelClasses() {
            return { "has-children": this.nodes };
        },
        indent() {
            return { transform: `translate(${this.depth * 20}px)` };
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

