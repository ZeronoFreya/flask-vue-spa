<template>
  <div class="about">
    <h1>This is an about page</h1>
    <explorer 
        :label="tree.label" 
        :folders="tree.folders"
        :files="tree.files"></explorer>
  </div>
</template>
<script>
import axios from "axios";
import explorer from "@/components/explorer.vue";
export default {
    data() {
        return {
            rootDir: "e:\\Fonts",
            tree: {
                "label": "root",
                "folders": [
                    {
                        "label": "folder1",
                        "folders": [
                            {
                                "label": "folder1.1",
                            },
                            {
                                "label": "folder1.2",
                                "folders": [
                                    {
                                        "label": "folder1.2.1",
                                        "files": ["file1.2.1.1", "file1.2.1.2"]
                                    },
                                ],
                            },
                        ],
                        "files": ["file1.1", "file1.2"],
                    },
                    {
                        "label": "folder2",
                    },
                ],
                "files": ["file0.1", "file0.2"]
            },
        };
    },
    methods: {
        getSelectFolderList() {
            const path = "http://localhost:5000/api/dl/listdir2";
            axios
                .post(path, {
                    rootDir: this.rootDir
                })
                .then(response => {
                    // this.randomNumber = response.data.randomNumber;
                    // console.log(response.data);
                    this.tree = response.data
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

