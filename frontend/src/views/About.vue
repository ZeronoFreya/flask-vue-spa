<template>
  <div class="about">
    <h1>This is an about page</h1>
    <explorer
        :target.sync="rootDir"
        :is-open="true"></explorer>
    <!-- <vue-ztree :list.sync="ztreeDataSourceSync"
        :expand="expandClick"
        :is-open="false"
        :is-check="false"></vue-ztree> -->
  </div>
</template>
<script>
import axios from "axios";
import explorer from "@/components/explorer.vue";
import vueZtree from "@/components/vue-ztree.vue";
export default {
    data() {
        return {
            rootDir: "e:\\DownLoad",
        };
    },
    methods: {
    },
    created() {
        // this.getSelectFolderList();
    },
    components: {
        vueZtree, explorer
    },
};
</script>
<style lang="scss" scoped>
li {
    text-align: left;
    white-space: nowrap;
    cursor: pointer;
    &:hover {
        background-color: #eeeeee;
        .ctrl-btn-contain {
            display: block;
        }
    }
    > span {
        margin-left: 10px;
    }
}
.ctrl-btn-contain {
    float: right;
    display: none;
}
</style>

