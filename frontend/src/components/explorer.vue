<template>
    <div class="explorer">
        <div class="label-wrapper" @click="toggleChildren">
            <div>
                <font-icon :icon="folderStatus"/>
                {{ label }}
            </div>
        </div>
        <div class="label-main" v-if="showChildren">
            <explorer
                v-for="folder in folders" 
                :key="folder.label"
                :folders="folder.folders"
                :files="folder.files"
                :label="folder.label"></explorer>
            <div class="label-wrapper"
                v-for="file in files"
                :key="file"
                >
                <div>
                    <font-icon icon="file"/>
                    {{ file }}
                </div>
            </div>
        </div>
        
    </div>
</template>
<script>
// import { library } from "@fortawesome/fontawesome-svg-core";
// import { faPlusSquare, faMinusSquare  } from "@fortawesome/free-solid-svg-icons";
// library.add(faCoffee, faSpinner );

export default {
    props: ["label", "folders", "files"],
    data() {
        return {
            showChildren: false,
        };
    },
    name: "explorer",
    computed: {
        folderStatus() {
            return this.showChildren ? "folder-open" : "folder";
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
        // border-bottom: 1px solid #ccc;
        cursor: pointer;
    }
    .label-main{
        padding-left: 30px;
        border-left: 1px #ddd solid;
        margin-left: 6px;
    }
}
</style>

