<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div>
        <p>demo</p>
        <ul>
            <li class="folders"
                @click="">
                <input type="checkbox">
                <i>@</i>
                <span>folder</span>
                <div class="ctrl-btn-contain">
                    <button type="button">del</button>
                </div>
            </li>
            <li class="file">
                <input type="checkbox">
                <i>#</i>
                <span>file</span>
                <div class="ctrl-btn-contain">
                    <button type="button">del</button>
                </div>
            </li>
        </ul>
    </div>
    <explorer 
        :label="tree.label" 
        :nodes="tree.nodes"
        :depth="0"></explorer>
  </div>
</template>
<script>
import axios from "axios";
import explorer from "@/components/explorer.vue";
export default {
    data() {
        return {
            rootDir: "f:\\Project\\Python",
            list: {
                name: "demo",
                folders: [
                    {
                        name: "folder1",
                        folders: [
                            {
                                name: "folder1-1",
                            },
                        ],
                        files: [],
                    },
                    {
                        name: "folder2",
                    },
                ],
                files: ["file1", "file2"],
            },
            tree: {
                label: "root",
                nodes: [
                    {
                        label: "item1",
                        nodes: [
                            {
                                label: "item1.1",
                            },
                            {
                                label: "item1.2",
                                nodes: [
                                    {
                                        label: "item1.2.1",
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        label: "item2",
                    },
                ],
            },
        };
    },
    methods: {
        getSelectFolderList() {
            const path = "http://localhost:5000/api/dl/listdir2";
            axios
                .post(path, {
                    rootDir: "f:\\Project\\Python",
                    idx: 2,
                })
                .then(response => {
                    // this.randomNumber = response.data.randomNumber;
                    console.log(response.data);
                })
                .catch(error => {
                    console.log(error);
                });
        },
    },
    created() {
        // this.getSelectFolderList();
    },
    components: {
        explorer,
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

